import sqlite3

preguntas = {
    "Social": [
        "¿Te sientes a gusto trabajando en equipos colaborativos?",
        "¿Disfrutas ayudando a otros a resolver sus problemas personales?",
        "¿Prefieres trabajos que te permitan interactuar frecuentemente con personas?",
        "¿Te consideras una persona empática y sensible a las necesidades de los demás?",
        "¿Te interesa participar en actividades comunitarias o de voluntariado?",
        "¿Disfrutas trabajar en entornos donde puedas establecer relaciones interpersonales cercanas?",
        "¿Te sientes satisfecho/a cuando puedes hacer una diferencia positiva en la vida de otras personas?",
        "¿Prefieres trabajos que impliquen enseñar, asesorar o guiar a otros?",
        "¿Te gusta organizar eventos sociales o actividades grupales?",
        "¿Te sientes cómodo/a manejando situaciones emocionales difíciles?"
    ],
    "Artistic": [
        "¿Te gusta expresarte a través de formas artísticas como el dibujo, la pintura o la escultura?",
        "¿Disfrutas explorando nuevas ideas creativas y expresiones artísticas?",
        "¿Prefieres trabajos que involucren diseño gráfico, moda o decoración?",
        "¿Te sientes inspirado/a por la música, el teatro o la literatura?",
        "¿Disfrutas la creación de contenido visual o multimedia?",
        "¿Te gusta improvisar o experimentar con nuevas técnicas artísticas?",
        "¿Prefieres trabajar en entornos donde la creatividad sea valorada y promovida?",
        "¿Te sientes atraído/a por carreras que permitan desarrollar tu talento artístico?",
        "¿Disfrutas visitando museos, galerías de arte o asistiendo a eventos culturales?",
        "¿Te interesa explorar cómo el arte y la creatividad pueden impactar positivamente en la sociedad?"
    ],
    "Realistic": [
        "¿Te gusta trabajar con tus manos para construir, reparar o mejorar cosas?",
        "¿Disfrutas de actividades al aire libre o trabajos que requieran habilidades físicas?",
        "¿Prefieres trabajar en entornos donde puedas utilizar herramientas o maquinaria?",
        "¿Te sientes atraído/a por carreras en campos como la carpintería, la mecánica o la construcción?",
        "¿Disfrutas resolver problemas prácticos mediante el razonamiento lógico y la experimentación?",
        "¿Te sientes a gusto trabajando en entornos físicamente demandantes?",
        "¿Prefieres trabajos que te permitan ver resultados tangibles de tu trabajo?",
        "¿Te gusta explorar cómo funcionan las cosas y cómo pueden mejorarse?",
        "¿Disfrutas participar en actividades deportivas o recreativas que requieran habilidades físicas?",
        "¿Te interesa aprender sobre tecnología y su aplicación práctica en diferentes campos?"
    ],
    "Enterprising": [
        "¿Te consideras una persona ambiciosa y orientada a alcanzar metas específicas?",
        "¿Disfrutas asumiendo roles de liderazgo y tomando decisiones estratégicas?",
        "¿Prefieres trabajos que te permitan influir en otros y persuadir para alcanzar objetivos comunes?",
        "¿Te sientes atraído/a por carreras en ventas, marketing o gestión empresarial?",
        "¿Disfrutas identificando oportunidades de negocio y desarrollando nuevas iniciativas?",
        "¿Prefieres trabajar en entornos dinámicos y competitivos?",
        "¿Te gusta negociar y buscar soluciones creativas para resolver problemas?",
        "¿Te sientes cómodo/a tomando riesgos calculados en busca de recompensas?",
        "¿Disfrutas estableciendo redes profesionales y colaborando en proyectos de alto impacto?",
        "¿Te interesa aprender sobre estrategias financieras y de mercado para el crecimiento empresarial?"
    ],
    "Investigative": [
        "¿Te gusta analizar datos y encontrar patrones o tendencias significativas?",
        "¿Disfrutas resolver problemas complejos utilizando métodos científicos o técnicos?",
        "¿Prefieres trabajos que requieran investigar y descubrir nuevos conocimientos?",
        "¿Te sientes atraído/a por carreras en ciencias, tecnología, ingeniería o matemáticas (STEM)?",
        "¿Disfrutas la exploración intelectual y la resolución de problemas teóricos?",
        "¿Prefieres trabajar en entornos donde se valore la innovación y la investigación continua?",
        "¿Te gusta desarrollar hipótesis y probar nuevas ideas a través de experimentos?",
        "¿Te sientes cómodo/a usando herramientas y tecnologías avanzadas para analizar información?",
        "¿Disfrutas aprender sobre teorías científicas o conceptos complejos y aplicarlos en situaciones prácticas?",
        "¿Te interesa explorar cómo la ciencia y la investigación pueden impactar en el progreso de la sociedad?"
    ],
    "Conventional": [
        "¿Te sientes cómodo/a siguiendo instrucciones detalladas y trabajando con procedimientos establecidos?",
        "¿Disfrutas organizar información, datos o documentos de manera sistemática?",
        "¿Prefieres trabajos que requieran precisión y atención al detalle?",
        "¿Te sientes atraído/a por carreras en contabilidad, administración, o tecnología de la información?",
        "¿Disfrutas aplicando normas y regulaciones en tu trabajo diario?",
        "¿Prefieres trabajar en entornos donde se valore la organización y la eficiencia operativa?",
        "¿Te gusta analizar información financiera o administrativa para tomar decisiones informadas?",
        "¿Te sientes cómodo/a trabajando con software especializado para gestionar datos o procesos?",
        "¿Disfrutas cumpliendo plazos y trabajando en proyectos estructurados paso a paso?",
        "¿Te interesa aprender sobre sistemas y procedimientos que optimicen la eficiencia organizacional?"
    ]
}

careers = {
    #SOCIAL — Helping, Instructing, Caregiving
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
    ],
    #ARTISTIC — Creating or Enjoying Art, Drama, Music, Writing
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
    ],
    #REALISTIC — Building, Repairing, Working Outdoors
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
    ],
    #ENTERPRISING — Selling, Managing, Persuading
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
    ],
    #INVESTIGATIVE — Researching, Analyzing, Inquiring
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
    ],
    #CONVENTIONAL — Accounting, Organizing, Processing Data
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

