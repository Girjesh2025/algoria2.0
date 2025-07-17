#!/usr/bin/env python3
# Project 1: Number Guessing Game (संख्या अनुमान खेल)
# यह game Python basics practice करने के लिए है

import random

print("🎮 Number Guessing Game में आपका स्वागत है! 🎮")
print("=" * 50)

# Game Instructions
print("📋 Game Rules:")
print("1. मैं 1 से 100 के बीच एक संख्या सोचूंगा")
print("2. आप को उस संख्या का अनुमान लगाना है")
print("3. मैं बताऊंगा कि आपका अनुमान सही है या गलत")
print("4. अगर गलत है तो बताऊंगा कि बड़ी या छोटी संख्या की जरूरत है")
print("5. आप जितनी कम tries में अनुमान लगा लेंगे, उतना अच्छा!")
print("=" * 50)

# Game Setup
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7
game_over = False

print(f"🎯 मैंने 1 से 100 के बीच एक संख्या सोची है!")
print(f"📊 आपके पास {max_attempts} tries हैं।")
print("🚀 चलिए शुरू करते हैं!\n")

# Main Game Loop
while not game_over and attempts < max_attempts:
    try:
        # Get user input
        guess = int(input(f"Try {attempts + 1}/{max_attempts}: अपना अनुमान बताएं (1-100): "))
        attempts += 1
        
        # Check if guess is in valid range
        if guess < 1 or guess > 100:
            print("❌ कृपया 1 से 100 के बीच संख्या बताएं!")
            attempts -= 1  # Don't count invalid attempts
            continue
        
        # Check the guess
        if guess == secret_number:
            print(f"🎉 बधाई हो! आपने सही अनुमान लगाया!")
            print(f"✅ सही संख्या: {secret_number}")
            print(f"📊 आपने {attempts} tries में जीता!")
            
            # Performance feedback
            if attempts == 1:
                print("🏆 अविश्वसनीय! पहली ही try में!")
            elif attempts <= 3:
                print("🌟 बहुत अच्छा! आप expert हैं!")
            elif attempts <= 5:
                print("👍 अच्छा काम!")
            else:
                print("😊 अच्छी कोशिश!")
            
            game_over = True
            
        elif guess < secret_number:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"📈 आपका अनुमान छोटा है! बड़ी संख्या try करें। ({remaining} tries बचे हैं)")
            
        else:  # guess > secret_number
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"📉 आपका अनुमान बड़ा है! छोटी संख्या try करें। ({remaining} tries बचे हैं)")
    
    except ValueError:
        print("❌ कृपया एक valid संख्या बताएं!")
        attempts -= 1  # Don't count invalid input

# Game Over
if not game_over:
    print(f"\n😔 Game Over! आपकी tries खत्म हो गईं।")
    print(f"🔍 सही संख्या थी: {secret_number}")

print("\n" + "=" * 50)
print("🙏 खेलने के लिए धन्यवाद!")

# Play Again Option
print("\n🔄 क्या आप फिर से खेलना चाहते हैं?")
print("इस file को फिर से run करें: python3 number_guessing_game.py")

# Game Statistics
print(f"\n📈 आपकी Performance:")
print(f"Total Attempts: {attempts}")
print(f"Success Rate: {('100%' if game_over else '0%')}")

# Learning Points
print(f"\n📚 इस game में आपने सीखा:")
print("✅ Variables का उपयोग")
print("✅ if-elif-else conditions")
print("✅ while loops")
print("✅ try-except error handling")
print("✅ Random number generation")
print("✅ User input handling")

print(f"\n🎯 Next Challenge: इस game को modify करके:")
print("1. Difficulty levels add करें (Easy, Medium, Hard)")
print("2. Score system बनाएं")
print("3. High score save करें")
print("4. Hints feature add करें")