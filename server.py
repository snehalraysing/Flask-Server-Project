from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)




