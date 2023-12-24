# src/main.py
from uagents import Bureau
from agents.temperature_alert_agent import temperature_alert_agent

temperature_alert_bureau = Bureau()
temperature_alert_bureau.add(temperature_alert_agent)

if __name__ == "__main__":
    temperature_alert_bureau.run()
