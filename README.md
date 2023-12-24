▪️ Team Name - **Yalgaar**

▪️ Project Name:-
  **Temperature Alert Agent**

▪️ Project Description:-

 **Documentation: Temperature Alert Agent**

---

### Introduction

The Temperature Alert Agent is a Python project built using Fetch.ai's uAgents library. It connects to a free weather API to fetch real-time temperatures for a specified location and sends alerts to users when the current temperature goes below the minimum or above the maximum threshold they've set.

### File Structure


project_directory
├── poetry.lock
├── pyproject.toml
├── README.md
└── src
    ├── agents
    │   ├── __init__.py
    │   └── temperature_alert_agent.py
    ├── uagents_temperature
    │   ├── __init__.py
    │   └── temperature_functions.py
    └── main.py

- **agents**: Contains the main Temperature Alert Agent implementation.
- **uagents_temperature**: Houses utility functions related to temperature fetching.
- **main.py**: Entry point for running the Temperature Alert Agent.

### Configuration

1. **.env File:**

   Create a `.env` file in the project directory with the following content:

   
   OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
   LOCATION=YourCity,YourCountryCode
   MIN_TEMPERATURE=20.0
   MAX_TEMPERATURE=30.0
   

   Replace `your_openweathermap_api_key` with your actual OpenWeatherMap API key.

### Dependencies

- Fetch.ai uAgents Library
- Requests Library
- Python Dotenv Library

### Setup

1. **Install Dependencies:**

   
   poetry install
   

2. **Run Temperature Alert Agent:**

   
   poetry run python src/agents/temperature_alert_agent.py
   

### Usage

1. **Agent Initialization:**

   The agent initializes with user configuration, including location and temperature thresholds.

2. **Temperature Fetching:**

   Every 2 seconds, the agent fetches the current temperature for the specified location using the OpenWeatherMap API.

3. **Alert Logic:**

   Every 5 seconds, the agent checks if the current temperature falls outside the user-defined range. If so, it triggers an alert/notification (simulated).

### Note

- The agent runs indefinitely, periodically checking the temperature and sending alerts.

---

**Run Guide:**

1. Clone the project repository:

   
   git clone <repository_url>
   cd <project_directory>
   

2. Create a virtual environment:

   
   poetry install
   

3. Create a `.env` file with your OpenWeatherMap API key and desired location:

   
   OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
   LOCATION=YourCity,YourCountryCode
   MIN_TEMPERATURE=20.0
   MAX_TEMPERATURE=30.0
   

4. Run the Temperature Alert Agent:

   
   poetry run python src/agents/temperature_alert_agent.py
   

   The agent will start fetching real-time temperatures and sending alerts based on the configured thresholds.

---

**Note:** Make sure to replace placeholders like `your_openweathermap_api_key` and `YourCity,YourCountryCode` with your actual values.
