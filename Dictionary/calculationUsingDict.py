
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculations_to_units} {nameOfUnits}"

def validate_and_execute():
    try:
        userInputNumber = int()

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
    user_input = input("Enter number of days and units of conversion:\n")
    daysAndUnits = user_input.split(":")
    days_and_units_dictionary = {"days" : daysAndUnits[0], "unit" : daysAndUnits[1]}
    validate_and_execute()
