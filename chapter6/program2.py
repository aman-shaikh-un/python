a = int(input("enter your age"))

if ( a > 18):
    print("you are eligible")
elif (a == 18):
    print("let this year get complete and grown up")
elif (a == 0):
    print("please provide right info")
elif( a < 0):
    print("negative age ? ( doesn't get accepted here)")
else:
    print("wait and try again when you are over 18")
print("Successfully submited details")
