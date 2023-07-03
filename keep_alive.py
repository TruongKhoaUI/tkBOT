from flask import Flask, render_template
from threading import Thread
import logging
import sys
import os

# Disable all texts in keep_alive.py
logging.getLogger('werkzeug').setLevel(logging.ERROR)
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

template_dir = os.path.abspath('/home/runner/tkBOT')
app = Flask(__name__, template_folder=template_dir)

# Show the webview
@app.route('/')
def home():
  return render_template('index.html')

# Port run
def run():
  app.run(host='0.0.0.0',port=8080)

# Start the thread
def keep_alive():
  t = Thread(target=run)
  t.start()