from google import genai
import os
from dotenv import load_dotenv
from app.Schemas.CodeAnalyses import CodeAnalysesResponse

load_dotenv()


class AIAnalysis:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def analyze_code(self, code: str, language: str) -> CodeAnalysesResponse:

        prompt = f"""
        Analyze the following {language} code.

        Provide:
        1. A detailed code review
        2. Specific improvements
        3. A rating out of 10

        Code:
        {code}
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": CodeAnalysesResponse,
            }
        )

        return CodeAnalysesResponse.model_validate_json(response.text)