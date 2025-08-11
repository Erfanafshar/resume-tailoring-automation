import re
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# File paths
RESUME_PATH = "data/resume.tex"
JOB_PATH = "data/job.txt"
MASTER_INFO_PATH = "data/master_info.md"


CLIENT = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = "gpt-4o-mini"

SECTION_NAMES = ["Summary", "Experience", "Projects", "Skills"]  # you already have this

SECTION_ORDER = ["Summary", "Experience", "Projects", "Skills"]


def choose_action():
    while True:
        choice = input("\n[a]ccept  [r]etry  [s]kip  [q]uit → ").strip().lower()
        if choice in {"a","r","s","q"}:
            return choice
        print("please type a, r, s, or q")


def find_section_span(latex_text, title):
    """Return (start_idx, end_idx, body) for a \section or \section* named title."""
    sec = re.compile(rf"\\section\*?\{{\s*{re.escape(title)}\s*\}}")
    it = list(sec.finditer(latex_text))
    if not it:
        return None
    m = it[0]
    start_body = m.end()
    # next section (starred or not)
    next_sec = re.compile(r"\\section\*?\{[^}]+\}")
    m2 = next_sec.search(latex_text, pos=start_body)
    end_body = m2.start() if m2 else len(latex_text)
    body = latex_text[start_body:end_body].strip()
    return (start_body, end_body, body)

def build_prompt(job_text, section_name, section_body, master_info_text):
    return f"""You tailor LaTeX resume sections. Preserve LaTeX commands and environments.
Do not add new sections, keep lists and formatting intact. Escape special chars if introduced.

JOB AD:
{job_text}

MASTER INFO (authoritative facts you must not contradict):
{master_info_text}

SECTION NAME: {section_name}

CURRENT SECTION (LaTeX):
{section_body}

Rewrite this section to align with the job ad, keep length similar, keep LaTeX valid.
Return only the LaTeX body for this section (no extra commentary)."""

def rewrite_with_llm(job_text, section_name, section_body, master_info_text):
    prompt = build_prompt(job_text, section_name, section_body, master_info_text)
    resp = CLIENT.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a careful LaTeX resume editor."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )
    return resp.choices[0].message.content.strip()

def apply_replacement(latex_text, start_idx, end_idx, new_body):
    return latex_text[:start_idx] + "\n" + new_body.strip() + "\n" + latex_text[end_idx:]

def yn(prompt="Accept? [y/N]: "):
    try:
        return input(prompt).strip().lower() in {"y", "yes"}
    except EOFError:
        return False


def tailor_one_section(latex_text, job_text, master_info_text, section_name="Summary", max_retries=3):
    span = find_section_span(latex_text, section_name)
    if not span:
        print(f"[warn] section not found: {section_name}")
        return latex_text

    start, end, body = span
    print(f"\n--- {section_name} current ---\n")
    print((body[:600] + "...") if len(body) > 600 else body)

    tries = 0
    while True:
        proposal = rewrite_with_llm(job_text, section_name, body, master_info_text)
        print(f"\n--- {section_name} proposed ---\n")
        print((proposal[:1000] + "...") if len(proposal) > 1000 else proposal)

        action = choose_action()

        if action == "a":
            new_tex = apply_replacement(latex_text, start, end, proposal)
            print(f"[ok] {section_name} updated")
            return new_tex

        if action == "s":
            print(f"[skip] {section_name} unchanged")
            return latex_text

        if action == "q":
            print("[note] quitting without changes to this section")
            return latex_text

        # action == "r"
        tries += 1
        if tries >= max_retries:
            print("[note] reached retry limit, leaving section unchanged")
            return latex_text
        print("[retry] generating a new proposal...")


def parse_sections(latex_text):
    """
    Finds sections either by:
    1) \section{Name}
    2) optional anchors:
       % RT:START Name
       ...content...
       % RT:END Name
    Returns dict: {name: content}
    """
    out = {}

    # 2) anchor blocks win if present
    anchor_pat = re.compile(
        r"%\s*RT:START\s+(?P<name>[^\n]+)\n(?P<body>.*?)%\s*RT:END\s+(?P=name)",
        re.DOTALL
    )
    for m in anchor_pat.finditer(latex_text):
        name = m.group("name").strip()
        body = m.group("body").strip()
        out[name] = body

    # 1) fallback to \section parsing for the common names
    # split by \section{...}
    sec_pat = re.compile(r"\\section\*?\{(?P<name>[^}]+)\}")
    splits = list(sec_pat.finditer(latex_text))

    for i, m in enumerate(splits):
        name = m.group("name").strip()
        start = m.end()
        end = splits[i + 1].start() if i + 1 < len(splits) else len(latex_text)
        body = latex_text[start:end].strip()
        if name in SECTION_NAMES and name not in out:
            out[name] = body
    return out


def read_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Step 1: Load files
    resume_text = read_file(RESUME_PATH)
    job_text = read_file(JOB_PATH)
    master_info = read_file(MASTER_INFO_PATH)

    # sections = parse_sections(resume_text)
    # print("\n=== Detected sections ===")
    # for k in SECTION_NAMES:
    #     if k in sections:
    #         preview = sections[k][:200].replace("\n", " ")
    #         print(f"- {k}: {preview}...")
    #     else:
    #         print(f"- {k}: not found")


    # Tailor just Summary first
    # updated = tailor_one_section(resume_text, job_text, master_info, section_name="Summary")

    # tailor ALL parts
    updated = resume_text
    for sec in SECTION_ORDER:
        print(f"\n=== Tailoring {sec} ===")
        updated = tailor_one_section(updated, job_text, master_info, section_name=sec)

    # Write output
    out_path = "data/resume_tailored.tex"
    if os.path.exists(out_path):
        print("[note] Overwriting previous tailored file.")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"[done] Wrote {out_path}")


if __name__ == "__main__":
    main()
