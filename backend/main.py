from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agents.company_agent import analyze_company
from agents.fit_agent import analyze_fit
from agents.scoring_agent import calculate_score
from agents.strategy_agent import generate_strategy
from pydantic import BaseModel
import json
class AnalyzeRequest(BaseModel):
    domain: str
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):

    domain = request.domain

    company_info = analyze_company(domain)
    fit_info = analyze_fit(company_info)
    score_info = calculate_score(company_info, fit_info)

    raw_strategy = generate_strategy(company_info)

    try:
        parsed = json.loads(raw_strategy)

        strategy_info = {
            "subject_line": parsed.get("subject_line", ""),
            "email_body": parsed.get("email_body", "")
        }

    except Exception as e:
        print("Strategy JSON parsing failed:", e)

        # Fallback: treat entire response as plain email text
        strategy_info = {
            "subject_line": "",
            "email_body": raw_strategy
        }

    return {
        "domain": domain,
        "company_analysis": company_info,
        "fit_analysis": {
            **fit_info,
            **score_info
        },
        "strategy": strategy_info
    }