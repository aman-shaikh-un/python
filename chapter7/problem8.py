#problem 8


n = int(input("enter a number: "))
for i in range(1, n+1):
    print(" "* (n-1), end ="")
    print("*" * i, end="")
    print("")
