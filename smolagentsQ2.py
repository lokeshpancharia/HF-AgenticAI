from smolagents import CodeAgent, ToolCallingAgent, HfApiModel
from smolagents.tools import DuckDuckGoSearchTool

# Initialize the web search tool
search_tool = DuckDuckGoSearchTool()

# Define the correct model using HfApiModel
model = HfApiModel(model="Qwen/Qwen2.5-Coder-32B-Instruct")

# Create the web search agent
web_agent = ToolCallingAgent(
    tools=[search_tool],  # Add required tools
    model=model,          # Correct model reference
    max_steps=10,         # Adjusted to match reference solution
    name="WebSearchAgent",  
    description="An agent that performs web searches using DuckDuckGo."
)

# Create manager agent with `managed_agents` instead of `agents`
manager_agent = CodeAgent(
    managed_agents=[web_agent],  # Corrected key here
    model=model,  
    name="ManagerAgent",  
    description="A manager that delegates tasks to specialized agents."
)
