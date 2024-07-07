import sqlite3
import data as ct

def create_questions_database(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    for category, question_list in ct.preguntas.items():
        table_name = category.lower()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT)''')
        for question in question_list:
            c.execute(f'''INSERT INTO {table_name} (question) VALUES (?)''', (question,))
    conn.commit()
    conn.close()
    print(f"Database '{db_file}' created successfully with categorized tables.")
create_questions_database('questions.db')
