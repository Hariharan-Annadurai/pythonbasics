c = int(input("Enter a number: "))
if c > 1:
    for i in range(2, c):
        if (c % i) == 0:
            print(c, "is not a prime number")
            break
    else:
        print(c, "is a prime number")
else:
    print(c, "is not a prime number")