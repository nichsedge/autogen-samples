from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_core.models import UserMessage
import asyncio

ollama_client = OllamaChatCompletionClient(
    model="qwen2.5:3b",
)


async def main():
    result = await ollama_client.create(
        [UserMessage(content="What is the capital of France?", source="user")]
    )  # type: ignore
    print(result)


asyncio.run(main())
