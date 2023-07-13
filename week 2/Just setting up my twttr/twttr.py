vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
user_input = input("Input: ")

for vowel in vowels:
    user_input = user_input.replace(vowel, "")

print(user_input)