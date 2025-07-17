# Day 1: Python Variables और Data Types
# आज हम सीखेंगे variables कैसे बनाते हैं

print("=== Python Variables सीखते हैं ===")

# 1. String Variables (Text के लिए)
name = "राहुल"
city = "मुंबई"
country = "भारत"

print(f"नाम: {name}")
print(f"शहर: {city}")
print(f"देश: {country}")

# 2. Integer Variables (पूर्ण संख्या के लिए)
age = 25
marks = 95
year = 2024

print(f"\nउम्र: {age} साल")
print(f"अंक: {marks}")
print(f"साल: {year}")

# 3. Float Variables (दशमलव संख्या के लिए)
height = 5.8
weight = 65.5
price = 299.99

print(f"\nकद: {height} फीट")
print(f"वजन: {weight} किलो")
print(f"कीमत: ₹{price}")

# 4. Boolean Variables (True/False के लिए)
is_student = True
is_working = False
has_license = True

print(f"\nक्या छात्र है: {is_student}")
print(f"क्या काम कर रहा है: {is_working}")
print(f"क्या लाइसेंस है: {has_license}")

# 5. Variable का type check करना
print(f"\n=== Variable Types ===")
print(f"name का type: {type(name)}")
print(f"age का type: {type(age)}")
print(f"height का type: {type(height)}")
print(f"is_student का type: {type(is_student)}")

# 6. Variables को बदलना
print(f"\n=== Variables को Update करना ===")
age = 26  # पहले 25 था, अब 26 है
print(f"नई उम्र: {age}")

# 7. Multiple variables एक साथ
a, b, c = 10, 20, 30
print(f"\na = {a}, b = {b}, c = {c}")

# 8. Same value multiple variables को
x = y = z = 100
print(f"x = {x}, y = {y}, z = {z}")

# Practice Exercise:
print(f"\n=== Practice Exercise ===")
print("अपनी जानकारी के साथ variables बनाएं:")

# आप यहाँ अपनी जानकारी भरें:
my_name = "आपका नाम यहाँ लिखें"
my_age = 0  # अपनी उम्र लिखें
my_city = "आपका शहर"
my_hobby = "आपका शौक"

print(f"मेरा नाम: {my_name}")
print(f"मेरी उम्र: {my_age}")
print(f"मेरा शहर: {my_city}")
print(f"मेरा शौक: {my_hobby}")

# Bonus: Input से variables बनाना
print(f"\n=== User Input ===")
# user_name = input("अपना नाम बताएं: ")
# user_age = int(input("अपनी उम्र बताएं: "))
# print(f"हैलो {user_name}! आप {user_age} साल के हैं।")

print("\n✅ Day 1 Complete! कल हम Operators सीखेंगे।")