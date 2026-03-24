# program to count vowels in a word
vowels = ['a','e','i','o','u','A','E','I','O','U']

word = input("Enter your word: ")

for letter in word:
    if letter in vowels:
        print(letter)