# Prompt the user to enter a word and assign it to the user_word variable.
user_word = input("Enter a word: ").upper()  # Convert the word to uppercase

# Iterate through each letter in the word
for letter in user_word:
    # Check if the letter is a vowel
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue  # Skip the vowel and move to the next iteration
    # Print the uneaten letters, each on a separate line
    print(letter)
