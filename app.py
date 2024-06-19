# /mnt/data/app.py

import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = '2bc077a9f6fe5f00241d146278207061'  # Replace with your actual API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error_message = 'City not found!'
    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
