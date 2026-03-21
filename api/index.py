from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# fake DB
history_db = []

class ContractRequest(BaseModel):
    contract: str

@app.get("/")
def root():
    return {"status": "ok", "message": "API running 🚀"}

@app.post("/submit")
def submit(data: ContractRequest):
    result = {
        "action": "submit",
        "contract": data.contract,
        "status": "received"
    }
    history_db.append(result)
    return result

@app.post("/verify")
def verify(data: ContractRequest):
    result = {
        "action": "verify",
        "verified": True,
        "risk": "Low"
    }
    history_db.append(result)
    return result

@app.get("/history")
def history():
    return {"history": history_db}