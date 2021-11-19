from flask import Flask, render_template, request, redirect
from datetime import *

app = Flask(__name__)

notes = []
@app.route('/notes')
def hello():
  return render_template('notes.html', name='guest', notes=notes)

@app.route('/notes/new', methods=['GET'])
def show_create_note_form():
  return render_template('add_note.html', name='guest', notes=notes)

@app.route('/notes/new', methods=['POST'])
def add_note():
  time = datetime.now()
  notes.append({'name': request.form['fio'], 'heading':request.form['heading'], 'time': time, 'text': request.form['note']})   #с ссылкой - так?
  return redirect('/notes')


@app.route('/note/<int:note_index>', methods=['GET', 'POST'])    
def see_note(note_index):   
  bigtext = notes[note_index]
  return render_template('see_note.html', note_index = note_index, text = bigtext['text'], heading = bigtext['heading'], author = bigtext['name'], time = bigtext['time'])


@app.route('/note/<int:note_index>/delete', methods=['GET', 'POST'])
def delete_note(note_index):
  notes.pop(note_index)
  return redirect('/notes')


app.run()


