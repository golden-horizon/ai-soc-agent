from fastapi import FastAPI, HTTPException
from collections import Counter
from case_management.case_repository import CaseRepository
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AI SOC Agent API",
    version="1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "project": "AI SOC Agent",
        "status": "running",
    }


@app.get("/cases")
def get_cases():
    repository = CaseRepository()
    cases = repository.list_cases()

    return {
        "total_cases": len(cases),
        "cases": cases,
    }


@app.get("/case/{case_id}")
def get_case(case_id: str):
    repository = CaseRepository()
    case = repository.get_case(case_id)

    if not case:
        raise HTTPException(status_code=404, detail="Case not found")

    return case


@app.get("/statistics")
def get_statistics():
    repository = CaseRepository()
    cases = repository.list_cases()

    status_counts = Counter(case.get("status", "Unknown") for case in cases)
    attack_counts = Counter(
        case.get("incident", {}).get("attack_type", "unknown")
        for case in cases
    )
    severity_counts = Counter(case.get("severity", "unknown") for case in cases)

    return {
        "total_cases": len(cases),
        "by_status": dict(status_counts),
        "by_attack_type": dict(attack_counts),
        "by_severity": dict(severity_counts),
    }    


@app.get("/high-priority")
def get_high_priority_cases():
    repository = CaseRepository()
    cases = repository.list_cases()

    high_priority_cases = [
        case
        for case in cases
        if case.get("severity") in ["Critical", "High"]
        or case.get("soc_decision") == "Escalate Immediately"
    ]

    return {
        "count": len(high_priority_cases),
        "cases": high_priority_cases,
    }