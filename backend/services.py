from flask import Flask, request, jsonify
from flask_cors import CORS
import db.extract_db as db
import os
from dotenv import load_dotenv
import db.user_db as user_db
import db.extract_db as db

def haz_diagnostico(conocido, conocimiento):
    explicacion_diagnostico = []
    for diagnosis, sintomas in conocimiento.items():
        if prueba_presencia_de(conocido, sintomas):
            explicacion_diagnostico = [sintoma[1] for sintoma in sintomas if prueba_verdad_de(sintoma[1], conocido)]
            return diagnosis, explicacion_diagnostico
    return None, []

def prueba_presencia_de(conocido, lista_de_sintomas):
    for sintoma in lista_de_sintomas:
        if not prueba_verdad_de(sintoma[1], conocido):
            return False
    return True

def prueba_verdad_de(sintoma, conocido):
    return sintoma in conocido

def siguiente_sintoma(conocido, conocimiento):
    for diagnosis, sintomas in conocimiento.items():
        for sintoma in sintomas:
            if sintoma[1] not in conocido and 'no ' + sintoma[1] not in conocido:
                return sintoma[1]
    return None

def obtener_pregunta(current_symptom, diagnostico_actual, conocido, conocimiento):
    if diagnostico_actual:
        return {'diagnostico': diagnostico_actual, 'explicacion': []}
    if current_symptom is None:
        current_symptom = siguiente_sintoma(conocido, conocimiento)
    if current_symptom is not None:
        return {'pregunta': f'Es verdad que {current_symptom}?', 'current_symptom': current_symptom}
    else:
        diagnostico_actual, explicacion_diagnostico = haz_diagnostico(conocido, conocimiento)
        if diagnostico_actual:
            return {'diagnostico': diagnostico_actual, 'explicacion': explicacion_diagnostico}
        return {'diagnostico': 'No hay suficiente conocimiento para elaborar un diagnostico.', 'explicacion': []}

def procesar_respuesta(data, current_symptom, diagnostico_actual, conocido, conocimiento):
    if 'respuesta' not in data:
        return {'error': 'Respuesta no proporcionada'}, current_symptom, diagnostico_actual, conocido
    
    respuesta = data['respuesta'].strip().lower()
    if respuesta not in ['si', 'no']:
        return {'error': 'Respuesta inválida'}, current_symptom, diagnostico_actual, conocido

    if respuesta == 'si':
        conocido.append(current_symptom)
    elif respuesta == 'no':
        conocido.append('no ' + current_symptom)

    diagnostico_actual, _ = haz_diagnostico(conocido, conocimiento)
    if diagnostico_actual:
        return {'diagnostico': diagnostico_actual, 'explicacion': []}, current_symptom, diagnostico_actual, conocido

    current_symptom = siguiente_sintoma(conocido, conocimiento)
    if current_symptom is None:
        diagnostico_actual, explicacion_diagnostico = haz_diagnostico(conocido, conocimiento)
        if diagnostico_actual:
            return {'diagnostico': diagnostico_actual, 'explicacion': explicacion_diagnostico}, current_symptom, diagnostico_actual, conocido
        return {'diagnostico': 'No hay suficiente conocimiento para elaborar un diagnostico.', 'explicacion': []}, current_symptom, diagnostico_actual, conocido
    
    return {'pregunta': f'Es verdad que {current_symptom}?'} , current_symptom, diagnostico_actual, conocido

def extraer_datos():
    return db.extraer_datos()

def obtener_nombres_tablas():
    return db.obtener_nombres_tablas()
