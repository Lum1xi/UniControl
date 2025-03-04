from student import StudentManager
from colorama import Fore, Style
studentmanager = StudentManager()
while True:
    print(Fore.BLUE + "1. Додати студента")
    print("2. Додати оцінку")
    print("3. Вивести оцінки студента")
    print("4. Вивести середній бал студента")
    print("5. Вивести топ студентів")
    print("6. Вивести інформацію про студента")
    print("7. Вийти" + Style.RESET_ALL)
    choice = input("Ваш вибір: ")

    if choice == "1":
        student_name = input("Введіть ім'я студента: ").lower().title()
        studentmanager.add_student(student_name)
    elif choice == "2":
        student_name = input("Введіть ім'я студента: ").lower().title()
        student = studentmanager.get_student(student_name)
        if student:
            student.add_grade()
        else:
            print(Fore.RED + "Студента не знайдено." + Style.RESET_ALL)
    elif choice == "3":
        student_name = input("Введіть ім'я студента: ").lower().title()
        student = studentmanager.get_student(student_name)
        if student:
            print(student.get_grade())
        else:
            print(Fore.RED + "Студента не знайдено." + Style.RESET_ALL)
    elif choice == "4":
        student_name = input("Введіть ім'я студента: ").lower().title()
        student = studentmanager.get_student(student_name)
        if student:
            print(Fore.GREEN + str(student.get_average()) + Style.RESET_ALL)
        else:
            print(Fore.RED + "Студента не знайдено." + Style.RESET_ALL)
    elif choice == "5":
        top_students = studentmanager.get_top_students()
        print(Fore.MAGENTA + "Топ студенти:" + Style.RESET_ALL)
        for student in top_students:
            print(f"{Fore.YELLOW}{student.name} - {student.get_average():.2f}{Style.RESET_ALL}")
    elif choice == "6":
        student_name = input("Введіть ім'я студента: ").lower().title()
        studentmanager.get_student_info(student_name)
    elif choice == "7":
        break
    else:
        print(Fore.RED + "Невірний вибір. Спробуйте ще раз." + Style.RESET_ALL)
