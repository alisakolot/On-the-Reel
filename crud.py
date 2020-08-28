"""CRUD operations."""

from model import db, User, Video, Image, Following, Reaction, connect_to_db

import os
import sample_users
from flask import Flask


# os.system('createdb alisadb2')


def create_user(first_name, last_name, username, email, password):
    """Create new user."""

    user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
   
    db.session.add(user)
    db.session.commit()

    return user


#users::users
#ratings::reacts
#movies::videos



def create_video(video_path, description, date_posted):
    """Create new video (info)."""

    video = Video(video_path=video_path, description=description, date_posted=date_posted)

    db.session.add(video)
    db.session.commit()

    return video

def create_image(image_path, description, user_id):
    """Create new video (info)."""
    #BRING BACK DATE_POSTED
    #ADD USER ID

    image = Image(image_path=image_path, description=description, user_id=user_id)

    db.session.add(image)
    db.session.commit()

    return image

#TEST NO USER ID 

# def create_image(image_path, description):
#     """Create new video (info)."""
#     #BRING BACK DATE_POSTED
#     #ADD USER ID

#     image = Image(image_path=image_path, description=description)

#     db.session.add(image)
#     db.session.commit()

#     return image



#//////////////////////////Codependent Relationships////////////////////////////


def create_reaction(user, reaction, video=None, image=None):
    """Keep track of reactions."""

    #Take user, video classes and add reaction(random int) to the database
    
    reaction = Reaction(user=user, video=video, image=image, reaction=reaction)

    #This will go into the 'reaction' table
    db.session.add(reaction)
    db.session.commit()

    return reaction


def create_following(subscriber, creator):
    """Create/document subscriber/creator relationships."""

    #Take subscriber_id (user_id) and creator_id (user_id) and add both to database
    following = Following(subscriber=subscriber, creator=creator)

    #This will go into the 'following' table
    db.session.add(following)
    db.session.commit()


    return following



#///////////////////////////////////// Get User Profile Info/////////////////////////

def get_users():
    """Return all users."""

    return User.query.all()

def get_username(username):
    """Return username."""
    # import pdb; pdb.set_trace()
    return User.query.filter_by(username = username).first()

def get_password(password):
    """Return password."""
    # import pdb; pdb.set_trace()
    return User.query.filter_by(User.password == password).first()
    #specify user password 

def get_firstname(first_name):
    """Return first name."""

    return User.query.filter(User.first_name == first_name).all()

def get_lastname(last_name):
    """Return last name."""

    return User.query.filter(User.last_name == last_name).all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()



#///////////////////////////////////// Get Video Info/////////////////////////

def get_videos():
    """Return all videos."""

    return Video.query.all()


def get_video_by_id(video_id):
    """Return a video by primary key."""

    return Video.query.get(video_id)




#///////////////////////////////////// Get Image Info/////////////////////////

def get_images():
    """Return all images."""

    return Image.query.all()

def get_images_by_path(image_path):
    """Return all image paths/urls."""
     
    return Image.query.filter_by(Image.image_path == image_path).all()


def get_image_by_id(image_id):
    """Return a image by primary key."""

    return Image.query.get(image_id)

def get_image_by_id_path(image_id, image_path):
    """Return tuples of image id and image path."""

    return Image.query(image_id, image_path).all()

def get_image_by_user_id(user_id):
    """Return user id corresponding to image id."""

    return Image.query.filter_by(user_id).first()
    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
