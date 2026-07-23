'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.'''


def album ( artist_name , album_title ):
    pr =f"{artist_name} {album_title}"
    return pr.title()
while True:
    print("enter artist name and album title")
    a_n = input("\n artist name: ")
    a_t = input("\n album title: ")
    break
singer=album(a_n,a_t)
print(singer)
        
