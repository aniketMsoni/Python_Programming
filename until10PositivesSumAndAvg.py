cnt = (int)(0);
sum = (int)(0);
total = (int)(0);
while ( cnt < 10):
    x = input();
    if(x > 0):
        cnt = cnt + 1;
    sum = sum + x;
    total = total + 1;

print("Sum : ", sum, "\n", "Average : ", sum /total );
