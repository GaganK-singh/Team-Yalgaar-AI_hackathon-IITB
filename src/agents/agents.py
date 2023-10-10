from uagents import Agent, Context

agent1 = Agent(name="Gagan", seed="gagan recovery phrase")

@agent1.on_interval(period=3.0)
async def say_hello(ctx: Context):
    print("Gaggu")

if __name__ == "__main__":
    agent1.run()