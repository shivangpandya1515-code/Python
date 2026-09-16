from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def form():
    return render_template('form.html')

@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    course = request.form.get('course')
    return render_template('result.html', name=name, email=email, course=course)

@app.route('/', methods = ['GET'])
def search():
    query  = request.args.get('query','')
    return f"<h3>You searched for: {query}</h3>"

if __name__ == '__main__':
    app.run(debug=True)