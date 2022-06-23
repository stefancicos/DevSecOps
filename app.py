from flask import Flask
from flask import request
from waitress import serve

app = Flask(__name__)
@app.route('/', methods=['GET'])
def main():
	cmd = request.args
	return cmd
serve(app, port=8081, host='0.0.0.0')
