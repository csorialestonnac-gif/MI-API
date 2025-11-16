from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API funcionando"}

@app.get("/datos")
def datos():
    return {"temperatura": 22, "humedad": 55}