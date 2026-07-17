#problem1: write a programt o find a greatest of 4 number entered by a user

a = int(input("enter no a "))
b = int(input("enter no b "))
c = int(input("enter no c "))
d = int(input("enter no d "))

if (a>b and a>c and a> d):
    print(" a is greater then b c and d ")
elif (b>a and b > c and b > d):
    print( "b is greater then a , c and d")
elif ( c > a and c > b and c > d):
    print(" c is greater then a , b , and d")
else:
    print( "d is greater then a , b and c")
