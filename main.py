from student import StudentManager

studentmanager = StudentManager()
while True:
    print("1. Додати студента")
    print("2. Додати оцінку")
    print("3. Вивести оцінки студента")
    print("4. Вивести середній бал студента")
    print("5. Вивести топ студентів")
    print("6. Вивести інформацію про студента")
    print("7. Вийти")
    choice = input("Ваш вибір: ")

    if choice == "1":
        student_name = input("Введіть ім'я студента: ")
        studentmanager.add_student(student_name)
    elif choice == "2":
        student_name = input("Введіть ім'я студента: ")
        student = studentmanager.get_student(student_name)
        if student:
            student.add_grade()
        else:
            print("Студента не знайдено.")
    elif choice == "3":
        student_name = input("Введіть ім'я студента: ")
        student = studentmanager.get_student(student_name)
        if student:
            print(student.get_grade())
        else:
            print("Студента не знайдено.")
    elif choice == "4":
        student_name = input("Введіть ім'я студента: ")
        student = studentmanager.get_student(student_name)
        if student:
            print(student.get_average())
        else:
            print("Студента не знайдено.")
    elif choice == "5":
        top_students = studentmanager.get_top_students()
        print("Топ студенти:")
        for student in top_students:
            print(f"{student.name} - {student.get_average():.2f}")
    elif choice == "6":
        student_name = input("Введіть ім'я студента: ")
        studentmanager.get_student_info(student_name)
    elif choice == "7":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
