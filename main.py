from fastapi import FastAPI
import openai
from dotenv import load_dotenv
import uvicorn
import json
import os

from models.models import UserResp
from src.external_api_wrapper import ExternalWrapper


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

@app.get("/")
def root():
    return {"data": "Rest API"}

@app.post("/dev/story")
def post_dev_story(user_resp: UserResp):

    with open("static/sample_output.json") as json_file:
        json_data = json.load(json_file)

    return json_data

@app.post("/api/story")
def post_api_story(user_resp: UserResp):
    print(user_resp)

    external_wrapper_obj = ExternalWrapper(
        name=user_resp.name,
        interests=user_resp.interests,
        topic=user_resp.topic,
        modifier=user_resp.modifier,
        narration=user_resp.narration,
        character_environment=user_resp.character_environment,
        character_descriptors=user_resp.character_descriptors,
        openai_obj=openai
    )

    return_dict = external_wrapper_obj.return_response()

    return return_dict

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)