word_without_vowels = ""

user_word = input("Enter a word: ").upper()

for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    word_without_vowels += letter
print(word_without_vowels)