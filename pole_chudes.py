import random

words = ["barcelona", "liverpool", "shakhtar", "atletico", "dynamo", "tottenham", "juventus", "internazionale", "bayern"]
random_word = random.choice(words)
list_of_letters = list(random_word)
open_letters = {" "}

guesses = int(input("Set number of guesses: "))
counter = 0

while counter < guesses:

    user_input = input("Enter a word or a letter: ")

    if len(user_input) > 1:
        if user_input == random_word:
            print("Correct, you won!")
            quit()
        else:
            print("Wrong, keep trying!")
            counter += 1
            continue

    if user_input in list_of_letters:
        copy_rand_word = random_word
        open_letters.add(user_input)
        for i in list_of_letters:
            if i not in open_letters:
                copy_rand_word = copy_rand_word.replace(i, "*")
        
        print(copy_rand_word)
        counter += 1
        if copy_rand_word == random_word:
            print("Correct, you won!")
            quit()
                
    else:
        print("Wrong, keep trying!")
        counter += 1

print("You lost!")