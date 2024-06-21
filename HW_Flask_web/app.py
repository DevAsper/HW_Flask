from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog/')
def blog():
    images = ['georgia.jpeg', 'kaliningrad.jpeg', 'spain.jpeg']
    return render_template('blog.html', images=images)

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
