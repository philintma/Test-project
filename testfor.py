from flask import Flask, render_template

app = Flask(__name__)
users = ['Аня', 'Ваня', 'Толя']
@app.route('/')
def hello():
  return render_template('for.html', users=users)
