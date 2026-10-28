
import json

students = {}

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    students[sid] = name
    print("Student added successfully!")

def view_students():
    for sid, name in students.items():
        print(sid, name)

def save_data():
    with open("students.txt", "w") as f:
        json.dump(students, f)
    print("Data saved!")

def load_data():
    global students
    try:
        with open("students.txt", "r") as f:
            students = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        students = {}

def main():
    load_data()

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Save Data")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                view_students()
            elif choice == 3:
                save_data()
            elif choice == 4:
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a number!")

main()
