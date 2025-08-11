import os
import re

# from dotenv import load_dotenv
#
# # Load your OpenAI API key
# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

# Define file paths
RESUME_PATH = "inputs/resume.tex"
INFO_PATH = "inputs/master_info.md"
JOB_AD_PATH = "inputs/job_ad.txt"
INSTR_PATH = "inputs/instruction.md"

# Load LaTeX resume
with open(RESUME_PATH, "r", encoding="utf-8") as f:
    resume_text = f.read()

# Load personal info
with open(INFO_PATH, "r", encoding="utf-8") as f:
    personal_info = f.read()

# Load job ad
with open(JOB_AD_PATH, "r", encoding="utf-8") as f:
    job_ad = f.read()

# Load instruction markdown
with open(INSTR_PATH, "r", encoding="utf-8") as f:
    instructions_text = f.read()

# # Show preview
# print("Resume Loaded (Length):", len(resume_text))
# print("Master Info Loaded (Length):", len(personal_info))
# print("Job Ad Loaded (Length):", len(job_ad))
# print("Instruction File Loaded (Length):", len(instructions_text))


def extract_section(text, section_name):
    """
    Extracts a section from LaTeX like \section{Summary} ... until the next \section or \end{document}
    """
    pattern = rf"\\section\{{{re.escape(section_name)}\}}(.*?)(?=\\section|\\end{{document}})"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

summary_section = extract_section(resume_text, "Summary")

# print("\n Extracted Summary Section:\n")
# print(summary_section or "[ Not found]")



def build_prompt(
    instruction_text: str,
    section_name: str,
    current_section: str,
    job_ad: str,
    personal_info: str
) -> str:
    return f"""
You are a resume rewriting assistant.

Please follow the rules and logic defined in the following instruction manual for tailoring resumes:
---
{instruction_text}
---

You are now updating the **{section_name}** section.

Here is the current content of the section:
---
{current_section}
---

Here is the job ad the resume should match:
---
{job_ad}
---

Here is the personal info (skills, background, experience):
---
{personal_info}
---

Your task:
- Propose a rewritten version of the **{section_name}** section
- Use LaTeX formatting
- Follow all relevant formatting, tone, and style instructions
- Explain clearly what you changed and why

Only rewrite if there’s something useful to improve. Otherwise say so.
"""


prompt_text = build_prompt(
    instruction_text=instructions_text,
    section_name="Summary",
    current_section=summary_section,
    job_ad=job_ad,
    personal_info=personal_info
)

print("\n Final Prompt Preview:\n")
print(prompt_text[:1000] + "\n...")  # Print first 1000 characters for sanity check
