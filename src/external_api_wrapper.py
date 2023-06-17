from dotenv import load_dotenv
import os
import re


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

        self.S1_PROMPT = ""

    def return_response(self):

        return_dict = {
            "data": {
                "s1": {
                    "text": None,
                    "highlightedText": None,
                    "imageUrl": None,
                    "audioUrl": None
                },
                "s2": {
                    "text": None,
                    "highlightedText": None,
                    "imageUrl": None,
                    "audioUrl": None
                },
                "s3": {
                    "text": None,
                    "highlightedText": None,
                    "imageUrl": None,
                    "audioUrl": None
                },
                "question": {
                    "text": None
                }
            }
        }

        s1_raw_text = self.generate_text_s1()

        return_dict["data"]["s1"]["text"] = s1_raw_text.replace("<b>", "").replace("</b>", "")


        return_dict["data"]["s1"]["highlightedText"] = re.findall("<b>(.*?)</b>", s1_raw_text)


        return_dict["data"]["question"]["text"] = self.generate_question()

        return_dict["data"]["s2"]["text"] = self.generate_text_s2(
            return_dict["data"]["question"]["text"],
            return_dict["data"]["s1"]["text"]
            )

        return_dict["data"]["s3"]["text"] = self.generate_text_s3(return_dict["data"]["s1"]["text"])
        return return_dict


    def generate_text_s1(self):
        self.S1_PROMPT = f"""
            Write a story that teaches a child about {self.topic}. 
            The story is centered around a character called {self.name} with the following characteristics: {", ".join(self.character_descriptors)}. 
            The story is set in the universe of {self.character_environment}. 
            Write the story with the following style: {self.modifier}.
            Enclose the best sentence that summarizes the topic with <b> at the start, and </b> at the end.
            """

        resp = self.openai_obj.Completion.create(
            model="text-davinci-003",
            prompt=self.S1_PROMPT,
            max_tokens=350,
            temperature=0
            )
        
        return resp["choices"][0]["text"]


    def generate_text_s2(self, question, s1_generated_text):
        
        completion = self.openai_obj.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.S1_PROMPT},
                {"role": "system", "content": s1_generated_text},
                {"role": "user", "content": f"{self.name} incorrectly answered the question: {question}. Write a brief paragraph using the previous story to explain why the {self.name} answered the question incorrectly. Do not reference the user directly in the response."}
            ]
        )

        return completion["choices"][0]["message"]["content"]

    def generate_text_s3(self, s1_generated_text):
        
        completion = self.openai_obj.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.S1_PROMPT},
                {"role": "system", "content": s1_generated_text},
                {"role": "user", "content": "Generate a kind ending to this story."}
            ]
        )

        return completion["choices"][0]["message"]["content"]

    def generate_question(self):
        PROMPT = f"""
        Write a yes or no question about {self.topic}, where the correct answer should be yes.
        """

        resp = self.openai_obj.Completion.create(
            model="text-davinci-003",
            prompt=PROMPT,
            max_tokens=350,
            temperature=0
        )

        return resp["choices"][0]["text"]