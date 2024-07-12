def check_brackets(expression: str) -> str:
    # Відповідність відкритих і закритих розділювачів
    pairs = {')': '(', ']': '[', '}': '{'}
    # Стек для зберігання відкритих розділювачів
    stack = []

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"

# Приклади використання функції
test_expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for test in test_expressions:
    print(f"'{test}': {check_brackets(test)}")

