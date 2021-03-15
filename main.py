from flask import Flask, send_from_directory, request
from flask_mobility import Mobility
from flask_talisman import Talisman
import codecs, os

#Threading
from threading import Thread

#WSGIServer
from gevent.pywsgi import WSGIServer

def loadPage(src):
    return codecs.open(src, "r", "utf-8").read()

def run():
	#WSGIServer
	WSGIServer(('', 8081), app).serve_forever()

#Thread
def keep_alive():
	t = Thread(target=run)
	t.start()

app = Flask(__name__)
Mobility(app)
Talisman(app, content_security_policy=None)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')

@app.route('/service-worker.js')
def service_worker():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'service-worker.js',
        mimetype='application/javascript')

@app.route('/script.js')
def scriptjs():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'script.js',
        mimetype='application/javascript')

@app.route('/manifest.json')
def manifest():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'manifest.json',
        mimetype='application/json')

@app.route('/icon-192.png')
def icon192():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'icon-192.png',
        mimetype='image/png')

@app.route('/')
def main():
	return loadPage("static/index.html")

if __name__ == '__main__':
  keep_alive()