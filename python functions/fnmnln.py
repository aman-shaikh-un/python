def formated_name(first_name,last_name,middle_name=""):
    if middle_name:
        str1=f"{first_name} {middle_name} {last_name}"
        return str1.title()
    else:
        str2=(f"{first_name} {last_name}")
        return str2.title()


teacher2=formated_name("adil","ali","kahan")
print(teacher2)
teacher=formated_name("sarah","shaikh")
print(teacher)
    
