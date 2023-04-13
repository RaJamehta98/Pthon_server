from flask import Flask
app = Flask(’FinTechExplained WebServer’)

@app.route(’/’)
def get_data():
    return "hello world"
