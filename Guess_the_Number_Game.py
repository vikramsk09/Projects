import random

correct_num = random.randint(1, 10)
total_attempts = 3
print(f"***You have only {total_attempts} attempts to play this game.***\n")

while True:

    if total_attempts == 0:
        print("\nSorry, you lose !!")
        print(f"The correct number was '{correct_num}'")
        break

    number = input("Enter a number between 1-10: ")

    if number.isalpha():
        print("Please type a number.\n")


    elif int(number) == correct_num:
        print("\nCongratulations!, you got the correct number.")
        print(f"The correct number was '{correct_num}'")
        break

    elif int(number) > correct_num:
        print("Please choose a lower number\n")
        total_attempts -= 1
        print(f"***Total {total_attempts} attempts left***")

    elif int(number) < correct_num:
        print("Please choose a higher number\n")
        total_attempts -= 1
        print(f"***Total {total_attempts} attempts left***")














































































































