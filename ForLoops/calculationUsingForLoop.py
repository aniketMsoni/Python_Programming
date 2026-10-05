calculations_to_units = 24
nameOfUnits = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculations_to_units} {nameOfUnits}"

def validate_and_execute():
    try:
        userInputNumber = int(num_of_days_element)
        if userInputNumber > 0:
            calculated_value = days_to_units(userInputNumber)
            print(calculated_value)
        elif userInputNumber == 0:
            print("You entered a 0")
        else:
            print("You entered a negative number")

    except ValueError:
        print("Your input is not a valid number")

user_input = ""
while user_input != "exit":
    userInput = input("Enter a number: ")
    for num_of_days_element in user_input:
        validate_and_execute()
