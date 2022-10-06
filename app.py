from flask import Flask
import os
from flask import request
from waitress import serve

app = Flask(__name__)

def run_cmd(cmd):
	return str(cmd)

@app.route('/cmdinj/<cmd>')
def main(cmd):
	return run_cmd(cmd)

@app.route('/pyevalinj/<cmd>')
def pyevalinj(cmd):
	return str(cmd)

@app.route('/<text>')
def xss(text = None):
	if text != None:
		return "Nice try, " + text
	else:
		return "Bet ya can't break me!"

serve(app, port=23001, host='172.17.0.2')
