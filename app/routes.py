from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Medhat'}
    posts = [
        {
            'author':{'username': 'Saad'},
            'body':'Beautiful day in Egypt!'        
        },
        {
            'author':{'username':'Medo'},
            'body':'A famouse comedy film.'
        }
    ]
    return render_template('index.html', title='Home', user=user,posts=posts)
    
