from flask import Flask
from waitress import serve

app = Flask(__name__)
@app.route('/')
def main():
	return 'Main page'
serve(app, port=8081, host='0.0.0.0')
