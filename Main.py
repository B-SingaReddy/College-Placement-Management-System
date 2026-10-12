
import json
import os
FILE_NAME = "students.json"
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                print("Invalid data format. Starting with empty records.")
        except (json.JSONDecodeError, OSError):
            print("Could not read data file. Starting with empty records.")
    return []
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def find_student(students, roll_no):
    for student in students:
        if student["roll_no"].lower() == roll_no.lower():
            return student
    return None


def get_cgpa():
    while True:
        try:
            cgpa = float(input("Enter CGPA (0-10): "))
            if 0 <= cgpa <= 10:
                return cgpa
            print("CGPA must be between 0 and 10.")
        except ValueError:
            print("Please enter a valid number.")


def add_student(students):
    print("\n--- Add Student ---")

    roll_no = input("Enter roll number: ").strip()

    if not roll_no:
        print("Roll number cannot be empty.")
        return

    if find_student(students, roll_no):
        print("Roll number already exists!")
        return

    name = input("Enter student name: ").strip()
    branch = input("Enter branch: ").strip()

    if not name or not branch:
        print("Name and branch cannot be empty.")
        return

    cgpa = get_cgpa()

    student = {
        "roll_no": roll_no,
        "name": name,
        "branch": branch,
        "cgpa": cgpa
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-" * 30)
        print("Roll Number:", student["roll_no"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("CGPA:", student["cgpa"])


def search_student(students):
    roll_no = input("Enter roll number to search: ").strip()
    student = find_student(students, roll_no)

    if student:
        print("\nStudent Found")
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("CGPA:", student["cgpa"])
    else:
        print("Student not found.")


def update_student(students):
    roll_no = input("Enter roll number to update: ").strip()
    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")

    name = input("New name (" + student["name"] + "): ").strip()
    if name:
        student["name"] = name

    branch = input("New branch (" + student["branch"] + "): ").strip()
    if branch:
        student["branch"] = branch

    while True:
        cgpa = input("New CGPA (press Enter to keep): ").strip()

        if not cgpa:
            break

        try:
            value = float(cgpa)
            if 0 <= value <= 10:
                student["cgpa"] = value
                break
            print("CGPA must be between 0 and 10.")
        except ValueError:
            print("Enter a valid number.")

    save_students(students)
    print("Student updated successfully!")


def delete_student(students):
    roll_no = input("Enter roll number to delete: ").strip()
    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    confirm = input(
        "Delete " + student["name"] + "? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Delete cancelled.")


def check_eligibility(students):
    if not students:
        print("No student records available.")
        return

    minimum = get_cgpa()
    found = False

    print("\nEligible Students:")

    for student in students:
        if student["cgpa"] >= minimum:
            print(
                student["name"],
                "| Roll No:", student["roll_no"],
                "| CGPA:", student["cgpa"]
            )
            found = True

    if not found:
        print("No eligible students found.")

def main():
    students = load_students()

    while True:
        print("\n===== COLLEGE PLACEMENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Check Placement Eligibility")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Enter the minimum required CGPA.")
            check_eligibility(students)
        elif choice == "7":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Enter 1 to 7.")


if __name__ == "__main__":
    main()
