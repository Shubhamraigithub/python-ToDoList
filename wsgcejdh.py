# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def count_character_frequency(text, character):
    frequency = 0
    for char in text:
        if char == character:
            frequency += 1
    return frequency

text = input("Enter the text: ")
character = input("Enter the character to count: ")

if len(character) == 1:
    frequency = count_character_frequency(text, character)
    print(f"Frequency of '{character}' in the text: {frequency}")
else:
    print("Please enter a single character to count its frequency.")
