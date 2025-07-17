# Python सीखने की गाइड / Python Learning Guide

## Python क्या है? / What is Python?

Python एक आसान और शक्तिशाली प्रोग्रामिंग भाषा है जो beginners के लिए perfect है।
Python is an easy and powerful programming language that's perfect for beginners.

## Python सीखने के फायदे / Benefits of Learning Python:

1. **आसान syntax** - Easy to read and write
2. **Versatile** - Web development, data science, AI, automation
3. **High demand** - Job opportunities में बहुत demand है
4. **Large community** - Help और resources आसानी से मिलते हैं

## Chapter 1: Python की शुरुआत / Getting Started

### Python Install करना / Installing Python
```bash
# Linux में Python usually pre-installed होता है
python3 --version

# अगर नहीं है तो install करें
sudo apt update
sudo apt install python3 python3-pip
```

### पहला Program / First Program
```python
# Hello World program
print("Hello, World!")
print("नमस्ते दुनिया!")
```

## Chapter 2: Variables और Data Types

### Variables
```python
# Variables बनाना
name = "राहुल"          # String
age = 25               # Integer  
height = 5.8           # Float
is_student = True      # Boolean

print(f"नाम: {name}")
print(f"उम्र: {age}")
print(f"लंबाई: {height}")
print(f"Student है: {is_student}")
```

### Data Types
```python
# Different data types
number = 42              # int
decimal = 3.14          # float
text = "Python सीखना है"  # string
is_true = False         # boolean
my_list = [1, 2, 3]     # list
my_dict = {"name": "अमित"} # dictionary
```

## Chapter 3: Input और Output

```python
# User से input लेना
name = input("अपना नाम बताइए: ")
age = int(input("अपनी उम्र बताइए: "))

print(f"हैलो {name}! आपकी उम्र {age} साल है।")

# Multiple inputs
print("आपका पसंदीदा रंग क्या है?")
color = input()
print(f"वाह! {color} बहुत अच्छा रंग है!")
```

## Chapter 4: Control Flow

### If-Else Statements
```python
age = int(input("अपनी उम्र बताइए: "))

if age >= 18:
    print("आप vote कर सकते हैं!")
elif age >= 16:
    print("आप driving license के लिए apply कर सकते हैं!")
else:
    print("आप अभी भी बच्चे हैं!")

# Grade calculator
marks = int(input("अपने marks बताइए: "))

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

print(f"आपका grade: {grade}")
```

### Loops

#### For Loop
```python
# Numbers print करना
print("1 से 10 तक के numbers:")
for i in range(1, 11):
    print(i)

# List के साथ loop
fruits = ["आम", "केला", "सेब", "संतरा"]
print("\nफलों की list:")
for fruit in fruits:
    print(f"मुझे {fruit} पसंद है")

# Table बनाना
number = int(input("किस number का table चाहिए? "))
print(f"\n{number} का table:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

#### While Loop
```python
# Counting game
count = 1
print("1 से 5 तक counting:")
while count <= 5:
    print(count)
    count += 1

# Guessing game
import random
secret_number = random.randint(1, 10)
guess = 0

print("1 से 10 के बीच एक number guess करिए!")
while guess != secret_number:
    guess = int(input("अपना guess बताइए: "))
    if guess < secret_number:
        print("ज्यादा बड़ा number try करिए!")
    elif guess > secret_number:
        print("छोटा number try करिए!")
    else:
        print("बधाई हो! आपने सही guess किया!")
```

## Chapter 5: Functions

```python
# Simple function
def greet(name):
    return f"नमस्ते {name}!"

# Function call करना
message = greet("प्रिया")
print(message)

# Calculator function
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2 if num2 != 0 else "Zero से divide नहीं कर सकते!"

# Calculator use करना
a = float(input("पहला number: "))
b = float(input("दूसरा number: "))
op = input("Operation (+, -, *, /): ")

result = calculator(a, b, op)
print(f"Result: {result}")

# Advanced function with default values
def introduce(name, age, city="दिल्ली"):
    print(f"मेरा नाम {name} है")
    print(f"मैं {age} साल का हूँ")
    print(f"मैं {city} में रहता हूँ")

introduce("राज", 22)
introduce("सुमित्रा", 28, "मुंबई")
```

## Chapter 6: Lists और Dictionaries

### Lists
```python
# List बनाना और use करना
fruits = ["आम", "केला", "सेब"]
print("Fruits:", fruits)

