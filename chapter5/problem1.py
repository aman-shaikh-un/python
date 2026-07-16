#write a program to create a dictionary of hindi words with value as thier
#translation provide user with an option to look it up

words = { "pani":"water",
          "kursi":"chair",
          "phanka":"fan"}
a=input("enter word in hindi and get english translation")
print(words.get(a))
