from flask import Flask, render_template, request

app = Flask(__name__)

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        post = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        }
        posts.append(post)
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
