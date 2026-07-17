#problem2: write a program to find out whether a student has passed or failed
#if it requires a total of 40% and least 33% in each subject to pass assume
#3 subject and take marks as an input from the user


a = int(input("enter your mathematics marks: "))
b = int(input("enter your chemistry marks: "))
c = int(input("enter your physics marks out: "))
if a >= 33 and b >= 33 and c >=33:
    total_percentage = (a + b + c)/3
    if total_percentage >=40:
        print("Result Passed")
    else:
        print("result failed ( total percentage is less than 40%)")
else:
    print("result: failed ( One more subject less than 33%)")
