import asyncio
import os

from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat, SelectorGroupChat
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
    Agent1= AssistantAgent(name="Researcher",model_client=openai_model_client,
                           system_message="You are aresearcher, don't write any articles, just gather facts and information")

    # create 2nd Agent
    Agent2= AssistantAgent(name="Writer", model_client=openai_model_client,
                           system_message="You are a Writer, take information from researcher and write article")

    # create 3rd Agent
    Agent3 = AssistantAgent(name="Critic", model_client=openai_model_client,
                            system_message="You are a Critic, review your writer's article"
                                           "say 'TERMINATE' when satisfactory reviews")

    # method for agent group chat- group chat will use its intelligence to decide order of agents
    team= SelectorGroupChat(participants=[Agent3,Agent2,Agent1],
                            model_client=openai_model_client,
                            allow_repeated_speaker=True,  #may have ag1 ag2 talking back to back
                            termination_condition=MaxMessageTermination(max_messages=6))

    # to start chat
    team.run_stream(task="Research on renewable energy trends")

    # to print the log
    await Console(team.run_stream(task="Research on renewable energy trends"))

    await openai_model_client.close()

asyncio.run(main1())