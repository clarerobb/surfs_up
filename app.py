from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world"

temperature=int(input("what is the temperature outside?"))
if temperature>80:
    print("Turn on the AC.")
else:
    print("Open the windows.")