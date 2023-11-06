from app import app, db
from models import User


@app.route('/')
def index():
    query = db.session.query(User).all()
    return query if query else 'epmty'


@app.route('/add')
def add():
    u = User(username='user_1', email='email_1')
    db.session.add(u)
    db.session.commit()
    return f'add {u.id}'


if __name__ == '__main__':
    app.run(debug=True)
