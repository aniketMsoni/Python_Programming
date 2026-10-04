calculations_to_units = 24
nameOfUnits = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculations_to_units} {nameOfUnits}"
    elif num_of_days == 0:
        return "you entered a 0"

def validate_and_execute():
    if userInput.isdigit():
        userInputNumber = int(userInput)
        calculated_value = days_to_units(userInputNumber)
        print(calculated_value)
    else:
        print("Your input is not a valid number")

userInput = input("Enter a number: ")
validate_and_execute()