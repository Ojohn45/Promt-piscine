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