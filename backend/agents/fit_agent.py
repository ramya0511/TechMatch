import json
from services.llm_service import call_llm

def analyze_fit(company_info):

    prompt = f"""
You are a lead scoring system.

Based on the company information below, return ONLY valid JSON.

Do NOT write code.
Do NOT write explanations.
Do NOT write examples.
Do NOT use markdown.
Do NOT add text before or after JSON.

Return exactly this format:

{{
  "fit_reasoning": "Short explanation of fit",
  "overlap_score": number between 0 and 100,
  "intent_score": number between 0 and 100
}}

Company Information:
{company_info}
"""

    raw_response = call_llm(prompt)

    try:
        parsed = json.loads(raw_response)
        return parsed
    except:
        print("Fit JSON parsing failed:", raw_response)
        return {
            "fit_reasoning": "Could not analyze fit properly.",
            "overlap_score": 0,
            "intent_score": 0
        }