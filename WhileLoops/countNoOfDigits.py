num = int(input("Enter a number: "))
cnt = 0

while num > 0:
    cnt += 1
    num = num // 10

print(cnt)