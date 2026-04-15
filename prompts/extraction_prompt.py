from langchain_core.prompts import PromptTemplate

extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an expert HR analyst. Extract information from the resume below.

IMPORTANT RULES:
- Only extract what is explicitly mentioned in the resume
- Do NOT assume or infer skills not present
- Be concise and factual

Resume:
{resume}

Extract and return in this exact format:
Skills: <comma-separated list>
Experience: <years and role>
Tools: <comma-separated list>
"""
)