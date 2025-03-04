from conf import all_subjects


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_name):
        student = Student(student_name)
        self.students.append(student)

    def get_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student
        return None

    def get_top_students(self, n=3):
        sorted_students = sorted(self.students, key=lambda s: s.get_average(), reverse=True)
        return sorted_students[:n]

    def get_student_info(self, student_name):
        student = self.get_student(student_name)
        if student is None:
            print("Студента з таким ім'ям не знайдено.")
            return
        print(f"Ім'я: {student.name}")
        print(f"Оцінки:\n{student.get_grade()}")
        print(f"Середній бал: {student.get_average():.2f}")


class Student:
    def __init__(self, full_name):
        self.name = full_name
        self.grades = {subject: None for subject in all_subjects}

    def get_grade(self):
        grade_list = []
        for subject, grade in self.grades.items():
            grade_list.append(f"{subject}: {grade if grade is not None else 'Немає оцінки'}")
        return "\n".join(grade_list)

    def add_grade(self):
        for index, subject in enumerate(all_subjects):
            print(f"{index}. {subject}")
        try:
            subject_index = int(input("\nПо якому предмету виставляємо оцінку (введіть номер): "))
            if 0 <= subject_index < len(all_subjects):
                subject = all_subjects[subject_index]
                grade = int(input("Яка оцінка: "))
                if 1 <= grade <= 12:
                    self.grades[subject] = grade
                else:
                    print("Оцінка повинна бути в діапазоні від 1 до 12.")
            else:
                print("Невірний індекс предмета.")
        except ValueError:
            print("Будь ласка, введіть коректне число.")

    def get_average(self):
        valid_grades = [grade for grade in self.grades.values() if grade is not None]
        return sum(valid_grades) / len(valid_grades) if valid_grades else 0
