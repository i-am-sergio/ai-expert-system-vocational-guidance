import sqlite3

def get_questions_by_category(db_file, category):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    table_name = category.lower()
    c.execute(f'''SELECT id, question FROM {table_name}''')
    questions = c.fetchall()
    conn.close()
    return questions

"""
# Ejemplo de uso:
questions_realistic = get_questions_by_category('questions.db', 'REALISTIC')
print("Preguntas de la categoría REALISTIC:")
for id, question in questions_realistic:
    print(f"{id}. {question}")
"""