from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    obj = {
        "message": "안녕하세요!",
        "user": "bhy"   
    }
    return obj
@app.get("/hello")
def hell(name="hong"):
    print("name is", name)
    return {
        "name":name
    }