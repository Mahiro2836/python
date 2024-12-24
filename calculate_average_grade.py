def calculate_average_grade(grades):
    if not grades:
        return None
    return round(sum(grades) / len(grades), 2)

def find_students_above_average(students_grades, average_grade):
    if average_grade is None:
      return []
    return [
        student
        for student, grade in students_grades.items()
        if grade > average_grade
    ]

def find_students_below_average(students_grades, average_grade):
    if average_grade is None:
      return []
    return [
        student
        for student, grade in students_grades.items()
        if grade < average_grade
    ]

def find_highest_grade_student(students_grades):
    if not students_grades:
        return None
    highest_grade_student = max(students_grades, key=students_grades.get)
    return highest_grade_student, students_grades[highest_grade_student]

def find_lowest_grade_student(students_grades):
    if not students_grades:
        return None
    lowest_grade_student = min(students_grades, key=students_grades.get)
    return lowest_grade_student, students_grades[lowest_grade_student]

def analyze_grades(students_grades):
    grades = list(students_grades.values())
    average_grade = calculate_average_grade(grades)

    print("----- Анализ оценок студентов -----")

    if average_grade is not None:
        print(f"Средний балл: {average_grade}")
        above_average = find_students_above_average(students_grades, average_grade)
        if above_average:
             print(f"Студенты с оценками выше среднего: {', '.join(above_average)}")
        else:
            print("Нет студентов с оценками выше среднего")

        below_average = find_students_below_average(students_grades, average_grade)
        if below_average:
             print(f"Студенты с оценками ниже среднего: {', '.join(below_average)}")
        else:
            print("Нет студентов с оценками ниже среднего")
    else:
        print("Нет данных об оценках.")

    highest_grade_info = find_highest_grade_student(students_grades)
    if highest_grade_info:
        highest_student, highest_grade = highest_grade_info
        print(f"Студент с наивысшей оценкой: {highest_student} ({highest_grade})")
    else:
        print("Нет данных об оценках для поиска студента с наивысшей оценкой")

    lowest_grade_info = find_lowest_grade_student(students_grades)
    if lowest_grade_info:
        lowest_student, lowest_grade = lowest_grade_info
        print(f"Студент с наименьшей оценкой: {lowest_student} ({lowest_grade})")
    else:
        print("Нет данных об оценках для поиска студента с наименьшей оценкой")

if __name__ == "__main__":
    students_grades = {
        "Иван": 4,
        "Мария": 5,
        "Петр": 3,
        "Анна": 5,
        "Елена": 4,
        "Сергей": 2,
    }

    analyze_grades(students_grades)

    print("\nАнализ для пустого списка:")
    analyze_grades({})

    print("\nАнализ для списка с одним студентом:")
    analyze_grades({"Алексей": 5})