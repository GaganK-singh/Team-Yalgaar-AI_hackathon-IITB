# src/agents/temperature_alert_agent.py
from uagents import Agent, Context, Model
from uagents_temperature.temperature_functions import fetch_current_temperature

class TemperatureAlertConfig(Model):
    location: str
    min_temperature: float
    max_temperature: float

class TemperatureAlert(Model):
    location: str
    current_temperature: float

temperature_alert_agent = Agent(name="temperature_alert_agent")

@temperature_alert_agent.on_start()
async def initialize_agent(ctx: Context):
    # Load user configuration from storage or user input
    config = TemperatureAlertConfig(location="YourCity,YourCountryCode", min_temperature=20.0, max_temperature=30.0)
    ctx.store.put("temperature_alert_config", config)

@temperature_alert_agent.on_interval(period=2.0)
async def fetch_and_check_temperature(ctx: Context):
    config = ctx.store.get("temperature_alert_config")

    current_temperature = fetch_current_temperature(config.location)
    await ctx.send(ctx.address, TemperatureAlert(location=config.location, current_temperature=current_temperature))

@temperature_alert_agent.on_message(model=TemperatureAlert)
async def check_temperature_alert(ctx: Context, sender: str, msg: TemperatureAlert):
    config = ctx.store.get("temperature_alert_config")
    current_temperature = msg.current_temperature

    if current_temperature < config.min_temperature:
        ctx.logger.info(f"Temperature in {config.location} is below the minimum threshold! Alerting user.")
        # Send notification or alert to the user
    elif current_temperature > config.max_temperature:
        ctx.logger.info(f"Temperature in {config.location} is above the maximum threshold! Alerting user.")
        # Send notification or alert to the user
