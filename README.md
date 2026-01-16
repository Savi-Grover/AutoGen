**INSTALLATION:**

1. download python; path sett
2. download PyCharm ; path sett
3. check python and pip version in cmd
4. once in pycharm-> create new project(AutoGen)
5. make sure this new proj has .venv environment
6. open pycharm terminal -> path shud start from .venv
7. point interpreter type - to python address for path settings

**Official  docs- https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/installation.html**
1. Pycharm terminal > pip install -U "autogen-agentchat"
2. download model -by pip command > pip install "autogen-ext[openai]" ( brain of autoGen)

tools download- https://microsoft.github.io/autogen/stable//user-guide/extensions-user-guide/index.html
3.  pip install -U "autogen-ext[mcp]"

to check all 3 downloaded> go to proj settings> interpreter> look for autogen-agentChat, mcp, openai

-------------------------first program----------------------

1 every func in Autogen needs to be Async;
2 every async function needs to be invoked by using asyncio.run(func_name())


**------------------------make workflows-------------------------------**
1. single agent--> task assigned or asked to a single agent

2. multiagent --> agent 1-->talk to agent 2 and back and forth until termination condition met

3. human machin: or human in loop: agent1--> human ---> agent1
