my_dict = {
    "name" : "Rahul",
    "age" : 20,
    "course" : "Python"
}

print(my_dict.items())
print("\n")
for x, y in my_dict.items():
    print(x, end="->")
    print(y, end="\n")
