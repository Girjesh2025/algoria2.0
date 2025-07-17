#!/usr/bin/env python3
# Daily Python Practice - रोज़ाना अभ्यास

print("🐍 Python Daily Practice Challenge! 🐍")
print("=" * 50)

import random
import datetime

# Today's Challenge Generator
challenges = [
    {
        "title": "Calculator Challenge",
        "description": "दो संख्याओं के साथ सभी arithmetic operations करें",
        "hint": "a = 15, b = 4 का उपयोग करें"
    },
    {
        "title": "Age Group Classifier",
        "description": "उम्र के आधार पर category बताएं (Child, Teen, Adult, Senior)",
        "hint": "if-elif-else का उपयोग करें"
    },
    {
        "title": "Grade Calculator",
        "description": "marks के आधार पर grade calculate करें",
        "hint": "90+ = A+, 80+ = A, 70+ = B, 60+ = C, <60 = F"
    },
    {
        "title": "Even/Odd Numbers",
        "description": "1 से 20 तक सभी even और odd numbers print करें",
        "hint": "for loop और % operator का उपयोग करें"
    },
    {
        "title": "String Manipulation",
        "description": "अपना नाम uppercase, lowercase, और title case में print करें",
        "hint": ".upper(), .lower(), .title() methods का उपयोग करें"
    }
]

# Pick today's challenge
today_challenge = random.choice(challenges)

print(f"📅 आज की Date: {datetime.date.today()}")
print(f"🎯 आज का Challenge: {today_challenge['title']}")
print(f"📝 Task: {today_challenge['description']}")
print(f"💡 Hint: {today_challenge['hint']}")
print("=" * 50)

# Practice Area - यहाँ अपना code लिखें
print("\n💻 Practice Area (यहाँ अपना code लिखें):")
print("# " + "="*48)

# Example Solutions (आप इन्हें देखने से पहले खुद try करें!)

print("\n🔐 Solutions (पहले खुद try करें!):")
print("# Uncomment करके solutions देखें:")

# Solution 1: Calculator
print("\n# Solution 1: Calculator")
print("""
# a = 15
# b = 4
# print(f"Addition: {a} + {b} = {a + b}")
# print(f"Subtraction: {a} - {b} = {a - b}")
# print(f"Multiplication: {a} * {b} = {a * b}")
# print(f"Division: {a} / {b} = {a / b}")
# print(f"Modulus: {a} % {b} = {a % b}")
# print(f"Power: {a} ** {b} = {a ** b}")
""")

# Solution 2: Age Group
print("# Solution 2: Age Group Classifier")
print("""
# age = 25
# if age < 13:
#     category = "Child (बच्चा)"
# elif age < 20:
#     category = "Teen (किशोर)"
# elif age < 60:
#     category = "Adult (युवा)"
# else:
#     category = "Senior (वरिष्ठ)"
# print(f"Age {age}: {category}")
""")

# Solution 3: Grade Calculator
print("# Solution 3: Grade Calculator")
print("""
# marks = 85
# if marks >= 90:
#     grade = "A+"
# elif marks >= 80:
#     grade = "A"
# elif marks >= 70:
#     grade = "B"
# elif marks >= 60:
#     grade = "C"
# else:
#     grade = "F"
# print(f"Marks: {marks}, Grade: {grade}")
""")

# Quick Practice Tests
print("\n🧪 Quick Tests (अपना knowledge test करें):")

# Test 1
print("Test 1: क्या output होगा?")
print("x = 10")
print("y = 3")
print("print(x // y)")
print("Answer: 3 (Floor division)")

# Test 2
print("\nTest 2: क्या output होगा?")
print("name = 'python'")
print("print(name.upper())")
print("Answer: PYTHON")

# Test 3
print("\nTest 3: क्या output होगा?")
print("a = 5")
print("print(a > 3 and a < 10)")
print("Answer: True")

# Daily Progress Tracker
print("\n📊 Progress Tracker:")
print("Day 1: Variables ✅")
print("Day 2: Operators ✅")
print("Day 3: Control Structures ⏳")
print("Day 4: Loops ⏳")
print("Day 5: Functions ⏳")

print("\n💪 Keep Learning! Python Master बनने के लिए daily practice करें!")
print("🎯 कल का लक्ष्य: Control Structures (if-else, loops)")