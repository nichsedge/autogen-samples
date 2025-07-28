from autogen_core.models import ModelInfo, UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
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