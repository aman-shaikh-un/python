a = int(input("Enter your marks: "))

if a >= 90 and a <= 100:
    print("Grade O")
elif a >= 80 and a < 90:
    print("Grade A")
elif a >= 70 and a < 80:
    print("Grade B")
elif a >= 60 and a < 70:
    print("Grade C")
elif a >= 50 and a < 60:
    print("Grade D")
elif a < 50:
    print("Grade F")
else:
    print("Invalid marks! Marks should be between 0 and 100.")
