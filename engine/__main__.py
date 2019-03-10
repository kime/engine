import os

from engine.views import engine
from flask import Flask

app = Flask(__name__)
app.register_blueprint(engine)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3785))
    app.run(host='0.0.0.0', port=port)
