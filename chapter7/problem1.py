#problem 1: print multiplication table entered by the user
n = int(input("enter the table you want tp print"))
for i in range (1,11):
    print(f"{n} X {i} = ",n*i)
