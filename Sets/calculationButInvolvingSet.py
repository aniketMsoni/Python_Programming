calculations_to_units = 24
nameOfUnits = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculations_to_units} {nameOfUnits}"

def validate_and_execute():
    try:
        userInputNumber = int(num_of_days_element)

        # Conversion usi time hoga jab input is positive integers
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
    user_input = input("Enter a number: ")
    list_of_days = user_input.split()
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()
