from flask import Flask, request, jsonify
from flask_cors import CORS
import services as service
import os
from dotenv import load_dotenv
import db.user_db as user_db

load_dotenv()
puerto = os.getenv("PORT", 5000)

def create_app():
    app = Flask(__name__)
    CORS(app)
    service.initialize_questions('questions.db')

    @app.route('/pregunta', methods=['GET'])
    def get_current_question():
        return handle_get_current_question()

    @app.route('/respuesta', methods=['POST'])
    def post_answer():
        return handle_post_answer()

    @app.route('/nuevo_diagnostico', methods=['POST'])
    def restart_diagnosis():
        return handle_restart_diagnosis()

    @app.route('/register', methods=['POST'])
    def register():
        return handle_register()

    @app.route('/login', methods=['POST'])
    def login():
        return handle_login()

    @app.route('/')
    def index():
        return "Bienvenido al Sistema Experto. Usa /pregunta para empezar."

    return app

def handle_get_current_question():
    try:
        result = service.get_current_question()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handle_post_answer():
    try:
        data = request.json
        answer = data.get("answer", "").lower()
        result = service.post_answer(answer)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handle_restart_diagnosis():
    try:
        result = service.restart_diagnosis()
        service.initialize_questions('questions.db')
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handle_register():
    try:
        data = request.json
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Usuario y/o contraseña no proporcionados'}), 400
        username = data['username']
        password = data['password']
        if user_db.register(username, password):
            return jsonify({'mensaje': 'Usuario registrado exitosamente'})
        return jsonify({'error': 'Usuario ya existe'}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handle_login():
    try:
        data = request.json
        if 'username' not in data or 'password' not in data:
            return jsonify({'error': 'Usuario y/o contraseña no proporcionados'}), 400
        username = data['username']
        password = data['password']
        if user_db.login(username, password):
            return jsonify({'mensaje': 'Inicio de sesión exitoso'})
        return jsonify({'error': 'Usuario y/o contraseña incorrectos'}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


