import subprocess


def open_pdf(cursor, current_user_node):
    cursor.execute(f"SELECT * FROM nodes WHERE id={current_user_node}")
    node = cursor.fetchall()
    subprocess.run(['start', '', node[0][2]], shell=True)

