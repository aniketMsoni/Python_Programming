a = int(input("Enter a : "));
b = int(input("Enter b : "));

mn = min(a, b);

while(True):
    if(a%mn == 0 and b%mn == 0):
        print("Hcf is : ", mn);
        break;
    mn = mn - 1;