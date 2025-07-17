# Python Projects for Practice
# यहाँ complete projects हैं जो आप बना सकते हैं

import random
import json
from datetime import datetime

def show_projects_menu():
    """Main menu to select different projects"""
    print("🚀 Python Projects Collection 🚀")
    print("=" * 40)
    print("1. To-Do List Manager")
    print("2. Simple Banking System")
    print("3. Student Grade Management")
    print("4. Number Guessing Game (Advanced)")
    print("5. Contact Book")
    print("6. Quiz Game")
    print("7. Exit")
    print("=" * 40)

def todo_list_manager():
    """Complete To-Do List application"""
    print("\n📝 TO-DO LIST MANAGER 📝")
    tasks = []
    
    while True:
        print("\n--- Menu ---")
        print("1. Tasks देखें")
        print("2. नया Task add करें")
        print("3. Task complete करें")
        print("4. Task delete करें")
        print("5. Tasks save करें")
        print("6. Main menu पर वापस जाएं")
        
        choice = input("\nअपनी choice enter करें: ")
        
        if choice == "1":
            if not tasks:
                print("❌ कोई tasks नहीं हैं!")
            else:
                print("\n📋 आपके Tasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✅" if task['completed'] else "⏳"
                    print(f"{i}. {status} {task['name']} - {task['priority']}")
        
        elif choice == "2":
            task_name = input("Task का नाम: ")
            priority = input("Priority (High/Medium/Low): ").title()
            tasks.append({
                'name': task_name,
                'priority': priority,
                'completed': False,
                'created': datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            print(f"✅ '{task_name}' task add कर दिया गया!")
        
        elif choice == "3":
            if tasks:
                try:
                    task_num = int(input("कौन सा task complete करना है? (number): "))
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num - 1]['completed'] = True
                        print(f"✅ Task complete हो गया: {tasks[task_num - 1]['name']}")
                    else:
                        print("❌ Invalid task number!")
                except ValueError:
                    print("❌ Please enter a valid number!")
            else:
                print("❌ कोई tasks नहीं हैं!")
        
        elif choice == "4":
            if tasks:
                try:
                    task_num = int(input("कौन सा task delete करना है? (number): "))
                    if 1 <= task_num <= len(tasks):
                        deleted_task = tasks.pop(task_num - 1)
                        print(f"🗑️ Task delete कर दिया: {deleted_task['name']}")
                    else:
                        print("❌ Invalid task number!")
                except ValueError:
                    print("❌ Please enter a valid number!")
            else:
                print("❌ कोई tasks नहीं हैं!")
        
        elif choice == "5":
            with open("tasks.json", "w", encoding="utf-8") as file:
                json.dump(tasks, file, ensure_ascii=False, indent=2)
            print("💾 Tasks save हो गए!")
        
        elif choice == "6":
            break
        
        else:
            print("❌ Invalid choice!")

def banking_system():
    """Simple Banking System"""
    print("\n🏦 SIMPLE BANKING SYSTEM 🏦")
    
    account = {
        'name': '',
        'account_number': '',
        'balance': 0,
        'transactions': []
    }
    
    # Account setup
    if not account['name']:
        account['name'] = input("अपना नाम enter करें: ")
        account['account_number'] = f"ACC{random.randint(10000, 99999)}"
        account['balance'] = float(input("Initial deposit amount: ₹"))
        account['transactions'].append({
            'type': 'Initial Deposit',
            'amount': account['balance'],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"✅ Account बन गया! Account Number: {account['account_number']}")
    
    while True:
        print("\n--- Banking Menu ---")
        print("1. Balance check करें")
        print("2. Money deposit करें")
        print("3. Money withdraw करें")
        print("4. Transaction history देखें")
        print("5. Account details देखें")
        print("6. Main menu पर वापस जाएं")
        
        choice = input("\nअपनी choice enter करें: ")
        
        if choice == "1":
            print(f"💰 Current Balance: ₹{account['balance']}")
        
        elif choice == "2":
            try:
                amount = float(input("कितना deposit करना है? ₹"))
                if amount > 0:
                    account['balance'] += amount
                    account['transactions'].append({
                        'type': 'Deposit',
                        'amount': amount,
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    print(f"✅ ₹{amount} deposit हो गया! New Balance: ₹{account['balance']}")
                else:
                    print("❌ Amount positive होना चाहिए!")
            except ValueError:
                print("❌ Valid amount enter करें!")
        
        elif choice == "3":
            try:
                amount = float(input("कितना withdraw करना है? ₹"))
                if amount > 0:
                    if amount <= account['balance']:
                        account['balance'] -= amount
                        account['transactions'].append({
                            'type': 'Withdrawal',
                            'amount': amount,
                            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })
                        print(f"✅ ₹{amount} withdraw हो गया! Remaining Balance: ₹{account['balance']}")
                    else:
                        print("❌ Insufficient balance!")
                else:
                    print("❌ Amount positive होना चाहिए!")
            except ValueError:
                print("❌ Valid amount enter करें!")
        
        elif choice == "4":
            print("\n📊 Transaction History:")
            if account['transactions']:
                for i, transaction in enumerate(account['transactions'], 1):
                    print(f"{i}. {transaction['type']}: ₹{transaction['amount']} - {transaction['timestamp']}")
            else:
                print("❌ No transactions yet!")
        
        elif choice == "5":
            print(f"\n👤 Account Details:")
            print(f"Name: {account['name']}")
            print(f"Account Number: {account['account_number']}")
            print(f"Current Balance: ₹{account['balance']}")
            print(f"Total Transactions: {len(account['transactions'])}")
        
        elif choice == "6":
            break
        
        else:
            print("❌ Invalid choice!")

def student_grade_management():
    """Student Grade Management System"""
    print("\n🎓 STUDENT GRADE MANAGEMENT 🎓")
    
    students = {}
    
    while True:
        print("\n--- Student Management Menu ---")
        print("1. नया Student add करें")
        print("2. Student के marks add करें")
        print("3. Student का report card देखें")
        print("4. सभी Students की list देखें")
        print("5. Class average calculate करें")
        print("6. Main menu पर वापस जाएं")
        
        choice = input("\nअपनी choice enter करें: ")
        
        if choice == "1":
            student_id = input("Student ID enter करें: ")
            if student_id not in students:
                name = input("Student का नाम: ")
                students[student_id] = {
                    'name': name,
                    'subjects': {},
                    'total_marks': 0,
                    'average': 0
                }
                print(f"✅ Student '{name}' add हो गया!")
            else:
                print("❌ यह Student ID पहले से exists है!")
        
        elif choice == "2":
            if not students:
                print("❌ पहले students add करें!")
                continue
            
            student_id = input("Student ID enter करें: ")
            if student_id in students:
                subject = input("Subject का नाम: ")
                try:
                    marks = float(input(f"{subject} के marks: "))
                    if 0 <= marks <= 100:
                        students[student_id]['subjects'][subject] = marks
                        
                        # Calculate total and average
                        total = sum(students[student_id]['subjects'].values())
                        count = len(students[student_id]['subjects'])
                        students[student_id]['total_marks'] = total
                        students[student_id]['average'] = total / count
                        
                        print(f"✅ {subject} के marks add हो गए!")
                    else:
                        print("❌ Marks 0-100 के बीच होने चाहिए!")
                except ValueError:
                    print("❌ Valid marks enter करें!")
            else:
                print("❌ Student ID नहीं मिला!")
        
        elif choice == "3":
            if not students:
                print("❌ कोई students नहीं हैं!")
                continue
            
            student_id = input("Student ID enter करें: ")
            if student_id in students:
                student = students[student_id]
                print(f"\n📊 Report Card - {student['name']} (ID: {student_id})")
                print("-" * 40)
                
                if student['subjects']:
                    for subject, marks in student['subjects'].items():
                        print(f"{subject}: {marks}")
                    
                    print("-" * 40)
                    print(f"Total Marks: {student['total_marks']}")
                    print(f"Average: {student['average']:.2f}")
                    
                    # Grade calculation
                    avg = student['average']
                    if avg >= 90:
                        grade = "A+"
                    elif avg >= 80:
                        grade = "A"
                    elif avg >= 70:
                        grade = "B"
                    elif avg >= 60:
                        grade = "C"
                    else:
                        grade = "F"
                    
                    print(f"Grade: {grade}")
                else:
                    print("❌ अभी तक कोई marks add नहीं किए गए!")
            else:
                print("❌ Student ID नहीं मिला!")
        
        elif choice == "4":
            if students:
                print("\n👥 All Students:")
                print("-" * 50)
                for student_id, student in students.items():
                    print(f"ID: {student_id} | Name: {student['name']} | Average: {student['average']:.2f}")
            else:
                print("❌ कोई students नहीं हैं!")
        
        elif choice == "5":
            if students:
                total_avg = sum(student['average'] for student in students.values() if student['average'] > 0)
                student_count = sum(1 for student in students.values() if student['average'] > 0)
                
                if student_count > 0:
                    class_average = total_avg / student_count
                    print(f"\n📈 Class Average: {class_average:.2f}")
                else:
                    print("❌ अभी तक किसी student के marks add नहीं किए गए!")
            else:
                print("❌ कोई students नहीं हैं!")
        
        elif choice == "6":
            break
        
        else:
            print("❌ Invalid choice!")

def advanced_guessing_game():
    """Advanced Number Guessing Game with levels"""
    print("\n🎯 ADVANCED GUESSING GAME 🎯")
    
    levels = {
        1: {"range": (1, 10), "attempts": 4, "name": "Beginner"},
        2: {"range": (1, 50), "attempts": 7, "name": "Intermediate"},
        3: {"range": (1, 100), "attempts": 10, "name": "Advanced"}
    }
    
    score = 0
    
    print("Choose difficulty level:")
    for level, info in levels.items():
        print(f"{level}. {info['name']} (1-{info['range'][1]}, {info['attempts']} attempts)")
    
    try:
        level = int(input("\nLevel select करें: "))
        if level not in levels:
            print("❌ Invalid level!")
            return
        
        level_info = levels[level]
        secret_number = random.randint(*level_info['range'])
        attempts = 0
        max_attempts = level_info['attempts']
        
        print(f"\n🎮 {level_info['name']} Level Started!")
        print(f"मैंने {level_info['range'][0]} से {level_info['range'][1]} के बीच एक number सोचा है!")
        print(f"आपके पास {max_attempts} attempts हैं।")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: "))
                attempts += 1
                
                if guess == secret_number:
                    points = (max_attempts - attempts + 1) * level * 10
                    score += points
                    print(f"🎉 बधाई हो! सही answer!")
                    print(f"Answer था: {secret_number}")
                    print(f"Points earned: {points}")
                    print(f"Total Score: {score}")
                    break
                elif guess < secret_number:
                    print("⬆️ Higher number try करें!")
                else:
                    print("⬇️ Lower number try करें!")
                
                if attempts == max_attempts:
                    print(f"\n😔 Game Over! Answer था: {secret_number}")
                    print(f"Final Score: {score}")
                    
            except ValueError:
                print("❌ Valid number enter करें!")
                
    except ValueError:
        print("❌ Valid level enter करें!")

def contact_book():
    """Simple Contact Book"""
    print("\n📞 CONTACT BOOK 📞")
    
    contacts = {}
    
    while True:
        print("\n--- Contact Menu ---")
        print("1. नया Contact add करें")
        print("2. Contact search करें")
        print("3. सभी Contacts देखें")
        print("4. Contact update करें")
        print("5. Contact delete करें")
        print("6. Main menu पर वापस जाएं")
        
        choice = input("\nअपनी choice enter करें: ")
        
        if choice == "1":
            name = input("Contact का नाम: ").title()
            if name not in contacts:
                phone = input("Phone number: ")
                email = input("Email (optional): ")
                contacts[name] = {
                    'phone': phone,
                    'email': email,
                    'created': datetime.now().strftime("%Y-%m-%d")
                }
                print(f"✅ Contact '{name}' add हो गया!")
            else:
                print("❌ यह contact पहले से exists है!")
        
        elif choice == "2":
            if not contacts:
                print("❌ कोई contacts नहीं हैं!")
                continue
            
            search_term = input("Name search करें: ").title()
            found = False
            for name, info in contacts.items():
                if search_term.lower() in name.lower():
                    print(f"\n📱 {name}")
                    print(f"Phone: {info['phone']}")
                    print(f"Email: {info['email']}")
                    print(f"Added: {info['created']}")
                    found = True
            
            if not found:
                print("❌ कोई contact नहीं मिला!")
        
        elif choice == "3":
            if contacts:
                print("\n📋 All Contacts:")
                print("-" * 40)
                for name, info in contacts.items():
                    print(f"👤 {name}")
                    print(f"📞 {info['phone']}")
                    print(f"📧 {info['email']}")
                    print("-" * 40)
            else:
                print("❌ कोई contacts नहीं हैं!")
        
        elif choice == "4":
            if not contacts:
                print("❌ कोई contacts नहीं हैं!")
                continue
            
            name = input("कौन सा contact update करना है? ").title()
            if name in contacts:
                print(f"Current info for {name}:")
                print(f"Phone: {contacts[name]['phone']}")
                print(f"Email: {contacts[name]['email']}")
                
                new_phone = input("नया phone number (current रखने के लिए Enter): ")
                new_email = input("नया email (current रखने के लिए Enter): ")
                
                if new_phone:
                    contacts[name]['phone'] = new_phone
                if new_email:
                    contacts[name]['email'] = new_email
                
                print(f"✅ {name} का contact update हो गया!")
            else:
                print("❌ Contact नहीं मिला!")
        
        elif choice == "5":
            if not contacts:
                print("❌ कोई contacts नहीं हैं!")
                continue
            
            name = input("कौन सा contact delete करना है? ").title()
            if name in contacts:
                confirm = input(f"क्या आप sure हैं कि {name} को delete करना है? (y/n): ")
                if confirm.lower() == 'y':
                    del contacts[name]
                    print(f"🗑️ {name} का contact delete हो गया!")
                else:
                    print("❌ Contact delete नहीं किया गया!")
            else:
                print("❌ Contact नहीं मिला!")
        
        elif choice == "6":
            break
        
        else:
            print("❌ Invalid choice!")

def quiz_game():
    """Simple Quiz Game"""
    print("\n🧠 QUIZ GAME 🧠")
    
    questions = [
        {
            "question": "Python में list का पहला element access करने के लिए कौन सा index use करते हैं?",
            "options": ["A) 1", "B) 0", "C) -1", "D) first"],
            "answer": "B"
        },
        {
            "question": "Python में string को integer में convert करने के लिए कौन सा function use करते हैं?",
            "options": ["A) str()", "B) float()", "C) int()", "D) convert()"],
            "answer": "C"
        },
        {
            "question": "Python में loop के लिए कौन सा keyword use करते हैं?",
            "options": ["A) loop", "B) for", "C) repeat", "D) while"],
            "answer": "B"
        },
        {
            "question": "Python में comment add करने के लिए कौन सा symbol use करते हैं?",
            "options": ["A) //", "B) /*", "C) #", "D) --"],
            "answer": "C"
        },
        {
            "question": "Python में function define करने के लिए कौन सा keyword use करते हैं?",
            "options": ["A) function", "B) def", "C) func", "D) define"],
            "answer": "B"
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print(f"📚 Total Questions: {total_questions}")
    print("हर सही answer के लिए 1 point मिलेगा!")
    
    for i, q in enumerate(questions, 1):
        print(f"\n❓ Question {i}/{total_questions}:")
        print(q["question"])
        
        for option in q["options"]:
            print(option)
        
        user_answer = input("\nआपका answer (A/B/C/D): ").upper()
        
        if user_answer == q["answer"]:
            print("✅ सही answer! बधाई हो!")
            score += 1
        else:
            print(f"❌ गलत answer! सही answer था: {q['answer']}")
    
    print(f"\n🏆 Quiz Complete!")
    print(f"आपका Score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 80:
        print("🌟 Excellent! Python में आपकी knowledge बहुत अच्छी है!")
    elif percentage >= 60:
        print("👍 Good! थोड़ी और practice करें!")
    else:
        print("📚 Python basics को फिर से revise करें!")

# Main Program
def main():
    """Main program function"""
    while True:
        show_projects_menu()
        
        try:
            choice = int(input("\nकौन सा project try करना चाहते हैं? "))
            
            if choice == 1:
                todo_list_manager()
            elif choice == 2:
                banking_system()
            elif choice == 3:
                student_grade_management()
            elif choice == 4:
                advanced_guessing_game()
            elif choice == 5:
                contact_book()
            elif choice == 6:
                quiz_game()
            elif choice == 7:
                print("🙏 धन्यवाद! Python सीखते रहें!")
                break
            else:
                print("❌ Invalid choice! 1-7 के बीच select करें।")
                
        except ValueError:
            print("❌ Please enter a valid number!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()