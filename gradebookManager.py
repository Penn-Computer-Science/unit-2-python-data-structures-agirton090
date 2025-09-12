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
    if not gradebook:
        print("Gradebook is empty.")
        return
    
    print("----- Gradebook Summary -----")
    averages = {}
    for student, grades in gradebook.items():
        avg = average(grades)
        averages[student] = avg
        print()


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

        choice = input("Choose (1-6): ")

        if choice == "1":
            name = input("Student name: ")
            if name in gradebook:
                print("That student already exists.")
            else:
                grades = input("Enter grades separated by spaces: ")
                gradebook[name] = [int(x) for x in grades.split()]
                print("Added {name}.")







