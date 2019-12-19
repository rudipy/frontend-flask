import requests
from flask import Flask, render_template

app = Flask(__name__)
API_URL = 'http://localhost:8000/api/v1'

@app.route('/')
def index():
    jobs = requests.get(f'{API_URL}/job/')
    jobs = jobs.json()
    return render_template('index.html', jobs=jobs)