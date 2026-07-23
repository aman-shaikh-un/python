def person(first_name , last_name):
    full = f"{first_name} {last_name}"
    return full
while True:
    print("\n what's your name")
    f_l = input("enter your first name: ")
    l_l = input("enter your last name:" )
    #q = input("press q to quit: ")
    #if ( q == "q" ):
    break

formated = person( f_l , l_l )
print(f"{formated}")
