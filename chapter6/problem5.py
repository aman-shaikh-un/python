#problem5 write a program which finds out whether a given name is present
#in a list or not

list=[ "aman", "kazuto","yume","miemie" ]
e=input("enter a name")
if ( e in list ):
    print("this username already exist")
else:
    print("username doesn't exist")
    
