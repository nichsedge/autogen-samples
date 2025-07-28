import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench
from autogen_core.models import ModelInfo

import os

model_client = OpenAIChatCompletionClient(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    model_info=ModelInfo(
        vision=False,
        function_calling=True,
        json_output=True,
        family="unknown",
        structured_output=True,
    ),
)

async def main() -> None:
    params = StdioServerParams(
        command="uvx", args=["ksei-mcp@latest"], 
        env={
            "KSEI_USERNAME": os.getenv("KSEI_USERNAME"),
            "KSEI_PASSWORD": os.getenv("KSEI_PASSWORD"),
            "KSEI_DATA_PATH": os.getenv("KSEI_DATA_PATH"),
        },
        read_timeout_seconds=60
    )

    # You can also use `start()` and `stop()` to manage the session.
    async with McpWorkbench(server_params=params) as workbench:
        assistant = AssistantAgent(
            name="Assistant",
            model_client=model_client,
            workbench=workbench,
            reflect_on_tool_use=True,
        )
        await Console(
            assistant.run_stream(task="get ksei portfolio summary and roast that portfolio")
        )


asyncio.run(main())
