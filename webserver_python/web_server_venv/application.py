from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world. This is our new page!'
    
'''@app.route('/name')
def get_name():
    return 'Moses Kalyango are my names'
'''
@app.route('/contact')
def get_contact():
    return 'my phone number is 899231215343'