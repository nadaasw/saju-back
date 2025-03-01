from fastapi import FastAPI
from saju_service import analyze_saju
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()

# ✅ CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (보안이 필요하면 특정 도메인으로 제한 가능)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

# ✅ 요청 데이터를 정의하는 Pydantic 모델 추가
class SajuRequest(BaseModel):
    birth_date: str
    birth_time: str
    name: str
    birth_place: str
    
@app.get("/")
def read_root():
    return {"message": "Welcome to Saju API"}

@app.post("/saju/")
def saju_analysis(request: SajuRequest):
    return analyze_saju(request.birth_date, request.birth_time, request.name, request.birth_place)