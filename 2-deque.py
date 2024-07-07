from collections import deque
import re

def is_palindrome(s):
    # Приведення рядка до нижнього регістру та видалення пробілів і неалфанумеричних символів, включаючи кирилицю
    a = s
    s = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', s).lower()
    # Створення двосторонньої черги
    char_deque = deque(s)
    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return f"Фраза |||{a}||| є паліндром? - Ні"
    return f"Фраза |||{a}||| є паліндром? - Так"

# Приклади використання функції
print(is_palindrome("дід Пилип піп Пилип дід"))  
print(is_palindrome("радар"))                     
print(is_palindrome("ротатор"))                      
print(is_palindrome("Привіт"))                     