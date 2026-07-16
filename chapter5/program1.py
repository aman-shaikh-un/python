#dictionary and sets
#dictionary
marks = {
    #keys and values
    "Aman":100,
    "Kaif":90,
    "Khushi":80,
    "list":[1,2,3,4,5]
    }
print(marks["list"]) #lookup
print(marks.items()) #give output as touple
print(marks.keys()) #keys
marks.update({"Khushi":98}) #add and update
print(marks)
prints(marks.get("Aman"))
