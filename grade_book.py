import statistics

grade_book = dict()


def add_grade():
    try:
        student_name = input("Student Name: ")
        grade = int(input("Grade: "))
        print("Adding grade to the books...")

        if student_name in grade_book:
            grade_book[student_name].append(grade)
        else:
            grade_book.setdefault(student_name, []).append(grade)
    except ValueError:
        print("You entered a non numeric value in the Grade field. Exiting to the main menu.\n")


def remove_student():
    student_name = input("Student Name: ")
    print("Removing student from the books...")

    if student_name in grade_book:
        grade_book.pop(student_name, None)
    else:
        print("The student that you are trying to remove does not exist within the books.")


def get_student_average():
    student_name = input("Student Name: ")

    if student_name in grade_book:
        average_grade = statistics.mean(grade_book[student_name])
        print(student_name, "has the average grade of", str(average_grade) + ".")
    else:
        print("The student that you are trying to remove does not exist within the books.")


def main_menu():
    print("Welcome to your grade book!")
    print("Please select one of the following options:\n")

    print("1) Enter Grades")
    print("2) Remove a Student")
    print("3) Average Grade of a Student")
    print("4) Exit\n")

    user_input = input("What would you like to do? (Please enter a number) ")

    if user_input == "1":
        add_grade()
    elif user_input == "2":
        remove_student()
    elif user_input == "3":
        get_student_average()
    elif user_input == "4":
        print("Exiting program. Have a great day. Thank you!")
        exit()
    else:
        print("You have entered an option that is not available. Please retry.")

    print("Entries in your grade book:", grade_book)
    print("Returning to the main menu...\n")


while True:
    main_menu()
