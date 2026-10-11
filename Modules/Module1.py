from Module2 import validate_and_execute, userInputMessage

user_input = ""
while user_input != "exit":
    user_input = input(userInputMessage)
    daysAndUnits = user_input.split(":")
    days_and_units_dictionary = {"days" : daysAndUnits[0], "unit" : daysAndUnits[1]}
    validate_and_execute(days_and_units_dictionary)
