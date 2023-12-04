def solution(grades1, grades2):
    # Створюємо порожній словник для зберігання різниці в оцінках
    grade_difference = {}

    # Перебираємо ключі (ПІБ студентів) в одному зі словників (можна обрати будь-який)
    for student in grades1:
        # Перевіряємо, чи такий студент є і в іншому словнику
        if student in grades2:
            # Рахуємо різницю в оцінках
            difference = grades1[student] - grades2[student]
            # Записуємо різницю в словник
            grade_difference[student] = difference

    return grade_difference


if __name__ == "__main__":
    grades_1 = {'Анна Коваленко': 92, 'Олег Петров': 85, 'Ірина Сидорова': 78, 'Свирид Свиридович': 99}
    grades_2 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 80}
    print(solution(grades_1, grades_2))