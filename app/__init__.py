from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    title = "New API App"
    para = "It is working for now"
    return render_template('index.html', temp_title=title, temp_para = para)



