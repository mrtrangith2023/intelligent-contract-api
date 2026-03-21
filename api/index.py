from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Fake in-memory DB
db = {}

# Models
class SubmitRequest(BaseModel):
    contract_code: str
    user_input: dict

class VerifyRequest(BaseModel):
    request_id: str

# Root endpoint
@app.get("/")
def root():
    return {"status": "ok"}

# Submit endpoint
@app.post("/api/submit")
def submit(req: SubmitRequest):
    request_id = str(uuid.uuid4())

    db[request_id] = {
        "contract_code": req.contract_code,
        "user_input": req.user_input,
        "result": None
    }

    # Log submit
    logging.info(f"Submit request_id={request_id} | input={req.user_input}")

    return {
        "request_id": request_id,
        "status": "submitted"
    }

# Verify endpoint
@app.post("/api/verify")
def verify(req: VerifyRequest):
    if req.request_id not in db:
        raise HTTPException(status_code=404, detail="Request ID not found")

    data = db[req.request_id]

    # Mock AI logic
    if ">" in data["contract_code"]:
        result = "approved"
        confidence = 0.95
        reason = "Condition in contract code satisfied"
    else:
        result = "rejected"
        confidence = 0.6
        reason = "Condition in contract code not satisfied"

    # Update DB
    db[req.request_id]["result"] = result

    # Log verify
    logging.info(f"Verify request_id={req.request_id} | result={result}")

    return {
        "request_id": req.request_id,
        "result": result,
        "confidence": confidence,
        "reason": reason
    }

# History endpoint
@app.get("/api/history")
def history():
    return [
        {"request_id": k, "result": v["result"]}
        for k, v in db.items()
    ]

# Health check
@app.get("/health")
def health():
    return {"status": "healthy"}