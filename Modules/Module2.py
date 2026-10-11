def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == 'hours':
        return f"{num_of_days} days are {num_of_days * 24} {"hours"}"
    elif conversion_unit == 'minutes':
        return f"{num_of_days} days are {num_of_days * 24 * 60} {"minutes"}"
    else:
        return "Unsupported unit"

def validate_and_execute(days_and_units_dictionary):
    try:
        userInputNumber = int(days_and_units_dictionary["days"])

        # Conversion usi time hoga jab input is positive integers
        if userInputNumber > 0:
            calculated_value = days_to_units(userInputNumber, days_and_units_dictionary["unit"])
            print(calculated_value)
        elif userInputNumber == 0:
            print("You entered a 0")
        else:
            print("You entered a negative number")

    except ValueError:
        print("Your input is not a valid number")

userInputMessage = "Enter number of days and units of conversion:\n"