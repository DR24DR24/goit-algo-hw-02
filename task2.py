from collections import deque

def is_palindrome(s: str) -> bool:
    # Перетворення рядка в нижній регістр і видалення пробілів
    s = ''.join(filter(str.isalnum, s)).lower()

    # Створення двосторонньої черги і додавання символів рядка
    char_deque = deque(s)

    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Приклади використання функції
test_strings = [
    "A man a plan a canal Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw",
    "No lemon no melon"
]

for test in test_strings:
    print(f"'{test}' is palindrome: {is_palindrome(test)}")
    