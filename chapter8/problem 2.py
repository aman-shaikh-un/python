def c_to_f(c):
    return (9 * c / 5) + 32

c = float(input("Enter temperature in Celsius: "))
f = c_to_f(c)

print("Temperature in Fahrenheit:", f)
