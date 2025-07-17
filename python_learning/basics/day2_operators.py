# Day 2: Python Operators
# आज हम सीखेंगे विभिन्न operators का उपयोग

print("=== Python Operators सीखते हैं ===")

# 1. Arithmetic Operators (गणितीय operators)
print("1. Arithmetic Operators:")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"जोड़ (Addition): {a} + {b} = {a + b}")
print(f"घटाव (Subtraction): {a} - {b} = {a - b}")
print(f"गुणा (Multiplication): {a} * {b} = {a * b}")
print(f"भाग (Division): {a} / {b} = {a / b}")
print(f"फ्लोर डिवीजन (Floor Division): {a} // {b} = {a // b}")
print(f"शेषफल (Modulus): {a} % {b} = {a % b}")
print(f"घात (Power): {a} ** {b} = {a ** b}")

# 2. Comparison Operators (तुलना operators)
print(f"\n2. Comparison Operators:")
x = 15
y = 20

print(f"x = {x}, y = {y}")
print(f"x == y (बराबर है?): {x == y}")
print(f"x != y (बराबर नहीं है?): {x != y}")
print(f"x < y (x छोटा है y से?): {x < y}")
print(f"x > y (x बड़ा है y से?): {x > y}")
print(f"x <= y (x छोटा या बराबर है?): {x <= y}")
print(f"x >= y (x बड़ा या बराबर है?): {x >= y}")

# 3. Logical Operators (तर्कसंगत operators)
print(f"\n3. Logical Operators:")
is_adult = True
has_id = False

print(f"is_adult = {is_adult}, has_id = {has_id}")
print(f"is_adult and has_id: {is_adult and has_id}")
print(f"is_adult or has_id: {is_adult or has_id}")
print(f"not is_adult: {not is_adult}")
print(f"not has_id: {not has_id}")

# 4. Assignment Operators (असाइनमेंट operators)
print(f"\n4. Assignment Operators:")
num = 10
print(f"शुरुआती num = {num}")

num += 5  # num = num + 5
print(f"num += 5 के बाद: {num}")

num -= 3  # num = num - 3
print(f"num -= 3 के बाद: {num}")

num *= 2  # num = num * 2
print(f"num *= 2 के बाद: {num}")

num /= 4  # num = num / 4
print(f"num /= 4 के बाद: {num}")

# 5. Practical Examples (व्यावहारिक उदाहरण)
print(f"\n=== Practical Examples ===")

# Example 1: Grade Calculator
marks = 85
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"अंक: {marks}, ग्रेड: {grade}")

# Example 2: Even/Odd Check
number = 17
if number % 2 == 0:
    result = "जोड़ (Even)"
else:
    result = "विषम (Odd)"
print(f"संख्या {number} है: {result}")

# Example 3: Age Category
age = 22
if age < 18:
    category = "बच्चा (Minor)"
elif age >= 18 and age < 60:
    category = "युवा (Adult)"
else:
    category = "वरिष्ठ (Senior)"
print(f"उम्र {age}: {category}")

# 6. Practice Exercises
print(f"\n=== Practice Exercises ===")

# Exercise 1: Simple Calculator
print("Exercise 1: Simple Calculator")
num1 = 25
num2 = 8
operation = "+"

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "गलत operation"

print(f"{num1} {operation} {num2} = {result}")

# Exercise 2: Temperature Check
print(f"\nExercise 2: Temperature Check")
temperature = 35
if temperature > 30:
    weather = "गर्म (Hot)"
elif temperature > 20:
    weather = "सामान्य (Normal)"
else:
    weather = "ठंडा (Cold)"
print(f"तापमान {temperature}°C: {weather}")

print(f"\n✅ Day 2 Complete! कल हम Control Structures सीखेंगे।")

# Challenge for you:
print(f"\n🎯 Challenge: अपने लिए एक BMI calculator बनाएं!")
print("BMI = weight(kg) / (height(m))^2")

# आप यहाँ code लिखें:
weight = 70  # अपना वजन किलो में
height = 1.75  # अपना कद मीटर में
bmi = weight / (height ** 2)
print(f"आपका BMI: {bmi:.2f}")

if bmi < 18.5:
    bmi_category = "कम वजन (Underweight)"
elif bmi < 25:
    bmi_category = "सामान्य (Normal)"
elif bmi < 30:
    bmi_category = "अधिक वजन (Overweight)"
else:
    bmi_category = "मोटापा (Obese)"

print(f"BMI Category: {bmi_category}")