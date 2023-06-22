import networkx as nx
import matplotlib.pyplot as plt
import openai
import os
from dotenv import load_dotenv
import subprocess

# load_dotenv()
# openai.api_key = os.getenv('API_KEY')

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "Вы: Привет, как дела?"},
#         {"role": "user", "content": "Я: Хорошо, спасибо! Как твои дела?"},
#     ]
# )

# response_text = response['choices'][0]['message']['content']
# print("Модель: " + response_text)






# current_user_node = 1
#
# # Выполнение SQL-запроса
# cursor.execute(f"SELECT * FROM questions WHERE node_id={current_user_node}")
#
# # Получение результатов
# questions = cursor.fetchall()


# for row in rows:
#     print(row)

# Example usage
# pdf_file_path = rows[0][2]
# open_pdf(f'{pdf_file_path}')
























# Создание семантической сети
# semantic_network = nx.DiGraph()
#
#



# q1 = Question('Что такое Python?', ['Выберите верное утверждение'])
# q2 = Question('Типизация в Python?', ['Выберите верное утверждение'])
# q3 = Question('Вы тупой?', ['Выберите верное утверждение'])
#
# # Добавление узлов
# semantic_network.add_node("собака")
# semantic_network.add_node("кошка")
# semantic_network.add_node("птица")
# semantic_network.add_node("denchik")
# semantic_network.add_node("pashok")

# semantic_network.add_node(q1)
# semantic_network.add_node(q2)
# semantic_network.add_node(q3)

# Добавление связей между узлами
# semantic_network.add_edge("собака", "животное", relation="является")
# semantic_network.add_edge("собака", "кошка")
# semantic_network.add_edge("кошка", "собака")
# semantic_network.add_edge("кошка", "животное", relation="является")
# semantic_network.add_edge("птица", "животное", relation="является")
# semantic_network.add_edge("denchik", "pashok", relation="friends")
# semantic_network.add_edge(q1, q2, relation="True")
# semantic_network.add_edge(q1, q3, relation="False")


# # Функция для поиска связей между понятиями
# def find_relations(source, target):
#     if semantic_network.has_edge(source, target):
#         relation = semantic_network[source][target]["relation"]
#         return f"{source} {relation} {target}"
#     else:
#         return "Связь не найдена"


# source_concept = input("Введите исходное понятие: ")
# target_concept = input("Введите целевое понятие: ")
# result = find_relations(source_concept, target_concept)
# print(result)

# Отображение семантической сети
# pos = nx.spring_layout(semantic_network)
# nx.draw(semantic_network, pos, with_labels=True)


# pos = nx.spring_layout(semantic_network)  # Определение позиций узлов
# nx.draw(semantic_network, pos, with_labels=True, node_color='lightblue')  # Отрисовка графа с узлами
# edge_labels = nx.get_edge_attributes(semantic_network, 'relation')  # Получение атрибутов ребер
# nx.draw_networkx_edge_labels(semantic_network, pos, edge_labels=edge_labels)  # Отрисовка меток ребер
#
# plt.show()
