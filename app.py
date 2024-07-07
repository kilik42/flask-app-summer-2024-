#imports
from flask import Flask, render_template, request, redirect, url_for
from flask_scss import Scss  # pip install Flask-Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# my app

app = Flask(__name__)
Scss(app, static_dir='static', asset_dir='assets')

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# db model
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    complete = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)
    
# routes
@app.route('/posts')
def posts():
    return render_template('posts.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)