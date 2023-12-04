import random
random_number = random.randint(0,2)

word_list = ["apple", "banana", "orange"]
word = word_list[random_number]

user_name = input("Enter your name: ")
print(f"Welcome {user_name}")
print("========================\n")
print("This is hangman, try to guess the word in less than 10 tries\n")

print("Guess the word:")