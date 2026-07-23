''' Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.'''

def make_album(artist_name , album_title , number_of_song=None):
    ar = { "artist name": artist_name , "album title": album_title} #"number of song": number_of_song }
    if number_of_song:
        ar ['number_of_song'] = number_of_song
    return ar

singer = make_album("Aman","Chronicles of Amane", "1")
print(singer)
