# Question 1 = Modify your palindrome function
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

# Question 2 = After your first attempt, ask AI:
answer =
    I ask AI and it said that It crashes because integers don’t have .lower().

# Question 3 = Reflect on what AI added that you didn't consider initially.

answer = 

    After i ask AI i found out that the AI code was faster and the AI code was using continue instead of while loops and my code does not correctly normalize all Unicode case mappings. example
    "ß".lower()  # "ß"
    "ß".upper()  # "SS"
    So my code give wrong results for some international text, and it also Allocates a full copy of the string, meaning for every new strings it creates a new one and stores it after comparing it usually  this is not a problem but when the string is large it takes more space so the AI code was more better at avoiding hidden costs and also communicates clearly.
