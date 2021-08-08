from flask import render_template,request,redirect,url_for
from ..request import get_article,get_source
from . import main
from ..models import Source,Article

# Views
@main.route('/')
def index():
    source = get_source('source')
    return render_template('index.html', source=source)

@main.route('/articles/<id>')
def article(id):
    article = get_article(id)
    title = f'{id}'

    return render_template('article.html', id = id, article= article)