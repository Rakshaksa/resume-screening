from langchain_groq import ChatGroq
from prompts.extraction_prompt import extraction_prompt

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

extraction_chain = extraction_prompt | llm
