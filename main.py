from fastapi import FastAPI
import openai
from dotenv import load_dotenv
import os

from models.models import UserResp



load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

resp = openai.Completion.create(
        model="text-davinci-003",
        prompt="What is the largest city in the United States?",
        max_tokens=200,
        temperature=0
        )

print(resp)

app = FastAPI()

@app.get("/")
def root():
    return {"data": "Rest API"}

@app.post("/api/story")
def post_api_story(user_resp: UserResp):
    print(user_resp)
    return {"data": "sample response"}
