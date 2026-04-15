from langchain_groq import ChatGroq
from prompts.matching_prompt import matching_prompt

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

matching_chain = matching_prompt | llm
