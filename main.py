# 파이썬 버전 3.7 이상 설치
# pip install fastapi
# pip install uvicorn[standard]" //실시간 미리보기
# uvicorn main:app --reload
# pip list 
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def test():
    return {"hi! FastAPI"}

