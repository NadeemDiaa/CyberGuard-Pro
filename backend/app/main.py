from fastapi import FastAPI

app = FastAPI(title="CyberGuard Pro API")

@app.get("/")
def read_root():
    return {"message": "Welcome to CyberGuard Pro API 🛡️"}
