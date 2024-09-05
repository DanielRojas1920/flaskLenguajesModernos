import sys
from connection import MySQLConnection

path = 'C:\\Users\\Danny Rojo\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\Scripts'

sys.path.append(path)

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

count = 0
notes = []
connection = MySQLConnection()


@app.route('/')
def hello_world():
    return render_template("index.html", notes = notes)

@app.route('/NewNote', methods=['POST'])
def new_note():
    global count
    value = request.form['textbox1']
    count = count +1
    notes.append((count, value))
    insert_values = [[value, '%s']]
    connection.insert('notes', insert_values)


    return redirect('/')

 
if __name__ == '__main__':
    for value in connection.select('notes'):
        notes.append(value)
        count= value[0]
    app.run()