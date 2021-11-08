from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()



#####3
counter = open('counter.txt', 'r')
lines = counter.readlines()
print(lines)
oldcount = lines[-1]
newcount = int(oldcount)+ 1
counter.close()


counter2 = open('counter.txt', 'w')
counter2.write(str(newcount))
counter2.close()
############