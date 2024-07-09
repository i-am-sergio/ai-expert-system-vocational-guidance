import sqlite3
import joblib
from skfuzzy import control as ctrl
import db.data as ct

# Initialize a global dictionary to store user answers
user_answers = {category: 0 for category in ["Realistic", "Artistic", "Investigative", "Social", "Enterprising", "Conventional"]}
current_question_index = 0
questions = []
stored_recommendations = None

def initialize_questions(db_file):
    global questions
    questions = []  # Reset questions list
    categories = ["Realistic", "Artistic", "Investigative", "Social", "Enterprising", "Conventional"]
    for category in categories:
        category_questions = get_questions_by_category(db_file, category)
        questions.extend([(question[0], question[1], category) for question in category_questions])

def get_questions_by_category(db_file, category):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    table_name = category.lower()
    c.execute(f'''SELECT id, question FROM {table_name}''')
    questions = c.fetchall()
    conn.close()
    return questions

def get_current_question():
    global current_question_index, questions
    if current_question_index < len(questions):
        question = questions[current_question_index]
        return {"question": question[1]}
    else:
        recommendations = prediction(user_answers)
        return {"message": "All questions answered", "recommendations": recommendations, "user": user_answers}

def post_answer(answer):
    global current_question_index, user_answers
    answer = answer.lower()
    if answer == "si":
        category = questions[current_question_index][2]  # The category is stored in the third position of the tuple
        user_answers[category] += 1
    current_question_index += 1
    if current_question_index < len(questions):
        next_question = questions[current_question_index]
        return {"question": next_question[1], "user": user_answers}
    else:
        recommendations = prediction(user_answers)
        return {"message": "All questions answered", "recommendations": recommendations,"user": user_answers}

def restart_diagnosis():
    global user_answers, current_question_index, questions, stored_recommendations
    user_answers = {category: 0 for category in ["Realistic", "Artistic", "Investigative", "Social", "Enterprising", "Conventional"]}
    current_question_index = 0
    questions = []
    stored_recommendations = None
    return {"message": "Diagnosis restarted"}

def get_course():
    careers = list(ct.career_data.keys())
    return {"careers": careers}

def prediction(user_answers):
    global stored_recommendations
    
    if stored_recommendations is not None:
        return stored_recommendations
    
    career_ctrl = joblib.load('career_recommendation_system.pkl')
    career_simulation = ctrl.ControlSystemSimulation(career_ctrl)
    for category, answer in user_answers.items():
        career_simulation.input[category] = answer
    career_simulation.compute()
    recommendations = {career: career_simulation.output[career] for career in ct.career_data.keys()}
    sorted_recommendations = sorted(recommendations.items(), key=lambda item: item[1], reverse=True)
    return sorted_recommendations
