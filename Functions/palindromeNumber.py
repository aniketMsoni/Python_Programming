num = int(input("Enter no of testcases : \n"))

def isPalindrome(n):
    temp = n
    reverse = 0
    while n > 0:
        ld = n % 10
        reverse *= 10
        reverse += ld
        n = n // 10 # floor division so no float division happens
    return reverse == temp

for i in range(1, num+1):
    x = int(input("Ente a number: "))
    if isPalindrome(x):
        print(f"{x} is a palindrome")
    else:
        print(f"{x} is not a palindrome")

