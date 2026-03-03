# Objective: Practice designing prompts that mimic function calls.

## Question1 = Create a prompt: “Simulate a weather API response for Paris today.”
answer =
    Promt = Simulate a weather API response for Paris today.

## Question2 = Define an expected JSON schema, e.g.:
answer =
    JSON Schema:
{
  "city": "Paris",
  "temperature_c": 12,
  "condition": "Cloudy",
  "humidity_percent": 68,
  "wind_kph": 18
}
## Question3 = Test the model with different cities and compare outputs.
answer = 
  Testing Model With Different Cties:
### PARIS
{
  "city": "Paris",
  "temperature_c": 12,
  "condition": "Cloudy",
  "humidity_percent": 68,
  "wind_kph": 18
}

### TOKYO
{
  "city": "Tokyo",
  "temperature_c": 16,
  "condition": "Sunny",
  "humidity_percent": 55,
  "wind_kph": 12
}

### NEW YORK
{
  "city": "New York",
  "temperature_c": 5,
  "condition": "Snow Showers",
  "humidity_percent": 75,
  "wind_kph": 22
}

### Comparing outputs
so we tested this tree cities Paris, New York, and Tokyo and fid out that the format Consistetly have these three outputs:
🔹Use the same JSON structure

🔹Contain identical fields (city, temperature_c, condition, humidity_percent, wind_kph)

🔹Use correct data types (strings and numbers)
So this shows schema consistency across inputs.