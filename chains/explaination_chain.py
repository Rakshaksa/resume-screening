from langchain_groq import ChatGroq
from prompts.explaination_prompt import explanation_prompt

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

explanation_chain = explanation_prompt | llm
