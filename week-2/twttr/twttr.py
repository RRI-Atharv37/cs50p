# remove vowels

CONSONANTS = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
words = input("Input: ")
print("Output: ", end="")
for letter in words:
    if letter not in CONSONANTS:
        print(letter, end="")
        