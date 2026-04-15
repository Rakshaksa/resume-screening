from langchain_groq import ChatGroq
from prompts.scoring_prompt import scoring_prompt

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

scoring_chain = scoring_prompt | llm
