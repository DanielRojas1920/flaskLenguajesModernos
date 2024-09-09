import sys
from connection import MySQLConnection

path = 'C:\\Users\\Danny Rojo\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\Scripts'

sys.path.append(path)

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


notes = []
connection = MySQLConnection( #Le quité mis datos
    host= "localhost",
    user="Username",
    password="Password",
    database = "database"
)


@app.route('/')
def hello_world():
    return render_template("index.html", notes = notes)

@app.route('/DeleteNote', methods = ['POST'])
def delete_note():
    global notes
    index = request.form['noteid']

    connection.connect()

    connection.delete('agendanotes', index)

    notes = []
    for value in connection.select('agendanotes'):
        notes.append(value)

    connection.disconnect()

    return redirect('/')

@app.route('/UpdateNotePage', methods=['POST'])
def update_note_page():
    global notes
    index = int(request.form['noteid'])
    aux_note = None
    for note in notes:
        if (note[0] == index):

            aux_note = list(note)
            break

    print(aux_note)

    return render_template("updateNote.html", note = aux_note)

@app.route('/UpdateNotePage/Update', methods=['POST'])
def update_note():
    global notes

    title = request.form['textbox1']
    date = request.form['fecha']
    details = request.form['details']
    id = request.form['noteid']
    date = '-'.join(date.split('/')[::-1])
    insert_values = [[title, '%s'], [date, '%s'], [details, '%s']]

    connection.connect()
    connection.update('agendanotes', id ,insert_values)
    
    notes = []

    for value in connection.select('agendanotes'):
        notes.append(value)

    connection.disconnect()



    return redirect('/')





@app.route('/NewNote', methods=['POST'])
def new_note():
    global notes

    title = request.form['textbox1']
    date = request.form['fecha']
    details = request.form['details']
    date = '-'.join(date.split('/')[::-1])
    insert_values = [[title, '%s'], [date, '%s'], [details, '%s']]

    connection.connect()
    connection.insert('agendanotes', insert_values)
    notes = []

    for value in connection.select('agendanotes'):
        notes.append(value)

    connection.disconnect()


    return redirect('/')

 
if __name__ == '__main__':
    connection.connect()

    for value in connection.select('agendanotes'):
        notes.append(value)

    connection.disconnect()
    
    app.run()