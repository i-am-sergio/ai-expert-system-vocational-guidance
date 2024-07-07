import joblib
from skfuzzy import control as ctrl
import data as ct

def prediction(user_answers):
    career_ctrl = joblib.load('career_recommendation_system.pkl')
    career_simulation = ctrl.ControlSystemSimulation(career_ctrl)
    for category, answer in user_answers.items():
        career_simulation.input[category] = answer
    career_simulation.compute()
    recommendations = {career: career_simulation.output[career] for career in ct.career_data.keys()}
    sorted_recommendations = sorted(recommendations.items(), key=lambda item: item[1], reverse=True)
    return sorted_recommendations

"""
# Test the function
user_answers = {
    'Realistic': 4,
    'Investigative': 1,
    'Artistic': 10,
    'Social': 8,
    'Enterprising': 6,
    'Conventional': 8
}
print(prediction(user_answers))
"""