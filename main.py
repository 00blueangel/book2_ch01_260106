from fastapi import FastAPI, Form
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "안녕하세요!",
        "user": "KBJ"
    }

@app.get("/hello")
def hello(
    name: Optional[str] = "홍길동",
    address: Optional[str] = "",
    phone: Optional[str] = "",
    email: Optional[str] = "",
    age: Optional[int] = 0,
    gender: Optional[str] = ""
):
    print("[GET] 사용자 정보:")
    print(f"성명: {name}, 주소: {address}, 전화번호: {phone}, 이메일: {email}, 나이: {age}, 성별: {gender}")
    return {
        "method": "GET",
        "name": name,
        "address": address,
        "phone": phone,
        "email": email,
        "age": age,
        "gender": gender
    }

@app.post("/hello")
def hello_post(
    name: str = Form(...),
    address: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...)
):
    print("[POST] 사용자 정보:")
    print(f"성명: {name}, 주소: {address}, 전화번호: {phone}, 이메일: {email}, 나이: {age}, 성별: {gender}")
    return {
        "method": "POST",
        "name": name,
        "address": address,
        "phone": phone,
        "email": email,
        "age": age,
        "gender": gender
    }
