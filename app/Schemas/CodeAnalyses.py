from pydantic import BaseModel

class CodeAnalysesRequest(BaseModel):
    code:str
    language:str

class CodeAnalysesResponse(BaseModel):
    review:str
    improvements:str
    rating:float

