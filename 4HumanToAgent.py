import asyncio
import os

from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient

from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("OPEN_API_KEY")
async def main1():

    openai_model_client = OpenAIChatCompletionClient(
        model="gpt-4o", api_key=api_key)

    #create 1st Agent
    Agent1= AssistantAgent(name="Agent1_MathsTeacher",model_client=openai_model_client,
                           system_message="You are a helpful Maths Teacher, explain to human how to solve a maths problem"
                           "When user say 'Thank You', acknowledge and say 'Lesson Complete' to end session")

    # create human user
    user_proxy= UserProxyAgent(name="Agent2_Student")

    # method for agent group chat
    team= RoundRobinGroupChat(participants=[user_proxy,Agent1],
                              termination_condition=TextMentionTermination("Lesson Complete"))

    # to start chat
    team.run_stream(task="What is 2*5, how it works")

    # to print the log
    await Console(team.run_stream(task="What is 2*5, how it works"))

    # agents will keep on talking indefinetely- so need to give a terminate condition

    # 1. maximum message termination= give a stop param for roundrobin
    ## termination_condition=MaxMessageTermination(max_messages=6))

    # 2. text termination
    ## termination_condition=TextMentionTermination("Lesson Complete"))


    await openai_model_client.close()

asyncio.run(main1())