import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import joblib
import data as ct

# Definir categorías como antecedentes
categories = {
    'Realistic': ctrl.Antecedent(np.arange(0, 11, 1), 'Realistic'),
    'Investigative': ctrl.Antecedent(np.arange(0, 11, 1), 'Investigative'),
    'Artistic': ctrl.Antecedent(np.arange(0, 11, 1), 'Artistic'),
    'Social': ctrl.Antecedent(np.arange(0, 11, 1), 'Social'),
    'Enterprising': ctrl.Antecedent(np.arange(0, 11, 1), 'Enterprising'),
    'Conventional': ctrl.Antecedent(np.arange(0, 11, 1), 'Conventional')
}

# Definir funciones de membresía para las categorías
for category in categories.values():
    category['low'] = fuzz.trimf(category.universe, [0, 0, 5])
    category['medium'] = fuzz.trimf(category.universe, [0, 5, 10])
    category['high'] = fuzz.trimf(category.universe, [5, 10, 10])

# Definir carreras como consecuentes
careers = {career: ctrl.Consequent(np.arange(0, 11, 1), career) for career in ct.career_data.keys()}

# Definir funciones de membresía para las carreras
for career in careers.values():
    career['low'] = fuzz.trimf(career.universe, [0, 0, 5])
    career['medium'] = fuzz.trimf(career.universe, [0, 5, 10])
    career['high'] = fuzz.trimf(career.universe, [5, 10, 10])

# Crear las reglas difusas
rules = []

def create_rule(category_name, level, career_name):
    antecedent = categories[category_name][level]
    consequent = careers[career_name][level]
    return ctrl.Rule(antecedent, consequent)

for career, categories_list in ct.career_data.items():
    for category in categories_list:
        for level in ['low', 'medium', 'high']:
            rules.append(create_rule(category, level, career))

# Crear el sistema de control difuso
career_ctrl = ctrl.ControlSystem(rules)

# Guardar la lógica difusa preentrenada en un archivo
joblib.dump(career_ctrl, 'career_recommendation_system.pkl')

print("Lógica difusa preentrenada guardada en 'career_recommendation_system.pkl'")
