#автоноски



items = ["n1.jpg", "n2.jpg", "n3.jpg", "n4.jpg", "n5.jpg", "n6.jpg", "n7.jpg", "n8.jpg" ]



from flask import Flask, render_template

app = Flask(__name__)
@app.route("/avtonoski")
def menu():
    global items  #это здесь ни на что не влияет, кажется
    return render_template("noskimenu.html", items = items)
    

