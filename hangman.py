import random
from wordlist import *

hangman_art = {0 : ("   ",
                    "   ",
                    "   "),
               1 : (" O ",
                    "   ",
                    "   "),
               2 : (" O ",
                    " | ",
                    "   "),
               3 : (" O ",
                    "/| ",
                    "   "),
               4 : (" O ",
                    "/|\\",
                    "   "),
               5 : (" O ",
                    "/|\\ ",
                    "/  "),
               6: (" O ",
                   "/|\\ ",
                   "/ \\")}

def display_hangman(wrong_guess):
    print("**********")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("".join(answer))

def main():
    while True:
        print("1. Play with animals name")
        print("2. Play with countries name")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            answer = random.choice(animals)
            break
        elif choice == 2:
            answer = random.choice(countries)
            break
        else:
            print("Invalid Choice, Try Again")

    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letters = set()
    is_running = True

    if " " in answer:
        for i in range(len(answer)):
            if answer [i] == " ":
                hint[i] = " "

    while is_running:
        display_hangman(wrong_guess)
        display_hint(hint)
        guess = input("Enter your letter: ").lower()

        if guess == answer:
            print("You won")
            is_running = False
        elif len(guess) != 1 or not guess.isalpha():
            print("Invalid! One Letter per round")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_guess += 1

        if guess in guessed_letters:
            print(f"your have already guess the letter {guess}")
            continue

        guessed_letters.add(guess)

        if "_" not in hint:
            display_hangman(wrong_guess)
            display_answer(answer)
            print("You win")
            is_running = False
        elif wrong_guess >= len(hangman_art) - 1:
            display_hangman(wrong_guess)
            display_answer(answer)
            print("You Lost")
            is_running = False

print("Thanks for playing")
if __name__ == '__main__':
    main()