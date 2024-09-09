from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = '2bc077a9f6fe5f00241d146278207061'  # Replace this with your actual API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
        response = requests.get(url)
        print(response.json())  # Print the API response for debugging purposes
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error_message = "City not found. Please check the city name and try again."
    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
