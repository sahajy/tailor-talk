import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

print("DEBUG TOGETHER_API_KEY =", os.getenv("TOGETHER_API_KEY"))

from langchain_together import Together
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from backend.gcal_utils import book_appointment, check_availability

# Initialize the Together AI LLM
llm = Together(
    model="meta-llama/Llama-3-8b-chat-hf",
    temperature=0.5,
    max_tokens=512,
    together_api_key=os.getenv("TOGETHER_API_KEY")
)

# Define LangChain-compatible tools
tools = [
    Tool(
        name="book_appointment",
        func=book_appointment,
        description="Books an appointment using 'YYYY-MM-DD HH:MM to HH:MM' format"
    ),
    Tool(
        name="check_availability",
        func=check_availability,
        description="Checks availability for time slot 'YYYY-MM-DD HH:MM to HH:MM'"
    )
]

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Agent runner function
def run_agent(query: str) -> str:
    return agent.run(query)
