from model import db, User, Video, Image, Following, Reaction, connect_to_db
from datetime import datetime

# #users::users
# #ratings::reactions
# #movies::videos


# #Users
s = User(username="Suzie", email="email", password="password", bio="Suzie's bio")
c = User(username="Cheese", email="eeemail", password="pppassword", bio = "Cheese's bio")
j = User(username="Jasmine", email="email1", password="password1", bio = "Jasmine's bio")



# #Videos

v1 = Video(video_path="path string1", description= "abcd", date_posted=datetime.now())
v2 =  Video(video_path="pathstring2", description = "efgh", date_posted=datetime.now())

v = [v1, v2]

# Images

i1 = Image(image_path="path string1", description= "ABCD", date_posted=datetime.now(), user=s)
i2 =  Image(image_path="pathstring2", description = "EFGH", date_posted=datetime.now(), user=c)

# i = [i1, i2]

# #Reactions
# r1 = Reaction(video=v1, user=s)
# r2 = Reaction(video=v2, user=j)

# #Follows
# f = Following(subscriber=s, creator=c)

# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)

#     import os
#     os.system('dropdb alisadb')
#     os.system('createdb alisadb')

#     db.create_all()

#     s = User(username="Suzie", email="email", password="password")
#     c = User(username="Cheese", email="eeemail", password="pppassword")

#     f = Following(subscriber=s, creator=c)

#     v = Video(video_file="path string", description= "abcd", date_posted=datetime.now())

#     r = Reaction(video=v, user=s)

    
#     db.session.add(s,c)
#     db.session.add(f,v)
#     db.session.add(r)

#     db.session.commit()

'''In order to run seed_database.py this needs to be a 
sample file containing video information only. 
Other info such as users, following, reactions, is created by 
seed_database.py.'''