from flask import Flask
import subprocess
import os
import ftplib
from flask import request
from waitress import serve

app = Flask(__name__)

def run_cmd(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/cmdinj/<cmd>')
def main(cmd):
	return run_cmd(cmd)

@app.route('/pyevalinj/<cmd>')
def pyevalinj(cmd):
	return str(eval(cmd))

@app.route('/<text>')
def xss(text):
	if text != null:
		return "Nice try, " + text
	else:
		return "Bet ya can't break me!"

@app.route('/sql/<cmd>')
def sqli(cmd):
	query = "DELETE FROM foo WHERE id = '%s'" % cmd
	return "No sqli here :)"
serve(app, port=8081, host='192.168.201.204')
