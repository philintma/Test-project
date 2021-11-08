#form
from flask import Flask, render_template, request

app = Flask(__name__)

code = []
# @app.route('/')
# def hello():
#   return render_template('form.html', name='guest')

@app.route('/checked', methods=['POST'])



def show_checked():
    code.append(request.form['code'])
    #синтаксический валидатор




    skobki = {'[':']', '{':'}', '(':')', '<':'>'}
    stack = []
    stackplaces = []
    codeparts = []

    for line in code:
        for symbol in line: #для каждого отдельного символа
            l = code.index(line)
            s = line.index(symbol)

            if str(symbol) in skobki.keys():
                stack.append(symbol)
                stackplaces.append([[l][s]])    #так?

            elif symbol in skobki.values() and len(stack)>0:   
                if skobki[stack[-1]] == symbol: #если это та самая закрывающая скобка 

                    stack.pop()
                    stackplaces.pop()
                    codeparts.append(code[stackplaces[-1]:[l][s]]) #от  индекса откр скобки до индекса закр скобки - здесь правильно? нельзя ли обойтись только s?
                    
               
#мы просто вносим большие части кода, потом красим от самой большой до самой мал части? 

    return codeparts #render_template('checked.html', code=code)

#пока не сделано с ошибочным кодом