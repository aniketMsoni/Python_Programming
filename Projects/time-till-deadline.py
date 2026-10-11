import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":") # list contains both goal and deadline as a string

goal = input_list[0]
deadline = input_list[1]

# Converting string into date time format and Finding today's date
deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()

# Calculation
time_till = deadline_date - today_date

#printing the statement
# Very precised
print(f"Dear user! Time remaining for your goal : {goal} is {time_till}")
# In days -- not very precised
print(f"Dear user! Time remaining for your goal : {goal} is {time_till.days} days")
# In hours -- very precised
print(f"Dear user! Time remaining for your goal : {goal} is {time_till.total_seconds() / 60 / 60} hours")