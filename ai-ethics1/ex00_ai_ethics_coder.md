# Part A: The Critical Distinction
# QESTION 1
#    question = How have you used AI for coding so far?
    answer =
        Yes i have used AI for coding.
    
#   question = Do you ask AI for solutions before trying yourself?
    answer =
        No i try it my self before i ask AI.

#    question = Can you explain code you've submitted without AI's help?
    answer =
        Yes i can 

#   question = What would happen if AI was suddenly unavailable during an exam or interview?
    answer = 
        I will already prepered so i will not need AI in the exam orinterview.

# QUESTION 2
#    question =  Identify your current pattern: Which learner are you now? 
    answer = 
        Learner B: "AI is my learning amplifier"

# Part B: The Wrong Way vs. The Right Way

# Step 1
# question 1: Write pseudocode for a function that checks if a string is a palindrome.
answer =   
    so we start by checking if the words are palindrome. A palindrome is a word that when you read it either from the front or you read it backwords it is still be the same. so if it checks and find out the word is a palindrome it will return true and if it is not it will return fales, meaning this is not a palindrome.

# question 2: Implement your solution in Python.
answer = 
    def is_palindrome(word):
    # it changes the word to lowercase to make the check  case-insensitive
    word = word.lower()
    
    # It checks if the words are the same forwards and backwards
    if word == word[::-1]:
        return True
    else:
        return False


# Example usage
print(is_palindrome("racecar")) 

# Step 2: Strategic AI use After you have a working solution, ask AI:
answer =

#   1. What's the time complexity?
        Time Complexity = O(n).

#   2. What edge cases might I miss?
        I found out that my code can not accept a palindrome with spaces and puctuations. 

#   3. Better Alternatives 
def is_palindrome(word):
    word = word.lower()
    left = 0
    right = len(word) - 1
    
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    
    return True
With this code it can handle spaces, puctuations, and upper/lower cases
# trade-offs
answer =
    it handles a palindrome but it does not handle palindromes with spaces, and punctuation.
    
# Step 3
# question = What did you learn by struggling first?
 answer =
    well i learned that my code checks and compares each character including spacestuation and punctuations and that makes it to not give a correct answer even when the word is a palindrome but when i use AI i saw a beter way that make it ignore spaces and punctuation, and compare letters and numbers only.

# question = How is your understanding different than if you'd just asked for the solution?
answer = 
    I learned that if i am dealing with palindrome or any other questions i should watch out for edge case.

# question = Can you now implement similar functions (reverse a string, find duplicates) without AI?
answer = 
    I think i can.

# question = What mental model did you build?
answer = 
    I first try to understand each and every thing a question is saying before i go forward to answer the question.

# Part C: Testing Your Understanding
# question 1 = Modify your palindrome function
    answer =
    def is_palindrome(word):
    word = word.lower()
    left, right = 0, len(word) - 1

    while left < right:

        while left < right and not word[left].isalnum():
            left += 1

        while left < right and not word[right].isalnum():
            right -= 1

        if word[left] != word[right]:
            return False, (left, right)

        left += 1
        right -= 1

    return True, None

print(is_palindrome("A man a plan a canal Panama"))

# After Asking AI = 
#   Possible Edge Cases =
        is_palindrome("")

✔ Your function returns True, None — which is correct.
#   Improved version =
        def is_palindrome(word):
    if not isinstance(word, str):
        return False, None

    left, right = 0, len(word) - 1

    while left < right:

        while left < right and not word[left].isalnum():
            left += 1

        while left < right and not word[right].isalnum():
            right -= 1

        if word[left].lower() != word[right].lower():
            return False, (left, right)

        left += 1
        right -= 1

    return True, None

This imroved version andle non-string input, Minor optimization by avoiding full string copy.
 
# Part D: The Fairness Contract

I will use AI when:

    I have tried solving a problem myself.

    I need to understand why something works.

    I want to explore alternative approaches.

I will NOT use AI when:

    I haven't tried the problem on my own.

    I am completing an exam or assessment.

    I am still learning fundamental concepts.

I know I'm using AI fairly when:

    I can explain my code without AI's help.

    I could solve a similar problem independently.

    I feel more confident in my own understanding.

Sign and date your contract:
date: 10/2/2026
sign: odumu

# Part E: Real-World Scenario Analysis

# question = Interview: "Explain how you'd implement a caching system." If you always relied on AI, can you answer?
answer = 
   I will not be able to answer the question because i do not know how to design caching system there for as i do not know how to properly design a caching systems i will fail the interview

# question = Production bug at 2 AM: AI is unavailable. Can you debug code you don't fully understand?
answer = 
    yes i wil try and do it

# question = New tech with little documentation: If you never learned to read docs and experiment, what happens?
answer = 
    so i will start by documenting so that i will know the main popose of th library, and after that i will creat a small prototype and i will test run it and if they is going to be any need i will i will ask my peers about it.

# question = Write a paragraph: How does using AI fairly now prepare you for these scenarios?
answer =
    These day many people use AI to learn coding not that it is a bad thing but they become too adicted to AI and they do not think crititically or think hard about thier work or question, they will just give AI the question to think and answer their question with out them geting what their soppoose to do. So to use AI fairly you need to try and understand the question first and try doing it your self, and also try to explore alternative approches to your work doing so you will be self sufficient and you will be able to solve a similar problem independently and this will make you be prepered for real world challages like collaborating responsibly or ensuring fairness in projects . Doing it this way you will have a brighter future in the tech world.

# Part F: Building Irreplaceable Skills

# Skill:
* Problem Decomposition	
#    Description:
        * Breaking down problems logically
#            Rating:
        	    4/5	
#                    Improvement Plan:
                       * I will put in more work, more time, and more effort so that i will be confident in my self and if given any task any time i will be able to do it.

# Skill:
* Systems Thinking
#    Description:
        * Understanding how components interact
#            Rating:
        	    3/5
#                    Improvement Plan:
                        * I will push my self and think beyong and out side the box and not limiting my self, so that i can see the biger picture of things.

# Skill
* Critical Evaluation	
#    Description:
        * Knowing when code is wrong or inefficient
#        	Rating:
                3/5
#                    Improvement Plan:
                        * This were i will put more critical thinking in my work and i will carefully analyze, not just leaving thing as they are but puting more effort to know if a code is: 
                        * efficient
                        * secure and
                        * if there is any bug
                        not just trusting it blidly.

# Rating:	
* Debugging Mindset
#    Description:
	    * Investigating unexpected behavior
#        	Rating:
                4/5
#                    Improvement Plan:
                        * I will try and be confident in my self and do not panic when i see a bug and try to have a good eye to find the bug and also to be quick to under stand the problem.

# Skill: 	
Conceptual Understanding	
#    Description:
        Knowing WHY, not just HOW
#            Rating:
        	    4/5
#                    Impovement Plan:
                        As it says not just how but why so i will make sure i understand the core concept behind tmy work or code not just knowing how my code works or saying it works.

# Choose your lowest-rated skill and write 3 specific actions you'll take this week to improve it without relying on AI.
# Systems Thinking
* Improving my knowlege by studying more.
* I will learn how to see bugs quiker so that they will be no problem to beging with.
* I wil try and understand the thing work better