def check_questions(cursor, current_user_node):
    cursor.execute(f"SELECT * FROM questions WHERE node_id={current_user_node}")
    questions = cursor.fetchall()
    correct_count = 0
    for q in questions:
        print(q[2])
        cursor.execute(f"SELECT * FROM answer_variants WHERE question_id={q[0]}")
        variants = cursor.fetchall()
        variants = [(i + 1, variants[i]) for i in range(len(variants))]
        print('-' * 75)
        for var in variants:
            print(f'{var[0]}. {var[1][2]}')
        answer = input("Выберите вариант ответа: ")
        while True:
            try:
                answer = int(answer)
                if answer < 0 or answer > len(variants):
                    raise ValueError
                break
            except ValueError:
                answer = input("Выберите вариант ответа: ")
        print('-' * 75)
        if variants[answer - 1][1][3]:
            print("Верно\n")
            correct_count += 1
        else:
            print("Неверно\n")
        print('=' * 75)
        print()

    if correct_count == len(questions):
        return True
    else:
        print("Прорешайте ещё раз!")
        return False
