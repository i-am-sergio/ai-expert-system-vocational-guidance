from flask import Flask, request, jsonify
from flask_cors import CORS
import db.extract_db as db
import os
from dotenv import load_dotenv
import db.user_db as user_db
import services as sv
from flask import Flask, request, jsonify
from flask_cors import CORS
import services as srv
import os
from dotenv import load_dotenv
import db.user_db as user_db

load_dotenv()
puerto = os.getenv("PORT", 5000)

def create_app():
    app = Flask(__name__)
    CORS(app)
    conocimiento = srv.extraer_datos()
    current_symptom = None
    diagnostico_actual = None
    conocido = []

    @app.route('/pregunta', methods=['GET'])
    def pregunta():
        nonlocal current_symptom, diagnostico_actual, conocido
        result = srv.obtener_pregunta(current_symptom, diagnostico_actual, conocido, conocimiento)
        current_symptom = result.get('current_symptom', None)
        diagnostico_actual = result.get('diagnostico', None)
        return jsonify(result)

    @app.route('/respuesta', methods=['POST'])
    def respuesta():
        nonlocal current_symptom, diagnostico_actual, conocido
        data = request.json
        result, current_symptom, diagnostico_actual, conocido = srv.procesar_respuesta(data, current_symptom, diagnostico_actual, conocido, conocimiento)
        return jsonify(result)
    
    @app.route('/nuevo_diagnostico', methods=['POST'])
    def nuevo_diagnostico_endpoint():
        nonlocal current_symptom, diagnostico_actual, conocido
        current_symptom = None
        diagnostico_actual = None
        conocido = []
        return jsonify({'mensaje': 'Diagnóstico reiniciado. Puede comenzar un nuevo diagnóstico.'})
    
    @app.route('/conocimiento', methods=['GET'])
    def obtener_conocimiento():
        return jsonify(conocimiento)
    
    @app.route('/course', methods=['GET'])
    def nombres_tablas():
        nombres = srv.obtener_nombres_tablas()
        return jsonify(nombres)
    
    @app.route('/register', methods=['POST'])
    def register():
        data = request.json
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Usuario y/o contraseña no proporcionados'}), 400
        username = data['username']
        password = data['password']
        if user_db.register(username, password):
            return jsonify({'mensaje': 'Usuario registrado exitosamente'})
        return jsonify({'error': 'Usuario ya existe'}), 400
    
    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Usuario y/o contraseña no proporcionados'}), 400
        username = data['username']
        password = data['password']
        if user_db.login(username, password):
            return jsonify({'mensaje': 'Inicio de sesión exitoso'})
        return jsonify({'error': 'Usuario y/o contraseña incorrectos'}), 400
    
    @app.route('/')
    def index():
        return "Bienvenido al Sistema Experto. Usa /pregunta para empezar."

    return app


