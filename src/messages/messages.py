from uagents import Agent, Bureau, Context

agent2 = Agent(name="agent1", seed="name1 recovery phrase")


#Agent2 Receives message from agent1 in models.py, if temprature is not in range(given)
@agent2.on_interval() 
async def get_message(ctx: Context):
    ctx.logger.info(f"Received message from {sender}: {msg.text}")

