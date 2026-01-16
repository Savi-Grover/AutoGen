import asyncio

# every func in Autogen needs to be Async;
# every async function needs to be invoked by using asyncio.run(func_name())

async def main():
    print("function 1")



asyncio.run(main())