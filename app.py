# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    time = request.form['time']
    return f"Appointment booked for {name} at {time}. Confirmation sent to {email}."

if __name__ == '__main__':
    app.run(debug=True)


