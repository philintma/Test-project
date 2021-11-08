counter = 0

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
     global counter
     counter += 1
     return render_template('hello.html', counter=counter)


app.run()





# def hello_world():
#     global counter
#     counter += 1
#     message = f"<p>Hello, World!</p> This page has already been shown {counter} times" 
    
#     return message 

# @app.route('/goodbye')
# def bye():
#     global counter
#     message = f"<p>Go away, World</p> This page can still be shown {10-counter} times" 
    
#     return message 
