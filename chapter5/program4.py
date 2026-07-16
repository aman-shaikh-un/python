s = {1,2,34,54,3,"Aman"}
print(s)
s.add("bytesbyaman")
print(s)
print( s, type(s))
print(len(s))
s.remove("Aman")
print(s)
s.pop()
print(s)
s.clear()
print(s)


s1={12,34,5,67}
s2={23,45,67}
print(s1.union(s2)) #merges 2 sets
print(s1.intersection(s2)) #print same element from both sets
