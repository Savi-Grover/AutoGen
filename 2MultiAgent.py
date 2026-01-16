import asyncio
import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("OPEN_API_KEY")
async def main1():
    print("function 1")


    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o", api_key=api_key)

    MultiAgentObj= AssistantAgent(name="Multi_Agent",model_client=openai_model_client)

    image=Image.from_file("/Users/savig/PycharmProjects/AgenticAIAutomation/image.jpg")

    MultiModalMessage_message=MultiModalMessage(content=["what do you see in this image", image], source="user")

    await Console(MultiAgentObj.run_stream(task=MultiModalMessage_message))
    await openai_model_client.close()

asyncio.run(main1())