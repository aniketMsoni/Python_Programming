N = int(input("Enter no of testcases : "))

while N > 0:
    num = int(input("Enter a number: "))
    n = num
    count = int(0)

    while n > 0:
        count = count + 1
        n = n // 10

    result = 0
    x = num
    while num > 0:
        ld = num % 10
        result = result + pow(ld, count)
        num = num // 10

    if result == x:
        print("Number is a armstrong number")
    else:
        print("Number is not a armstrong number")
    N = N - 1