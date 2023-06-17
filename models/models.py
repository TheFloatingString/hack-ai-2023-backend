from pydantic import BaseModel

class UserResp(BaseModel):
    name:       str                         # child's name
    # grade:      str | None = None           # child's current grade
    # school:     str | None = None           # child's current school
    interests:  list[str] = []              # list of interests (in string)

    # curriculum: str | None = None           # current curriculum (i.e. brain)
    topic:      str                         # question about main topic

    modifier:   str                         # describe the tone (i.e. please make it mysterious)
    narration:  str                         # name of narrator (i.e. Dumbledore)

    character_environment:  str             # character environnment
    character_descriptors:  list[str] = []  # list of character descriptors