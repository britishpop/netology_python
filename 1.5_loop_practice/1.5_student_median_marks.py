students = [
    {"name": "Карина", "surname": "Степанова", "sex": "женский", "exp": True, "homeworks": [8, 6, 10, 7, 6], "exam": 8},
    {"name": "Саша", "surname": "Фулбрайт", "sex": "мужской", "exp": False, "homeworks": [8, 8, 9, 6, 9], "exam": 10},
    {"name": "Саша", "surname": "Фулбрайт", "sex": "женский", "exp": True, "homeworks": [9, 9, 9, 7, 6], "exam": 10},
    {"name": "Евгений", "surname": "Горский", "sex": "мужской", "exp": False, "homeworks": [3, 4, 8, 1, 6], "exam": 5},
    {"name": "Валентин", "surname": "Рубинштейн", "sex": "мужской", "exp": False, "homeworks": [7, 2, 9, 6, 5],
     "exam": 6},
    {"name": "Инга", "surname": "Махмутова", "sex": "женский", "exp": True, "homeworks": [7, 4, 8, 5, 9], "exam": 8},
    {"name": "Ильза", "surname": "Ростова", "sex": "женский", "exp": False, "homeworks": [7, 8, 7, 9, 7], "exam": 7},
    {"name": "Андрей", "surname": "Берг", "sex": "мужской", "exp": True, "homeworks": [8, 9, 8, 8, 7], "exam": 8}
]


def main(args):
    user_choice = ""
    while "q" not in user_choice:
        user_choice = input(
            "Сессия завершилась. Все данные собраны и посчитаны. Выберите команду, чтобы узнать оценки:\n mg - узнать средние оценки по группе\n ms - узнать средние оценки по срезам мужчина/женщина и с опытом/без опыта\n bs - узнать имя лучшего студента в группе\n q - завершить программу и пойти домой\n ")
        if user_choice == "mg":
            median_mark()
            print("Средняя оценка за домашние задания по группе - {},\n средняя оценка за экзамен - {}".format(
                args["group_hw"], (args["group_exam"])))
        elif user_choice == "ms":
            median_mark()
            print(
                "У мужчин средняя оценка за домашние задания - {}, за экзамены - {}\nУ женщин средняя оценка за домашние задания - {}, за экзамены - {},\nУ студентов с опытом программирования средняя оценка за домашние задания - {}, за экзамен - {}\nУ студентов без опыта программирования средняя оценка за домашние задания - {}, за экзамен - {}".format(
                    args["male_hw"], args["male_exam"], args["female_hw"], args["female_exam"], args["exp_hw"],
                    args["exp_exam"], args["nonexp_hw"], args["nonexp_exam"]))
        elif user_choice == "bs":
            best_student()


def median(args):
    median_value = round(sum(args) / len(args), 1)
    return median_value


def median_mark():
    female_marks_hw = []
    male_marks_hw = []
    exp_marks_hw = []
    nonexp_marks_hw = []
    female_marks_exam = []
    male_marks_exam = []
    exp_marks_exam = []
    nonexp_marks_exam = []
    for student_data in students:
        if "женский" in student_data["sex"]:
            female_marks_hw.append(median(student_data["homeworks"]))
            female_marks_exam.append(student_data["exam"])
        else:
            male_marks_hw.append(median(student_data["homeworks"]))
            male_marks_exam.append(student_data["exam"])
        if student_data["exp"] == True:
            exp_marks_hw.append(median(student_data["homeworks"]))
            exp_marks_exam.append(student_data["exam"])
        else:
            nonexp_marks_hw.append(median(student_data["homeworks"]))
            nonexp_marks_exam.append(student_data["exam"])
    group_marks_hw = round(((median(female_marks_hw) + median(male_marks_hw)) / 2), 1)
    group_marks_exam = round(((median(female_marks_exam) + median(male_marks_exam)) / 2), 1)
    overall_marks = {
        "female_hw": median(female_marks_hw),
        "female_exam": median(female_marks_exam),
        "male_hw": median(male_marks_hw),
        "male_exam": median(male_marks_exam),
        "exp_hw": median(exp_marks_hw),
        "exp_exam": median(exp_marks_exam),
        "nonexp_hw": median(nonexp_marks_hw),
        "nonexp_exam": median(nonexp_marks_exam),
        "group_hw": group_marks_hw,
        "group_exam": group_marks_exam
    }
    return overall_marks


def best_student():
    integral_mark_group = []
    all_marks = []
    best_students = []
    for student_data in students:
        integral_mark = round(0.6 * median(student_data["homeworks"]) + 0.4 * student_data["exam"], 1)
        integral_mark_group.append(dict(
            [("name", student_data['name']), ("surname", student_data['surname']), ("integral_mark", integral_mark)]))
        all_marks.append(integral_mark)
    for best_marks in integral_mark_group:
        if best_marks["integral_mark"] == max(all_marks):
            best_students.append(best_marks)
    if len(best_students) < 2:
        print("Лучший студент - {} {} с интегральной оценкой {}".format(best_students[0]["name"],
                                                                        best_students[0]["surname"],
                                                                        best_students[0]["integral_mark"]))
    else:
        print("Лучшие студенты - \n{}".format(best_students))


main(median_mark())
