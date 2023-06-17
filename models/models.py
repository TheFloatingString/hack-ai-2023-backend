from pydantic import BaseModel

class UserResp(BaseModel):
    name:       str
    modifier:   str
    narration:  str
