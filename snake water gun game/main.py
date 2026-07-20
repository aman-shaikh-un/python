import random

computer = random.choice([-1,0,1])
youstr = input( "enter your choice: ")
youDict = {"s":1 ,"w":-1, "g":0}
reverseDict = {1: "Snake" , -1 : "Water" , 0: "Gun"}
you = youDict[youstr]

print(f"You choose {reverseDict[you]} \nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer ==-1 and you ==1):
        print("YOU WIN")

    elif(computer ==-1 and you ==0):
        print("YOU LOST")

    elif(computer ==1 and you ==-1):
        print("YOU LOST")

    elif(computer ==1 and you ==0):
        print("YOU WIN")

    elif(computer ==0 and you ==-1):
        print("YOU WIN")

    elif(computer ==0 and you ==1):
        print("YOU WIN")

    else:
        print("Something wnet wrong")
