actual_number = 22
n = int(input("How many games would you like to play? "))
for i in range(n):
    entered_number = int(input("Please enter a random number between 1-25 "))
    if entered_number < actual_number:
        print(f"{entered_number} is lower!")
    elif entered_number > actual_number:
        print(f"{entered_number} is higher!")
    else:
        print("Correct!!!")
        print(f"You guessed in {i + 1} attempts")
        break
