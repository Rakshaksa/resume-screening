from langchain_core.prompts import PromptTemplate

matching_prompt = PromptTemplate(
    input_variables=["extracted_info", "job_description"],
    template="""
You are a technical recruiter. Compare the candidate profile against the job requirements.

Candidate Profile:
{extracted_info}

Job Description:
{job_description}

List the following:
Matched Requirements: <what the candidate has that matches>
Missing Requirements: <what the candidate lacks>
Partial Matches: <areas where candidate partially meets requirements>
"""
)