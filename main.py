from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import MessageForm
from datetime import date

app = Flask("__main__")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///text.db'
app.config['SECRET_KEY'] = '63103453574bccae5541fa05'
db = SQLAlchemy(app)

class Msg(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(length = 20), nullable =False, unique = True)
    main = db.Column(db.String(length = 1500), nullable = False)
    author = db.Column(db.String(length = 20), nullable = False, default = "User")
    date = db.Column(db.Date, default=date.today)
    views = db.Column(db.Integer(), nullable = False, default = 0)


@app.route('/home')
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/post', methods = ['GET', 'POST'])
def post():
    form = MessageForm()
    if form.validate_on_submit():
        form.author.data = form.author.data or "Anonymous"
        msg = Msg(title=form.title.data, main=form.message.data, author=form.author.data)
        db.session.add(msg)
        db.session.commit()
        return redirect('home')
    
    return render_template('post.html', form=form)

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/view')
def view():
    messages = Msg.query.all()
    messages.reverse()
    return render_template('view.html', messages=messages)

@app.route('/story/<int:Msg_id>')
def story(Msg_id):
    msg = db.session.query(Msg).get(Msg_id)
    return render_template('story.html', msg = msg)


if __name__ == "__main__":
    app.run(debug=True)



