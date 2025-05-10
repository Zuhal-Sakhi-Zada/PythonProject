import random
number = random.randint(1, 100)
guess = None
attempts = 5

print("Welcome to the number guessing game.")
print(f"You have {attempts} attempts to guess the number between 1 and 100.")

while attempts>0:
    try:
        guess= int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == number:
        print("congratulations, you got it right.")
        break

        attempts -= 1

    if attempts == 0:
         print(f"sorry, out of attempts. the number was {number}.")
         break

    hint = "too low" if guess<number else "too high"
    print(f"{hint}, you have {attempts} attempt(s) left.")
