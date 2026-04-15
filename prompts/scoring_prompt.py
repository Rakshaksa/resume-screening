from langchain_core.prompts import PromptTemplate

scoring_prompt = PromptTemplate(
    input_variables=["match_result", "job_description"],
    template="""
You are an objective scoring engine. Based on the match analysis, assign a fit score.

Match Analysis:
{match_result}

Job Description:
{job_description}

Rules:
- Score must be between 0 and 100
- Be strict and objective
- Do NOT inflate scores

Return ONLY this:
Score: <number between 0-100>
"""
)