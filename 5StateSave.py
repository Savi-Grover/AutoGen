import asyncio
import json
import os

from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

# save state is useful if task is large - token limited so saving state helps to continue task after abrupt task termination
api_key=os.getenv("OPEN_API_KEY")
async def main1():

    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o", api_key=api_key)

    #create 1st Agent
    Agent1= AssistantAgent(name="Helper",model_client=openai_model_client,
                           system_message="You are a Helper, explain things like a professor, ask follow up questions")

    # create 2nd Agent
    Agent2= AssistantAgent(name="Student", model_client=openai_model_client,
                           system_message="You are a student, ask questions")

    # to start chat- agent 1 's fav color
    Agent1.run_stream(task="My Favorite color is blue")

    # to print the log
    await Console(Agent1.run_stream(task="My Favorite color is blue"))

    # save the state
    state=await Agent1.save_state()

    # dump it in json file ; in write mode
    with open("memory.json","w") as f:
        json.dump(state,f, default=str)

    # load it in json file ; in read mode
    with open("memory.json", "r") as f:
        saved_state=json.load(f)

    #AGENT 2 HAS no idea of fav color
    await Agent2.load_state(saved_state)

    # run the task
    await Console(Agent2.run_stream(task="What is my favorite color"))

    await openai_model_client.close()

asyncio.run(main1())