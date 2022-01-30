from flask import render_template
from app import app
from .request import get_news


# views start here
@app.route('/')
def index():
    title = "News API App"
    newsList = get_news()
    return render_template('index.html', temp_title=title, temp_NewsList=newsList)