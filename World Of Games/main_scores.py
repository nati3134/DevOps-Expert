from flask import Flask
from utils import SCORES_FILE_NAME



app = Flask(__name__)


def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        return f'{e.args[1]}: {e.filename}\n'


@app.route('/')
def index():
    return score_server()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')