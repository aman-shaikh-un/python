'''8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"India, Delhi"
Call your function with at least three city-country pairs, and print the
values that are returned.'''

def city_country ( city , country ):
    c_c = f"{country}, {city}"
    return c_c.title()
while True:
    print("enter your country and city name here: ")
    f_c = input("enter country: ")
    s_c = input("enter city: ")
    break
countryandcity = city_country( f_c , s_c )
print(countryandcity)
    
