from agents.company_agent import scrape_website
from services.llm_service import call_llm
import json

def generate_datavex_profile():

    website_text = scrape_website("datavex.ai")

    prompt = f"""
    Based ONLY on the website content below, extract structured information:

    - product_description
    - target_customers
    - core_features
    - value_proposition
    - industries_served

    Return JSON only.

    Website Content:
    {website_text}
    """

    structured_data = call_llm(prompt)

    # Save locally
    with open("datavex_profile.json", "w") as f:
        json.dump(structured_data, f, indent=4)

    print("Datavex profile saved successfully.")


if __name__ == "__main__":
    generate_datavex_profile()