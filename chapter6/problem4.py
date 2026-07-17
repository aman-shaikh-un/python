#problem 4: write a program to find wthether a username contains less than 10 charcater or not

a = input("enter your usrname")
if ( len(a) <= 10 ):
    print("your username contain less than 10 characters")
else:
    print("your username contains morw than 10 characters")
