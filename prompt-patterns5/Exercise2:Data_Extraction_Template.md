# Objective: Extract structured data from unstructured input.

# Question1 = Choose an unstructured text (e.g., "John Doe, age 29, lives in Paris and works as a software engineer.").
answer =
    Faith Adokole, age 29, lives in Abuja and works as a software engineer.
# Question2 = Create a template prompt:
answer = 
    JSON format.
    {
  "Name": "Faith Adokole",
  "Age": 29,
  "Location": "Abuja",
  "Occupation": "Software Engineer"
}

# Question3 = Validate the output and ensure consistency across multiple inputs.
answer = 
    So after validation i found out that all the fiels are presented properly and the values matches the text and there are in proper JSON format.