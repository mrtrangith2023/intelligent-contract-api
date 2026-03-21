from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

history = []

class ContractSubmission(BaseModel):
    user: str
    action: str
    data: dict

@router.post("/submit")
def submit_contract(submission: ContractSubmission):
    record = submission.dict()
    record["timestamp"] = datetime.utcnow().isoformat()
    history.append(record)
    return {"status": "ok", "message": "Contract submitted", "id": len(history)-1}

@router.post("/verify")
def verify_contract(submission_id: int):
    try:
        submission = history[submission_id]
        if submission["action"] in ["mint", "transfer"]:
            return {"status": "success", "submission": submission}
        return {"status": "fail", "reason": "Invalid action"}
    except IndexError:
        return {"status": "error", "reason": "Submission ID not found"}

@router.get("/history")
def get_history():
    return history