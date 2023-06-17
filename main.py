from fastapi import FastAPI
import openai
from dotenv import load_dotenv
import os

from models.models import UserResp
from src.external_api_wrapper import ExternalWrapper


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

    external_wrapper_obj.generate_text()

    return_dict = {
        "data": {
            "s1": {
                "text": "string",
                "highlightedText": "string",
                "imageUrl": "string",
                "audioUrl": "string"
            },
            "s2": {
                "text": "string",
                "highlightedText": "string",
                "imageUrl": "string",
                "audioUrl": "string"
            },
            "s3": {
                "text": "string",
                "highlightedText": "string",
                "imageUrl": "string",
                "audioUrl": "string"
            }
        }
    }

    return return_dict
