import numpy as np
import skfuzzy as fuzz

# Definición de funciones de membresía difusa
x = np.arange(0, 1.01, 0.01)
low = fuzz.trimf(x, [0, 0.3, 0.5])
medium = fuzz.trimf(x, [0.3, 0.5, 0.7])
high = fuzz.trimf(x, [0.5, 1, 1])

# Ejemplo de puntuaciones del usuario
scores = {
    "Social": 1.0,
    "Artistic": 0.4,
    "Realistic": 0.3,
    "Enterprising": 0.2,
    "Investigative": 0.7,
    "Conventional": 0.1
}

# Definición de carreras según intereses y habilidades
careers = {
    "Social": {
        "Special Education Teacher": [
            "Social",
            "Enterprising",
            "Artistic"
        ],
        "Occupational Therapist": [
            "Social",
            "Artistic"
        ],
        "Community Service Director": [
            "Social"
        ],
        "Instructional Coordinator": [
            "Social"
        ],
        "Secondary School Teacher": [
            "Social"
        ],
        "Registered Nurse": [
            "Social",
            "Artistic",
            "Investigative"
        ]
    },
    "Artistic": {
        "Arts/Entertainment Manager": [
            "Artistic"
        ],
        "Art Teacher": [
            "Artistic",
            "Social"
        ],
        "Editor": [
            "Artistic"
        ],
        "Photographer": [
            "Artistic",
            "Realistic",
            "Enterprising"
        ]
    },
    "Realistic": {
        "Engineer": [
            "Realistic",
            "Investigative"
        ],
        "Computer & IS Manager": [
            "Realistic",
            "Conventional"
        ],
        "Horticulturist": [
            "Realistic",
            "Enterprising",
            "Investigative"
        ],
        "Management Analyst": [
            "Realistic",
            "Enterprising",
            "Conventional"
        ],
        "Technical Support Specialist": [
            "Realistic",
            "Investigative",
            "Conventional"
        ]
    },
    "Enterprising": {
        "Facilities Manager": [
            "Enterprising",
            "Conventional",
            "Social"
        ],
        "Flight Attendant": [
            "Enterprising",
            "Social",
            "Artistic"
        ],
        "Bartender": [
            "Enterprising",
            "Artistic",
            "Realistic"
        ],
        "Purchasing Agent": [
            "Enterprising",
            "Realistic",
            "Conventional"
        ],
        "Cosmetologist": [
            "Enterprising",
            "Artistic"
        ]
    },
    "Investigative": {
        "Chiropractor": [
            "Investigative",
            "Social",
            "Artistic"
        ],
        "Pharmacist": [
            "Investigative",
            "Conventional",
            "Enterprising"
        ],
        "Psychologist": [
            "Investigative",
            "Artistic",
            "Social"
        ],
        "University Faculty Member": [
            "Investigative"
        ],
        "Respiratory Therapist": [
            "Investigative",
            "Realistic",
            "Social"
        ]
    },
    "Conventional": {
        "Nursing Home Administrator": [
            "Conventional",
            "Enterprising",
            "Social"
        ],
        "Administrative Assistant": [
            "Conventional",
            "Social",
            "Realistic"
        ],
        "Customer Service Representative": [
            "Conventional",
            "Realistic"
        ],
        "Paralegal": [
            "Conventional",
            "Artistic"
        ],
        "Food Service Manager": [
            "Conventional",
            "Enterprising",
            "Social"
        ],
        "Business/Finance Supervisor": [
            "Conventional",
            "Realistic",
            "Enterprising"
        ]
    }
}

# Calcular grados de pertenencia difusa
membership = {}
for category in scores:
    membership[category] = {
        "Low": fuzz.interp_membership(x, low, scores[category]),
        "Medium": fuzz.interp_membership(x, medium, scores[category]),
        "High": fuzz.interp_membership(x, high, scores[category])
    }

# Definir carreras recomendadas basadas en pertenencia difusa
recommended_careers = {}
for category in membership:
    for career in careers[category]:
        career_score = 0
        for level in ["Low", "Medium", "High"]:
            if level == "Low":
                continue  # Ignorar niveles "Low"
            if level in careers[category][career]:
                career_score += membership[category][level]
        if career_score > 0:  # Solo considerar carreras con al menos algún nivel de pertenencia
            if career not in recommended_careers:
                recommended_careers[career] = 0
            recommended_careers[career] += career_score

# Ordenar carreras por su idoneidad
sorted_careers = sorted(recommended_careers.items(), key=lambda item: item[1], reverse=True)

# Mostrar las mejores carreras recomendadas
print("Carreras recomendadas:")
for career, score in sorted_careers[:3]:  # Mostrar las 3 mejores carreras
    print(f"- {career} (Score: {score})")
