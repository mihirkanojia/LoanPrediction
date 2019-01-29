from flask import Flask
import webbrowser
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ =='__main__':
    url = 'http://127.0.0.1:5000'
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
    app.run()