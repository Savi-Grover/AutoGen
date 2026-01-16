import asyncio
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

api_key=os.getenv("OPEN_API_KEY")
async def main1():
    print("function 1")


    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o", api_key=api_key)

    #create 1st Agent
    Agent1= AssistantAgent(name="Agent1_MathsTeacher",model_client=openai_model_client,
                           system_message="You are a Maths Teacher, explain things like a professor, ask follow up questions")

    # create 2nd Agent
    Agent2= AssistantAgent(name="Agent2_Student", model_client=openai_model_client,
                           system_message="You are a student, ask questions")

    # method for agent group chat- list decides order of communication
    team= RoundRobinGroupChat(participants=[Agent1,Agent2],
                              termination_condition=MaxMessageTermination(max_messages=6))

    # to start chat
    team.run_stream(task="What is Algebra, how it works")

    # to print the log
    await Console(team.run_stream(task="What is Algebra, how it works"))

    # agents will keep on talking indefinetely- so need to give a terminate condition

    # 1. maximum message termination= give a stop param for roundrobin
    ## termination_condition=MaxMessageTermination(max_messages=6))

    # 2. text termination


    await openai_model_client.close()

asyncio.run(main1())