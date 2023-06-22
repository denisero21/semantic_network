from db_connection import connection
from questions import check_questions
from open_theory import open_pdf

if __name__ == "__main__":
    cursor = connection.cursor()
    current_user_node = 1  # В будущем подтянуть из бд

    while True:
        open_pdf(cursor, current_user_node)
        if check_questions(cursor, current_user_node):
            current_user_node += 1

    cursor.close()
    connection.close()
