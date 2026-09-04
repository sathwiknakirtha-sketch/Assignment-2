import csv
import os

file_name = "students.csv"

# Create file if it does not exist
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll Number", "Name", "Marks"])


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([roll, name, marks])

        print("Student added successfully!")

    # Display Students
    elif choice == "2":
        with open(file_name, "r") as file:
            reader = csv.reader(file)

            print("\n--- STUDENT DETAILS ---")

            for row in reader:
                print(row)

    # Search Student
    elif choice == "3":
        roll = input("Enter roll number to search: ")
        found = False

        with open(file_name, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == roll:
                    print("\nStudent Found!")
                    print("Roll Number:", row[0])
                    print("Name:", row[1])
                    print("Marks:", row[2])
                    found = True
                    break

        if not found:
            print("Student not found!")

    # Delete Student
    elif choice == "4":
        roll = input("Enter roll number to delete: ")

        students = []
        found = False

        with open(file_name, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == roll:
                    found = True
                else:
                    students.append(row)

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)

        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # Exit
    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")