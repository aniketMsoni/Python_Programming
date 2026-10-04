from Functions.scopeUsage import x

calculations = 10 # global

def show():
    calculations = 10 # local
    print(calculations)

show()
print(x)