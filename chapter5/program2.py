#get key sfaetly return none if key doesnot exist

user = {"name": "Aman", "age": 19 }
print(user.get("name"))
print(user.get("age"))
print(user.get("address"))

#retruns a view of all keys in dictionary

user1 = {"name":"Kaif" , "age":20}
print(user1.keys())
for key in user1.keys():
    print(key)
    
#returns a value of all members in dictionary
    
user2 = {"name":"Saitama" ,"age":90}
for value in user2.values():
    print(value)
    
#returns all items of the list
    
user3 = {"name":"Doraemon", "age":45}
print(user3.items())
for key, value in user3.items():
    print(f"{key},{value}")

#merge another dictionary into current one
    
user4={"name":"kazuto","age":67}
user4.update({"name":"kaso"})
user4.update({"location":"paris","fashion":"10/10"})
print(user4)

#removes a key an dits value safely
user5 = {"name":"fero" ,"age":67,
         "name":"yuri","age":45}
print(user5.pop("name")

#popitem
user = {"name":"aman" ,"age":90}
item = user.popitem()
print(item)
print(user)


#setdefault; returns a value of the key if it exists if not the key with the default
#value an dretunrs it
user = { "user":"aman","age":78}
user.setdefault("age", 30)
print(user.popitem)




