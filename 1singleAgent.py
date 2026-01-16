import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("OPEN_API_KEY")

async def main():
    print("function 1")

    from autogen_ext.models.openai import OpenAIChatCompletionClient
    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o", api_key=api_key)

    SingleAgentObj= AssistantAgent(name="Single_Agent",model_client=openai_model_client)
    await Console(SingleAgentObj.run_stream(task="what is 25 * 8"))
    await openai_model_client.close()

asyncio.run(main())