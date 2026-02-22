from services.llm_service import call_llm

def generate_strategy(company_info):

    prompt = f"""
You are a B2B sales email generator.

Based on the company information below, generate a personalized outreach email.

Company Info:
{company_info}

IMPORTANT:
Return ONLY valid JSON.
Do NOT include explanations.
Do NOT include code examples.
Do NOT include markdown.
Do NOT add extra text.

Return format:

{{
  "subject_line": "Short compelling subject",
  "email_body": "Full outreach email in plain text"
}}
"""

    return call_llm(prompt)