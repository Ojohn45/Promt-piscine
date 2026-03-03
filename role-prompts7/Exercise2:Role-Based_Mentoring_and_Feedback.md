# Objective: Use role-based prompts for personalized feedback.

# Question1 = Ask the model to act as a coding mentor.
answer =
    Okay done that.

# Question2 = Provide a simple piece of code (e.g., a Python function with a bug).
answer = The code with the bug.
    def is_palindrome(word)
    word = word.lower()
    left, right = 0, len(word) - 1

    while left < right:

        while left < right and not word[left].isalnum():

        while left < right and not word[right].isalnum():

        if word[left] != word[right]:
            return False, (left, right)

        left += 1
        right -= 1

        return True, None
print(is_palindrome("A man a plan a canal Panama"))

# After asking AI:
answer = 
    The AI corrected the bug:
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

# Question3 = Prompt the model: "Act as a mentor reviewing this code. Provide corrections and explain improvements."
answer = 

    ✅ 1. Corrected Version (Fixed Errors)
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
🔧 Corrections Made
1️⃣ Added missing colon
def is_palindrome(word):

Python requires a colon after function definitions.

2️⃣ Fixed empty while loops

Originally:

while left < right and not word[left].isalnum():

There was no body inside the loop.

Now:

left += 1
right -= 1

This properly moves the pointers past non-alphanumeric characters.

3️⃣ Moved return True outside the loop

Before, it was inside the main while loop, which caused the function to stop too early.

Now it correctly returns True only after the loop fully finishes.

🚀 Improvements You Can Make

Now let’s level it up.

💡 Improvement 1: Cleaner Version (Simpler Approach)

You can simplify everything using string filtering:

def is_palindrome(word):
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned == cleaned[::-1]


print(is_palindrome("A man a plan a canal Panama"))
Why this is better:

Shorter

Easier to read

Still O(n) time complexity

More Pythonic

💡 Improvement 2: Better Return Style

Instead of returning:

return True, None

You could just return:

return True

Unless you specifically need the mismatch indexes.

Keep it simple unless required.

💡 Improvement 3: Add Type Safety

If this function is used in real applications, you could protect it:

def is_palindrome(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

That makes your function safer in larger systems.

# Question4 = Review the response and check if the role influences feedback style.
answer = 
    After doing this i saw that the AI was very helpfull. I mean after i gave it the buged code  it not only showed me the bug but also explain my code line by line cearfully and also pointed out the posibilities of why my code is like that, and gave me the correct code and thought me how to do it properly so i dont think they is any feedback.