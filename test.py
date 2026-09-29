from app.Services.ai_analysis import AIAnalysis


ai = AIAnalysis()

code = """
def add(a, b):
    return a + b
"""

result = ai.analyze_code(
    code=code,
    language="Python"
)

print("Review:")
print(result.review)

print("\nImprovements:")
print(result.improvements)

print("\nRating:")
print(result.rating)