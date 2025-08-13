# Resume Tailoring Automation

**Resume Tailoring Automation** is a semi-automated tool that uses a Large Language Model (LLM) to customize LaTeX-based resumes for specific job applications.  
It rewrites targeted sections of a resume (e.g., Summary, Experience, Projects, Skills) to better align with a given job description while preserving LaTeX formatting and structure.

## Overview

Many job applications benefit from resumes that are tailored to the specific role and keywords in the posting.  
This project streamlines that process by combining:

- **Your original LaTeX resume**
- **A job description or posting**
- **Your static personal information** (education, awards, contact details, etc.)

The system then:
1. Identifies the key sections to adapt.
2. Generates rewritten versions that reflect the job ad’s language and priorities.
3. Lets you interactively approve, retry, or skip each change.
4. Outputs a tailored `.tex` file, leaving the original untouched.

## Key Features

- **Section-by-section tailoring** — works on Summary, Experience, Projects, Skills, and can be extended to more.
- **Interactive approval** — you decide whether to accept, retry, or skip each proposed change.
- **Preserves LaTeX syntax** — formatting, commands, and environments are maintained.
- **Non-destructive editing** — original resume remains unchanged; tailored version is saved separately.
- **Job-aligned language** — uses the job ad text to guide LLM rewriting for relevance and keyword matching.

## Example Use Case

1. You have a master LaTeX resume containing all your experience and projects.
2. You receive a job posting for a Python Backend Engineer.
3. This tool rewrites your Summary, highlights Python-related experience, and emphasizes backend projects, producing a tailored resume ready for that application.

## Why This Exists

Tailoring a resume manually for each job can be time-consuming.  
This tool speeds up the process, helping you create high-quality, job-specific resumes while retaining control over final edits.