# List में add करना
fruits.append("अंगूर")
fruits.insert(1, "संतरा")
print("Updated fruits:", fruits)

# List से remove करना
fruits.remove("केला")
print("After removing केला:", fruits)

# List operations
numbers = [1, 2, 3, 4, 5]
print(f"Total: {sum(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Length: {len(numbers)}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)
```

### Dictionaries
```python
# Dictionary बनाना
student = {
    "name": "अनिल",
    "age": 20,
    "subjects": ["Math", "Science", "English"],
    "grade": "A"
}

print(f"Student का नाम: {student['name']}")
print(f"उम्र: {student['age']}")

# Dictionary में add/update करना
student["city"] = "जयपुर"
student["age"] = 21

print("Updated student info:")
for key, value in student.items():
    print(f"{key}: {value}")

# Nested dictionary
school = {
    "class_10": {
        "students": 45,
        "teacher": "श्रीमती शर्मा"
    },
    "class_12": {
        "students": 38,
        "teacher": "श्री गुप्ता"
    }
}

print(f"Class 10 में {school['class_10']['students']} students हैं")
```

## Chapter 7: File Handling

```python
# File में write करना
with open("my_notes.txt", "w", encoding="utf-8") as file:
    file.write("Python सीखना बहुत मजेदार है!\n")
    file.write("मैं हर दिन कुछ नया सीखता हूँ।\n")

# File से read करना
with open("my_notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("File content:")
    print(content)

# Line by line read करना
with open("my_notes.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# JSON file handling
import json

data = {
    "name": "विकास",
    "hobbies": ["cricket", "music", "coding"],
    "age": 24
}

# JSON में save करना
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# JSON से load करना
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    print("Loaded data:", loaded_data)
```

## प्रैक्टिस Projects / Practice Projects

### Project 1: To-Do List
```python
todo_list = []

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Tasks देखें")
    print("2. Task add करें")
    print("3. Task complete करें")
    print("4. Exit")

def show_tasks():
    if not todo_list:
        print("कोई tasks नहीं हैं!")
    else:
        print("\nआपके Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("नया task enter करें: ")
    todo_list.append(task)
    print(f"'{task}' add कर दिया गया!")

def complete_task():
    show_tasks()
    if todo_list:
        try:
            task_num = int(input("कौन सा task complete किया? (number): "))
            completed_task = todo_list.pop(task_num - 1)
            print(f"'{completed_task}' complete किया गया!")
        except:
            print("Invalid number!")

# Main program
while True:
    show_menu()
    choice = input("अपनी choice enter करें: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("धन्यवाद!")
        break
    else:
        print("Invalid choice!")
```

### Project 2: Simple Calculator
```python
def calculator():
    print("=== CALCULATOR ===")
    print("Available operations: +, -, *, /, %, **")
    
    while True:
        try:
            num1 = float(input("पहला number enter करें: "))
            operation = input("Operation enter करें (+, -, *, /, %, **): ")
            num2 = float(input("दूसरा number enter करें: "))
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Zero से divide नहीं कर सकते!")
                    continue
            elif operation == "%":
                result = num1 % num2
            elif operation == "**":
                result = num1 ** num2
            else:
                print("Invalid operation!")
                continue
                
            print(f"Result: {num1} {operation} {num2} = {result}")
            
            again = input("फिर से calculate करना चाहते हैं? (y/n): ")
            if again.lower() != 'y':
                break
                
        except ValueError:
            print("Invalid input! Numbers enter करें।")

calculator()
```

## सीखने के Tips / Learning Tips

1. **Daily practice करें** - हर दिन कम से कम 30 मिनट coding करें
2. **Projects बनाएं** - Theory के साथ practical projects भी करें  
3. **Errors से डरें नहीं** - Errors से सीखना part of learning है
4. **Community join करें** - Python communities में participate करें
5. **Documentation पढ़ें** - Official Python docs बहुत helpful हैं

## Next Steps

1. **Advanced Topics**: OOP, Modules, Packages
2. **Web Development**: Django, Flask
3. **Data Science**: Pandas, NumPy, Matplotlib
4. **AI/ML**: TensorFlow, Scikit-learn
5. **Automation**: Selenium, Beautiful Soup

## Useful Resources

- Python.org - Official documentation
- W3Schools Python Tutorial
- Real Python
- Python Tutor (visualizer)
- Stack Overflow (for doubts)

---

**Remember**: Programming सीखना एक journey है। Patient रहें और regular practice करें। आप जरूर सफल होंगे! 🐍✨