from urllib import request

from fastapi import FastAPI

from app.Schemas.CodeAnalyses import (
    CodeAnalysisRequest,
    CodeAnalysisResponse
)

app = FastAPI()

@app.get("/analyze_request" , request=CodeAnalysisRequest)
def analyze_request():
    print(request.code)
    print(request.language)


@app.post("/analyze", response_model=CodeAnalysisResponse)
def analyze_code(request: CodeAnalysisRequest):
    return CodeAnalysisResponse(
        review="Code looks readable.",
        improvements="Add better error handling.",
        rating=8.5
    )