from dotenv import load_dotenv
import os


load_dotenv()


class ExternalWrapper:

    def __init__(self, name, interests, topic, modifier, narration, character_environment, character_descriptors, openai_obj):
        self.name = name
        self.interests = interests
        self.topic = topic
        self.modifier = modifier
        self.narration = narration
        self.character_environment = character_environment
        self.character_descriptors = character_descriptors
        self.openai_obj = openai_obj

    def generate_text(self):
        S1_PROMPT = f"""
            Write a story that teaches a child about {self.topic}. 
            The story is centered around a character with the following characteristics: {", ".join(self.character_descriptors)} 
            The story is set in the universe of {self.character_environment}. 
            Write the story with the following style: {self.modifier}
            """

        resp = self.openai_obj.Completion.create(
            model="text-davinci-003",
            prompt=S1_PROMPT,
            max_tokens=350,
            temperature=0
            )

        print(resp)
        