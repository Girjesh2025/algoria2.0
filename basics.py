# Python Basics Practice File
# यह file Python के basic concepts को practice करने के लिए है

print("=== Python की शुरुआत ===")
print("नमस्ते! Python सीखने में आपका स्वागत है!")

# Variables और Data Types
print("\n=== Variables और Data Types ===")
name = "राहुल"
age = 25
height = 5.8
is_student = True

print(f"नाम: {name}")
print(f"उम्र: {age}")
print(f"लंबाई: {height} feet")
print(f"Student है: {is_student}")

# Basic Operations
print("\n=== Basic Math Operations ===")
a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} × {b} = {a * b}")
print(f"{a} ÷ {b} = {a / b}")
print(f"{a} का {b} से remainder = {a % b}")
print(f"{a} की power {b} = {a ** b}")

# Strings
print("\n=== String Operations ===")
first_name = "राम"
last_name = "शर्मा"
full_name = first_name + " " + last_name

print(f"पूरा नाम: {full_name}")
print(f"नाम की length: {len(full_name)}")
print(f"Uppercase में: {full_name.upper()}")
print(f"Lowercase में: {full_name.lower()}")

# Lists
print("\n=== Lists ===")
colors = ["लाल", "हरा", "नीला", "पीला"]
print(f"रंगों की list: {colors}")
print(f"पहला रंग: {colors[0]}")
print(f"आखिरी रंग: {colors[-1]}")

colors.append("गुलाबी")
print(f"नया रंग add करने के बाद: {colors}")

# Loops
print("\n=== For Loop Example ===")
print("1 से 5 तक counting:")
for i in range(1, 6):
    print(f"Number: {i}")

print("\nरंगों की list:")
for color in colors:
    print(f"मुझे {color} रंग पसंद है")

# If-Else
print("\n=== If-Else Example ===")
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

print(f"Marks: {marks}")
print(f"Grade: {grade}")

# Functions
print("\n=== Functions ===")

def greet_user(name):
    return f"नमस्ते {name}! आपका दिन शुभ हो!"

def add_numbers(x, y):
    return x + y

# Function calls
greeting = greet_user("प्रिया")
print(greeting)

result = add_numbers(15, 25)
print(f"15 + 25 = {result}")

# Dictionary
print("\n=== Dictionary Example ===")
student = {
    "name": "अमित",
    "age": 20,
    "subjects": ["Math", "Science", "English"],
    "grade": "A"
}

print("Student की जानकारी:")
for key, value in student.items():
    print(f"{key}: {value}")

print("\n=== Practice Complete! ===")
print("अब आप इन concepts को अच्छी तरह समझ गए हैं।")
print("अगले step के लिए interactive_practice.py file run करें!")