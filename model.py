"""Models for app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    fname = db.Column(db.String, nullable=False)
    rpg_class = db.Column(db.String, nullable=False)
    rpg_ability = db.Column(db.String, nullable=False)
    total_score = db.Column(db.Integer)
    level = db.Column(db.Integer)

    tasks = db.relationship("Task", back_populates="users")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>' 
    
class Task(db.Model):
    __tablename__ = "tasks"

    task_id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)

    users = db.relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<Task task_id={self.task_id} user_id={self.user_id}>"


def connect_to_db(flask_app, db_uri="postgresql:///productivity", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app, echo=False) 