age=25
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
    
if age >= 15:
    print("You are a child.")
else:
    print("You are a teenager or older.")
if age >= 60:
    print("You are a senior citizen.")
else:
    print("You are not a senior citizen.")
province="Balochistan"
if province == "Sindh" or province == "Punjab":
    print("You are from Balochistan.")
else:
    print("You are not from Balochistan.")
is_raining = False
if not is_raining:
    print("You don't go outside because it is raining.")
    
    grade="A"
    
    if grade == "A":
        print("Excellent")
    elif grade == "B":
        print("Good")
    elif grade == "C":
        print("Average")
    else:
        print("Needs Improvement")



weight=50
height=1.98
bmi=weight/(height**2)
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normal weight")
elif bmi >= 25 and bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obese")
else:
    print("Invalid BMI value")
        