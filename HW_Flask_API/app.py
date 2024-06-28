from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    error_message = None  # Инициализация переменной
    try:
        response = requests.get('https://catfact.ninja/fact')
        response.raise_for_status()
        data = response.json()
        fact = data['fact']
    except requests.exceptions.RequestException as e:
        fact = "Sorry, we couldn't fetch a cat fact at this moment."
        error_message = str(e)
    return render_template('index.html', fact=fact, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
