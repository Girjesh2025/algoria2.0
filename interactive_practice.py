# Interactive Python Practice
# यह file user input के साथ practice करने के लिए है

print("🐍 Python Interactive Practice Session 🐍")
print("=" * 50)

# User Input Practice
print("\n=== Chapter 1: आपके बारे में जानकारी ===")
user_name = input("अपना नाम बताइए: ")
user_age = int(input("अपनी उम्र बताइए: "))
user_city = input("आप कहाँ रहते हैं? ")

print(f"\nनमस्ते {user_name}!")
print(f"आपकी उम्र {user_age} साल है और आप {user_city} में रहते हैं।")

if user_age >= 18:
    print("आप vote कर सकते हैं! 🗳️")
else:
    years_left = 18 - user_age
    print(f"Vote करने के लिए आपको {years_left} साल और इंतजार करना होगा।")

# Simple Calculator
print("\n=== Chapter 2: Calculator ===")
print("आइए एक simple calculator बनाते हैं!")

num1 = float(input("पहला number enter करें: "))
operation = input("कौन सा operation करना है? (+, -, *, /): ")
num2 = float(input("दूसरा number enter करें: "))

if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} × {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} ÷ {num2} = {result}")
    else:
        print("Error: Zero से divide नहीं कर सकते!")
else:
    print("Invalid operation!")

# Grade Calculator
print("\n=== Chapter 3: Grade Calculator ===")
subject_count = int(input("कितने subjects के marks enter करने हैं? "))
total_marks = 0

for i in range(subject_count):
    marks = float(input(f"Subject {i+1} के marks enter करें: "))
    total_marks += marks

average = total_marks / subject_count
print(f"\nकुल marks: {total_marks}")
print(f"Average: {average:.2f}")

if average >= 90:
    grade = "A+"
    comment = "बहुत बढ़िया! 🌟"
elif average >= 80:
    grade = "A"
    comment = "अच्छा performance! 👍"
elif average >= 70:
    grade = "B"
    comment = "ठीक है, और मेहनत करें! 💪"
elif average >= 60:
    grade = "C"
    comment = "Pass हो गए, लेकिन और improve करना होगा! 📚"
else:
    grade = "F"
    comment = "ज्यादा मेहनत की जरूरत है! 📖"

print(f"आपका Grade: {grade}")
print(comment)

# Number Guessing Game
print("\n=== Chapter 4: Number Guessing Game ===")
import random

secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 5

print("मैंने 1 से 20 के बीच एक number सोचा है!")
print(f"आपके पास {max_attempts} attempts हैं।")

while attempts < max_attempts:
    guess = int(input(f"\nAttempt {attempts + 1}: अपना guess enter करें: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"🎉 बधाई हो! आपने सही guess किया!")
        print(f"Answer था: {secret_number}")
        print(f"आपने {attempts} attempts में guess किया!")
        break
    elif guess < secret_number:
        print("ज्यादा बड़ा number try करें! ⬆️")
    else:
        print("छोटा number try करें! ⬇️")
    
    if attempts == max_attempts:
        print(f"\n😔 Game Over! सही answer था: {secret_number}")

# List Practice
print("\n=== Chapter 5: Shopping List ===")
shopping_list = []

print("अपनी shopping list बनाइए!")
print("(Exit करने के लिए 'done' type करें)")

while True:
    item = input("कौन सी चीज़ shopping list में add करनी है? ")
    if item.lower() == 'done':
        break
    shopping_list.append(item)
    print(f"'{item}' list में add कर दिया गया!")

print(f"\n📝 आपकी Shopping List:")
if shopping_list:
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")
    print(f"\nकुल items: {len(shopping_list)}")
else:
    print("आपकी list empty है!")

# Password Strength Checker
print("\n=== Chapter 6: Password Strength Checker ===")
password = input("अपना password enter करें: ")

strength_score = 0
feedback = []

if len(password) >= 8:
    strength_score += 1
else:
    feedback.append("कम से कम 8 characters होने चाहिए")

if any(c.isupper() for c in password):
    strength_score += 1
else:
    feedback.append("कम से कम एक uppercase letter होना चाहिए")

if any(c.islower() for c in password):
    strength_score += 1
else:
    feedback.append("कम से कम एक lowercase letter होना चाहिए")

if any(c.isdigit() for c in password):
    strength_score += 1
else:
    feedback.append("कम से कम एक number होना चाहिए")

special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
if any(c in special_chars for c in password):
    strength_score += 1
else:
    feedback.append("कम से कम एक special character होना चाहिए")

print(f"\nPassword Strength Score: {strength_score}/5")

if strength_score == 5:
    print("🔒 बहुत strong password! Perfect!")
elif strength_score >= 3:
    print("🔓 Okay password, लेकिन और improve कर सकते हैं")
else:
    print("❌ Weak password! बेहतर बनाइए")

if feedback:
    print("\nImprovement suggestions:")
    for suggestion in feedback:
        print(f"• {suggestion}")

print("\n" + "=" * 50)
print("🎊 Interactive Practice Complete! 🎊")
print("अब आप Python के basic concepts समझ गए हैं!")
print("अगले step के लिए projects.py file check करें!")