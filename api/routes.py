from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

history = []

class ContractSubmission(BaseModel):
    user: str
    action: str
    data: dict

# 📥 Submit Contract
@router.post("/submit")
def submit_contract(submission: ContractSubmission):
    record = submission.dict()
    record["timestamp"] = datetime.utcnow().isoformat()
    history.append(record)

    return {
        "status": "ok",
        "message": "Contract submitted",
        "id": len(history) - 1
    }

# 🔍 Verify Contract (UPGRADED with reasoning)
@router.post("/verify")
def verify_contract(submission_id: int):
    try:
        submission = history[submission_id]
        action = submission["action"]

        if action == "mint":
            return {
                "status": "approved",
                "reason": "Action 'mint' is allowed by system rules",
                "submission": submission
            }

        elif action == "transfer":
            return {
                "status": "approved",
                "reason": "Transfer action is valid under contract policy",
                "submission": submission
            }

        else:
            return {
                "status": "rejected",
                "reason": f"Action '{action}' is not supported",
                "submission": submission
            }

    except IndexError:
        return {
            "status": "error",
            "reason": "Submission ID not found"
        }

# 🤖 AI Verify (NEW ENDPOINT - VERY IMPORTANT)
@router.post("/ai-verify")
def ai_verify(data: dict):
    action = data.get("action")
    amount = data.get("data", {}).get("amount", 0)

    # Fake AI reasoning simulation
    if action == "mint" and amount > 50:
        return {
            "status": "approved",
            "reason": "AI decision: high-value mint is acceptable",
            "confidence": 0.92
        }

    elif action == "transfer":
        return {
            "status": "approved",
            "reason": "AI decision: transfer behavior is normal",
            "confidence": 0.88
        }

    return {
        "status": "rejected",
        "reason": "AI decision: suspicious or unsupported action",
        "confidence": 0.45
    }

# 📜 History
@router.get("/history")
def get_history():
    return history