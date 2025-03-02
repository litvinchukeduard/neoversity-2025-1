'''
Знайти чи слово є паліндром 

level
'''

def is_palindrome(text: str) -> bool:
    text = text.replace(',', '').replace(' ', '').replace('-', '').lower()
    return text[::-1] == text

# result = is_palindrome('level')
# if result:
#     print('Is okay')
# else:
#     print('Is not okay')

assert is_palindrome('level') == True
assert is_palindrome('hello') == False

assert is_palindrome("A man, a plan, a canal - Panama") == True


print('hello'[-4])
