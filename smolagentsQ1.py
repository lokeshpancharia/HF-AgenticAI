from smolagents import CodeAgent, HfApiModel
from smolagents.tools import DuckDuckGoSearchTool

# Define the correct model using HfApiModel
model = HfApiModel(model="Qwen/Qwen2.5-Coder-32B-Instruct")

# Define search tool
search_tool = DuckDuckGoSearchTool()

# Create the agent
agent = CodeAgent(
    tools=[search_tool],  # Add search tool here
    model=model           # Use HfApiModel instead of pipeline
)
