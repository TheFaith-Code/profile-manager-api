from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Profile Manager API is running 🚀"}

