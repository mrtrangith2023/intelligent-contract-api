from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1️⃣ Tạo app FastAPI
app = FastAPI(title="Intelligent Contract API")

# 2️⃣ CORS để frontend IP khác gọi API được
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # hoặc ["http://192.168.56.1:3000"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3️⃣ Include router
from api.routes import router
app.include_router(router, prefix="/api")

# 4️⃣ Root test
@app.get("/")
def read_root():
    return {"message": "Intelligent Contract API is running"}