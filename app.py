from flask import Flask
import subprocess
import ftplib
from flask import request
from waitress import serve

app = Flask(__name__)

def run_cmd(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/cmdinj/<cmd>')
def main(cmd):
	number = 9
	return str(run_cmd(cmd))+"<hr>"+str(exec("number*number"))+"<hr>"+str(eval("number + number"))

@app.route('/pyinj/<cmd>')
def pyinf(cmd):

serve(app, port=8081, host='0.0.0.0')
