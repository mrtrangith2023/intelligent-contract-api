from pydantic import BaseModel
from datetime import datetime

class ContractSubmission(BaseModel):
    user: str
    action: str
    data: dict

# Simulate intelligent contract
class IntelligentContract:
    def __init__(self):
        self.history = []

    def submit(self, submission: ContractSubmission):
        submission_record = submission.dict()
        submission_record['timestamp'] = datetime.utcnow()
        self.history.append(submission_record)
        return {"status": "ok", "message": "Contract submitted"}

    def verify(self, submission: ContractSubmission):
        # Example simple logic
        if submission.action in ["mint", "transfer"]:
            return {"status": "success"}
        return {"status": "fail", "reason": "Invalid action"}