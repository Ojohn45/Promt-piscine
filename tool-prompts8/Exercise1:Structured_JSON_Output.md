# Objective: Create prompts that produce structured machine-readable output.

# Question1 = Write a prompt that asks for unstructured information (e.g., “List three cities with their populations.”).
answer = 
    List three countries with one of their state each.
# Question2 = Rewrite the prompt to enforce structured JSON output:
answer =
    JSON Format:
    [
  {
    "country": "United States",
    "state": "California"
  },
  {
    "country": "Nigeria",
    "state": "Lagos State"
  },
  {
    "country": "India",
    "state": "Maharashtra"
  }
]
# Question = Test with multiple inputs and verify the JSON stays valid.
answer = 
#    multiple inputs =
1. 
[
  {
    "country": "United States",
    "state": "Texas"
  },
  {
    "country": "Canada",
    "state": "Ontario"
  },
  {
    "country": "Australia",
    "state": "Victoria"
  }
]

2. 
[
  {
    "country": "Nigeria",
    "state": "Kano State"
  },
  {
    "country": "India",
    "state": "Gujarat"
  },
  {
    "country": "Brazil",
    "state": "São Paulo"
  }
]

# Verifying =
    if all input stay start and end with [] it will bring out the output and inside that it should have {} and the keys are in double quotes " " to bring out the correct output.