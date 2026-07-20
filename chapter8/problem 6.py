def rem(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item)
    return n

l = ["aman", "garou", "krish"]
print(rem(l, "aman"))
