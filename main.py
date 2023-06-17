from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"data": "Rest API"}

@app.post("/api/story")
def post_api_story():
    return {"data": "sample response"}
