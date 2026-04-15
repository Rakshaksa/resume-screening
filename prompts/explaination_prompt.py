from langchain_core.prompts import PromptTemplate

explanation_prompt = PromptTemplate(
    input_variables=["score", "match_result", "extracted_info"],
    template="""
You are an AI hiring assistant. Write a clear explanation of the candidate's score.

Score: {score}
Match Analysis: {match_result}
Candidate Profile: {extracted_info}

Write a 3-5 sentence explanation covering:
1. Why this score was assigned
2. Key strengths of the candidate
3. Critical gaps or weaknesses
4. Hiring recommendation (Strong Yes / Maybe / No)
"""
)