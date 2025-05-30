from collections import deque

def is_palindrome(input_string):
    # Підготовка рядка: нижній регістр + видалення пробілів
    processed_string = input_string.lower().replace(" ", "")
    
    # Створення двосторонньої черги та додавання символів
    char_deque = deque(processed_string)
    
    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

# Приклади використання
test_strings = [
    "Привіт, світ!",
    "Мем",
    "Exam",
    "Я беру книгу",
    "1234321"
]

for s in test_strings:
    print(f"'{s}': {'Так' if is_palindrome(s) else 'Ні'}")