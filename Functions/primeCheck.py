n = int(input("Enter total no of testcases :"))

def primeno(num):
    for i in range(2, int(num//2)+1):
        if num % i == 0:
            print("Not a prime number")
            return False
    return True


while n > 0:
    num = int(input("Enter a number :"))
    if num == 0 or num == 1:
        print("Neither prime nor composite")
    else:
        result = primeno(num)
        if result == True:
            print("A prime number")
    n = n - 1
