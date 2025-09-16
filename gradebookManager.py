def average(grades):
    if len(grades) == 0:
        return 0 
    return sum(grades) / len(grades)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
    
def show_summary(gradebook):
    print("----- Gradebook Summary -----")
    averages = {}

    if not gradebook:
        print("Gradebook is empty.")
        return

    for student, grades in gradebook.items():
        avg = average(grades)
        averages[student] = avg
        print(f"{student}: {avg:.2f} ({letter_grade(avg)}) ")

        
    if averages:
        top_student = max(averages, key=averages.get)
        print(f"Top Student: {top_student} with average {averages[top_student]:.2f}")

    

    
    


def main():

    gradebook = {
        "Josh": [59, 29, 30],
        "Bill": [89, 100, 78],
        "Frank": [24, 68, 98]
    }

    while True:
        print("-- Options --")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Remove a student")
        print("4. Remove a grade")
        print("5. View summary")
        print("6. Quit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Student name: ")
            if name in gradebook:
                print("That student already exists.")
            else:
                grades = input("Enter grades separated by spaces: ")
                gradebook[name] = list(map(int, grades.split()))
                print(f"Added {name}.")

        elif choice == "2":
            name = input("Enter student name: ")
            if name not in gradebook:
                print("Student not found.")
            else:
                grades = input("Enter grades separated by spaces: ")
                gradebook[name].extend(list(map(int, grades.split())))
                print("Grades added for {name}.")
        
        elif choice == "3":
            name = input ("Enter student name to remove: ")
            if name in gradebook:
                del gradebook[name]
                print(f"{name} removed.")
            else:
                print("Student not found.")
        
        elif choice == "4":
            name = input("Enter student name: ")
            if name in gradebook:
                print(f"{name}'s grades {gradebook[name]}")
                try:
                    grade = int(input("Enter the grade to remove: "))
                    gradebook[name].remove(grade)
                    print(f"Removed {grade} from {name}.")
                except ValueError:
                    print("That grade was not found.")
            else:
                print("Student not found.")

        elif choice == "5":
            show_summary(gradebook)

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

        








