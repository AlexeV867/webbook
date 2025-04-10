from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Подключение к базе данных
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Создание таблицы при первом запуске
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            location TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    devices = conn.execute('SELECT * FROM devices').fetchall()
    conn.close()
    return render_template('index.html', devices=devices)

@app.route('/add', methods=['POST'])
def add_device():
    name = request.form['name']
    device_type = request.form['type']
    location = request.form['location']
    status = request.form['status']

    conn = get_db_connection()
    conn.execute('INSERT INTO devices (name, type, location, status) VALUES (?, ?, ?, ?)',
                 (name, device_type, location, status))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>/<string:status>')
def update_status(id, status):
    conn = get_db_connection()
    conn.execute('UPDATE devices SET status = ? WHERE id = ?', (status, id))
    conn.commit()
    conn.close()
    return redirect('/')

# Маршрут для удаления устройства
@app.route('/delete/<int:id>')
def delete_device(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM devices WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)