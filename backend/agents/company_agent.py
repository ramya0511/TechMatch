import json
from services.llm_service import call_llm

def analyze_company(domain):

    prompt = f"""
You are a company research analyst.

Return ONLY valid JSON.
Do NOT include explanation.
Do NOT include code.
Do NOT include markdown.

Return format:

{{
  "industry": "Industry name",
  "summary": "Short company summary",
  "business_model": {{
      "revenue_streams": ["item1", "item2"]
  }},
  "target_customers": ["customer1", "customer2"]
}}

Company domain:
{domain}
"""

    raw_response = call_llm(prompt)

    try:
        parsed = json.loads(raw_response)
        return parsed
    except:
        print("Company JSON parsing failed:", raw_response)
        return {
            "industry": "Unknown",
            "summary": "Could not analyze company.",
            "business_model": {
                "revenue_streams": []
            },
            "target_customers": []
        }