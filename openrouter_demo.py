# Import the dependencies
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os
import asyncio

# Load the environment variables
# You should always use a .env file to store your API keys
load_dotenv()
open_router_api_key = os.getenv("OPENROUTER_API_KEY")

open_router_model_client = OpenAIChatCompletionClient(
    base_url="https://openrouter.ai/api/v1",
    model="deepseek/deepseek-r1-0528:free",
    api_key=open_router_api_key,
    model_info={
        "family": "deepseek",
        "vision": True,
        "function_calling": True,
        "json_output": False,
    },
)

assistent = AssistantAgent(
    name="myassistent",
    model_client=open_router_model_client,
    system_message="You are a helpful assistant that answers questions accurately and concisely.",
)


async def main():
    result = await assistent.run(task="What is the capital of India?")
    print(f"Result: {result.messages[-1].content}")


asyncio.run(main())
