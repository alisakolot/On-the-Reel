"""Models for video uploading app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    #subscribers(all the people who follow the creator, displays with user_id. displayed with a list of users)
    #creators(all the people who the subscriber follows, displays with user_id, displayed with list of users)



    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username} first_name={self.first_name} last_name={self.last_name} email={self.email} password={self.password}>'



class Video(db.Model):
    """User's Video."""

    __tablename__ = 'video'

    video_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    video_path = db.Column(db.String)
    description = db.Column(db.Text)
    date_posted = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Video video_id={self.video_id} video_path={self.video_path} description={self.description} date_posted={self.date_posted}>'



class Image(db.Model):
    """User's Image."""

    __tablename__ = 'image'

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    image_path = db.Column(db.String)
    description = db.Column(db.Text)
    date_posted = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Image image_id={self.image_id} image_file={self.image_file} description={self.description} date_posted={self.date_posted}>'


class Reaction(db.Model):
    """User Reactions to Video."""

    __tablename__ = 'reaction'

    reaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #number

    reaction = db.Column(db.Integer) #similar to rating, to be mapped to different emojis

    #Reaction by user to video
    video_id = db.Column(db.Integer, db.ForeignKey('video.video_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    #describing relationships between video/user to reaction
    video = db.relationship('Video', foreign_keys = video_id, backref="reactions")
    user = db.relationship('User', foreign_keys = user_id, backref="reactions") 


    #Reaction by user to images
    image_id = db.Column(db.Integer, db.ForeignKey('image.image_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    #describing relationships between image/user to reaction
    image = db.relationship('Image', foreign_keys = image_id, backref="reactions")
    user = db.relationship('User', foreign_keys = user_id, backref="reactions") 


    
    def __repr__(self):
        return f'<Reaction reaction_id={self.reaction_id} video_id={self.video_id} image_id={self.image_id} user_id={self.user_id}>'



class Following(db.Model):
    """Following: relationships between users."""

    __tablename__ = 'following'


    following_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    subscriber_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    #describing relationships between creator and subscribers
    creator = db.relationship('User', foreign_keys = creator_id, backref='subscribers')
    subscriber = db.relationship('User', foreign_keys= subscriber_id, backref='creators')



    def __repr__(self):
        return f'<Following subscriber_id={self.subscriber_id} creator_id={self.creator_id}>'


def connect_to_db(flask_app, db_uri='postgresql:///alisadb', echo=True):
    #alisadb corresponds to database that will exist, how you are connecting to database 

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    connect_to_db(app)



