#usingr raw string is useful while printing os related commands
#imports os module
import os
#specied directory that i wanted to rpint
directory_path=r'D:\videos'
#prints list of directories names
contents = os.listdir(directory_path)
#print each file and driectory
for item in contents:
    print(item)
