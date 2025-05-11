import random
import time

number = random.randint(1, 100)
attempts = 5

print("Welcome to the number guessing game.")
time.sleep(0.5)
print(f"You have {attempts} attempts to guess the number between 1 and 100.")
time.sleep(0.5)
while attempts > 0:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == number:
        print("congratulations, you got it right.")
        time.sleep(2)
        repeat = input("Do you wanna play again?")
        if repeat.lower() in ["yes", "y"]:
            number = random.randint(1, 100)
            attempts = 5
            print("\nA new game started. Guess the number between 1 and 100.\n")
            continue
        else:
            break

    attempts -= 1

    if attempts == 0:
        print(f"sorry, out of attempts. the number was {number}.")
        time.sleep(2)
        repeat = input("Do you wanna play again?")
        if repeat.lower() in ["yes", "y"]:
            number = random.randint(1, 100)
            attempts = 5
            print("\nA new game started. Guess the number between 1 and 100.\n")
            continue
        else:
            break

  #  hint = "too low" if guess < number else "too high" guess>number else "almost there" guess+-=number
  #  time.sleep(1)
   # print(f"{hint}, you have {attempts} attempt(s) left.")
  #  time.sleep(0.5)

    def hint():
        if abs(guess-number) <=2:
            return "almost there! you're very close."
        elif guess>number:
            return "too high"
        elif guess<number:
            return "too low"
    time.sleep(0.3)
    print(f"{hint()}, you have {attempts} attempt(s) left.")
