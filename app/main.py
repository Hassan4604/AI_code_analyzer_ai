from fastapi import FastAPI

from app.Schemas.CodeAnalyses import (
    CodeAnalysesRequest,
    CodeAnalysesResponse
)

from app.Services.ai_analysis import AIAnalysis


app = FastAPI()

ai_analysis = AIAnalysis()


@app.post("/analyze", response_model=CodeAnalysesResponse)
def analyze_code(request: CodeAnalysesRequest):

    result = ai_analysis.analyze_code(
        code=request.code,
        language=request.language
    )

    return result