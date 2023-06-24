from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! This is version 1'
    
if __name__ == "__main__":
    app.run(host='13.232.56.25', port=5000)