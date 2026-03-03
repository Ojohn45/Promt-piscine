# Step 1 - Do it yourself
# Question 1: Write pseudocode for a function that checks if a string is a palindrome.

    answer = 
    
    so we start by checking if the words are palindrome. A palindrome is a word that when you read it either from the front or you read it backwords it is still be the same. so if it checks and find out the word is a palindrome it will return true and if it is not it will return false, meaning this is not a palindrome.

# Question 2: Implement your solution in Python.
<<<<<<< HEAD
    answer = 
    # defining it as a palindrome(is_palindrome)
=======
    answer =
     
>>>>>>> refs/remotes/origin/main
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
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))

# Step 2 - Use AI to learn
# Question = Now that your function works, use AI to go deeper:
answer =

#   What's the time complexity?
    Time Complexity = O(n).

#   What edge cases might I miss?
    i found out that my code can not accept a palindrome with spaces and puctuations. 

#   Are there better approaches?"
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
with this code it can handle spaces, puctuations, and upper/lower cases

# Step 3 - Reflection
* What did you learn from solving it before asking AI?

 answer =

    well i learned that my code checks and compares each character including spaces and punctuations and that makes it to not give a correct answer even when the word is a palindrome but when i use AI i saw a better way that make it ignore spaces and punctuation, and compare letters and numbers only

* How is your understanding different now?

answer = 
 
    I learned that if i am dealing with palindrome or any other questions i should watch out for edge case

* Could you now write similar functions (e.g., reverse a string) without help?

answer = 

    I think i can
