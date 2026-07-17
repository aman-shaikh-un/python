#problem3: A spam comment defined a text containing following keyowrs:
#Make  alot of money, buy now subcribe this click this write a program
#todetect the spams

a = "Make s lot of oney"
b = "buy now"
c = "subscribe me"
d = "click this"

message=input("comment here: ")

if ( a in message or b in message or c in message or d in message):
    print("your are a spammer: ")
else:
    print("your comment posted successfully ")
