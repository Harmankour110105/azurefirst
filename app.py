# app.py
from flask import Flask, render_template, request,abort

app = Flask(__name__)
ALLOWED_IPS = ['117.210.169.244']  # or maybe hardcoded IPs

@app.before_request
def limit_remote_addr():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(f"Visitor IP: {ip}")  # debug line
    if ip not in ALLOWED_IPS:
        abort(403)
        
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    time = request.form['time']
    return f"Appointment booked for {name} at {time}. Confirmation sent to {email}."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)


