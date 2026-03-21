from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

# fake DB
db = {}

# models
class SubmitRequest(BaseModel):
    contract_code: str
    user_input: dict

class VerifyRequest(BaseModel):
    request_id: str


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/api/submit")
def submit(req: SubmitRequest):
    request_id = str(uuid.uuid4())

    db[request_id] = {
        "contract_code": req.contract_code,
        "user_input": req.user_input,
        "result": None
    }

    return {
        "request_id": request_id,
        "status": "submitted"
    }


@app.post("/api/verify")
def verify(req: VerifyRequest):
    if req.request_id not in db:
        return {"error": "not found"}

    data = db[req.request_id]

    # mock AI logic
    if ">" in data["contract_code"]:
        result = "approved"
        confidence = 0.95
    else:
        result = "rejected"
        confidence = 0.6

    db[req.request_id]["result"] = result

    return {
        "request_id": req.request_id,
        "result": result,
        "confidence": confidence
    }


@app.get("/api/history")
def history():
    return [
        {"request_id": k, "result": v["result"]}
        for k, v in db.items()
    ]