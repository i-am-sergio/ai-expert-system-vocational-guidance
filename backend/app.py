import os
from dotenv import load_dotenv
import controller as ctrl

load_dotenv()
puerto = os.getenv("PORT", 5000)

if __name__ == '__main__':
    app = ctrl.create_app()
    app.run(debug=True, host='0.0.0.0', port=int(puerto))
