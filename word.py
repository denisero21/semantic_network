import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import networkx as nx
import matplotlib.pyplot as plt


def extract_triples(text):
    # Разбиваем текст на предложения
    sentences = sent_tokenize(text)

    triples = []

    for sentence in sentences:
        # Токенизируем предложение на слова
        words = word_tokenize(sentence)

        # Используем библиотеку NLTK для определения частей речи
        pos_tags = nltk.pos_tag(words)

        # Создаем триады "Субъект-Предикат-Объект"
        for i in range(len(pos_tags) - 2):
            subject = pos_tags[i][0]
            predicate = pos_tags[i + 1][0]
            obj = pos_tags[i + 2][0]
            triple = (subject, predicate, obj)
            triples.append(triple)

    return triples


def visualize_triples(triples):
    # Создаем пустой граф
    G = nx.DiGraph()

    for triple in triples:
        subject, predicate, obj = triple

        # Добавляем узлы (субъекты и объекты) в граф
        G.add_node(subject)
        G.add_node(obj)

        # Добавляем ребро с предикатом между субъектом и объектом
        G.add_edge(subject, obj, label=predicate)

    # Определяем позиции узлов для визуализации
    pos = nx.spring_layout(G)

    # Рисуем узлы
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)

    # Рисуем ребра с подписями
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos)

    # Рисуем метки узлов
    nx.draw_networkx_labels(G, pos)

    # Показываем граф
    plt.axis('off')
    plt.show()


def generate_questions(triples):
    questions = []

    for triple in triples:
        subject, predicate, obj = triple

        # Генерируем вопросы, используя шаблоны
        question_who = f"Кто {predicate} {obj}?"
        question_what = f"Что {predicate} {obj}?"
        question_where = f"Где {predicate} {obj}?"

        # Добавляем сгенерированные вопросы в список
        questions.extend([question_who, question_what, question_where])

    return questions


def is_valid_question(question):
    # Реализуйте правила или анализатор для определения корректности вопроса
    # Верните True, если вопрос является корректным, и False в противном случае
    # Можете использовать регулярные выражения, NLP или другие методы

    # Пример правила: вопрос должен начинаться со слова "Кто", "Что" или "Где"
    valid_start_words = ["Кто", "Что", "Где"]
    start_word = question.split()[0]
    if start_word not in valid_start_words:
        return False

    # Добавьте дополнительные правила для корректности вопросов

    return True


def correct_question(question):
    # Реализуйте правила или замены для коррекции некорректного вопроса
    # Можете использовать правила замены или другие методы

    # Пример правила: заменить некорректное начало вопроса на "Кто"
    invalid_start_words = ["Когда", "Почему"]
    start_word = question.split()[0]
    if start_word in invalid_start_words:
        question = "Кто" + question[len(start_word):]

    # Добавьте дополнительные правила для коррекции вопросов

    return question


# Пример использования
text = "Я ем яблоко. Она пишет письмо. Мальчик бросает мяч. Иди в лес за дровами."
triples = extract_triples(text)

visualize_triples(triples)
questions = generate_questions(triples)

for question in questions:
    if is_valid_question(question):
        print(question)
    else:
        print(f"Некорректный вопрос: {question}")
        corrected_question = input("Введите корректный вопрос: ")

        while not is_valid_question(corrected_question):
            print("Некорректный вопрос. Попробуйте еще раз.")
            corrected_question = input("Введите корректный вопрос: ")

        print(f"Скорректированный вопрос: {corrected_question}")


