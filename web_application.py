import os

# A simple web application using Flask
from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    host_name = os.uname()[1]  # Get the host name
    ip_address = os.popen('hostname -I').read().strip()  # Get the IP address
    author = os.getenv('AUTHOR', 'Unknown')  # Get the author from environment variable
    return f"Welcome to the Simple Web Application!\nHost Name: {host_name}\nIP Address: {ip_address}\nAuthor: {author}"

# Define a route for a JSON response
@app.route('/api/data')
def get_data():
    data = {'message': 'Hello, World!', 'status': 'success'}
    return jsonify(data)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)