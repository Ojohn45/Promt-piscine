# Objective: Combine multiple prompts to simulate a tool-using agent.

# Question1 = Step 1 prompt: Ask for a user’s query (e.g., “What’s the temperature in Paris?”).
answer = 
    Promt = What’s the temperature in Paris?

    model output =
        Right now in Paris, the temperature is about 16 °C (60 °F) with cloudy conditions — and forecasts show highs around 17–19 °C over the next couple of days, so it’s generally mild and not too hot or col

# Question2 = Step 2 prompt: Simulate a call to the weather API.
answer =
    Promt = Simulate a call to the weather API.

    model output =
        Request (what your app sends):

GET https://api.weather.com/current?city=Paris&units=metric

# Simulated API Response

{
  "location": "Paris",
  "temperature_celsius": 17,
  "condition": "Partly Cloudy",
  "humidity": 72,
  "wind_speed_kph": 14
}
#       What’s Happening Here
        The request asks for Paris weather in metric units.

        The response returns structured JSON data.

        Fields are consistent and properly typed:   

# Queston3 = Step 3 prompt: Format the final answer back to the user.
answer =
    Final answer =
        {
  "location": "Paris",
  "temperature_celsius": 17,
  "condition": "Partly Cloudy",
  "humidity": 72,
  "wind_speed_kph": 14
}

    That’s the properly formatted JSON response the user would receive from the system after the API call.

# Question4 = Document the chained process and outputs.
answer =
    So basicly the user asked, what is the weather in paris. After that the system build the API call which is this:
    GET https://api.weather.com/current?city=Paris&units=metric
    and stuctured API response in JSON:
    {
  "location": "Paris",
  "temperature_celsius": 17,
  "condition": "Partly Cloudy",
  "humidity": 72,
  "wind_speed_kph": 14
}

        So the full chain is: User → Intent Detection → API Call → API Response → Schema Validation → Final Output