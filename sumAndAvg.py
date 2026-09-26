n = int(input("Enter a number : "));

for i in range(1, n):
    arr = list(map(int , input().split()));

sum = 0;
for x in arr:
    sum += x;

print(sum);