#!/usr/bin/env python3
# Python Learning Quick Start - तुरंत शुरू करें!

import os
import subprocess
import sys

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def run_python_file(file_path):
    """Run a Python file and wait for user to continue"""
    try:
        print(f"\n🚀 Running: {file_path}")
        print("=" * 50)
        subprocess.run([sys.executable, file_path], check=True)
        print("\n" + "=" * 50)
        input("📱 Press Enter to continue...")
    except subprocess.CalledProcessError:
        print("❌ Error running the file!")
        input("📱 Press Enter to continue...")
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        input("📱 Press Enter to continue...")

def show_menu():
    clear_screen()
    print("🐍 Python Learning Center - हिंदी में सीखें! 🐍")
    print("=" * 60)
    print("📚 Choose your learning path:")
    print()
    print("1️⃣  Day 1: Variables और Data Types")
    print("2️⃣  Day 2: Operators")
    print("3️⃣  Daily Practice Challenges")
    print("4️⃣  Number Guessing Game (Project)")
    print("5️⃣  View Learning Guide")
    print("6️⃣  Check Python Installation")
    print("0️⃣  Exit")
    print()
    print("=" * 60)

def show_learning_guide():
    """Display the learning guide"""
    clear_screen()
    print("📖 Python Learning Guide")
    print("=" * 50)
    
    guide_content = """
    🎯 12-Week Python Learning Plan:
    
    Week 1-2: Basics
    ✅ Variables, Data Types
    ✅ Operators
    ⏳ Control Structures (if-else)
    ⏳ Loops (for, while)
    
    Week 3-4: Data Structures
    ⏳ Lists, Tuples
    ⏳ Dictionaries, Sets
    ⏳ String manipulation
    
    Week 5-6: Functions
    ⏳ Function definition
    ⏳ Parameters, return values
    ⏳ Scope, lambda functions
    
    Week 7-8: OOP
    ⏳ Classes and Objects
    ⏳ Inheritance
    ⏳ Encapsulation
    
    Week 9-10: File Handling
    ⏳ Reading/Writing files
    ⏳ Exception handling
    ⏳ Working with CSV, JSON
    
    Week 11-12: Libraries & Projects
    ⏳ Popular libraries (requests, pandas)
    ⏳ Web scraping
    ⏳ GUI applications
    ⏳ Final projects
    
    📅 Daily Routine:
    • Morning (30 mins): Theory
    • Evening (1 hour): Coding practice
    • Weekend: Project work
    
    🌟 Tips for Success:
    • Code daily, even if just 30 minutes
    • Practice on real projects
    • Join Python communities
    • Don't just read, write code!
    """
    
    print(guide_content)
    input("\n📱 Press Enter to return to menu...")

def check_python():
    """Check Python installation and version"""
    clear_screen()
    print("🔍 Python Installation Check")
    print("=" * 40)
    
    try:
        import sys
        print(f"✅ Python Version: {sys.version}")
        print(f"✅ Python Path: {sys.executable}")
        
        # Check some basic modules
        modules_to_check = ['random', 'datetime', 'os', 'json']
        print(f"\n📦 Checking essential modules:")
        
        for module in modules_to_check:
            try:
                __import__(module)
                print(f"  ✅ {module}")
            except ImportError:
                print(f"  ❌ {module} - Not available")
        
        print(f"\n🎉 Your Python installation looks good!")
        print(f"🚀 Ready to start learning!")
        
    except Exception as e:
        print(f"❌ Error checking Python: {e}")
    
    input("\n📱 Press Enter to return to menu...")

def main():
    while True:
        show_menu()
        
        try:
            choice = input("👉 Enter your choice (0-6): ").strip()
            
            if choice == '1':
                run_python_file("python_learning/basics/day1_variables.py")
            
            elif choice == '2':
                run_python_file("python_learning/basics/day2_operators.py")
            
            elif choice == '3':
                run_python_file("python_learning/practice/daily_practice.py")
            
            elif choice == '4':
                run_python_file("python_learning/projects/number_guessing_game.py")
            
            elif choice == '5':
                show_learning_guide()
            
            elif choice == '6':
                check_python()
            
            elif choice == '0':
                clear_screen()
                print("🙏 Happy Learning! Python Master बनने के लिए daily practice करते रहें!")
                print("📚 Remember: Practice makes perfect!")
                print("🌟 आपका Python journey यहीं से शुरू होता है!")
                break
            
            else:
                clear_screen()
                print("❌ Invalid choice! Please select 0-6.")
                input("📱 Press Enter to continue...")
        
        except KeyboardInterrupt:
            clear_screen()
            print("\n👋 Goodbye! Keep coding!")
            break
        except Exception as e:
            clear_screen()
            print(f"❌ An error occurred: {e}")
            input("📱 Press Enter to continue...")

if __name__ == "__main__":
    main()