"""Server for Video/Image app."""

from flask import (Flask, render_template, request, flash, session,
                redirect, jsonify)
from model import connect_to_db
import crud

import cloudinary_image_api

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined






#//////////////////////////////////////////Homepage:Create Profile//////////////////////////////////////////////////
@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/login', methods=['POST']) #methods=['PUT'] <= create, modify
def create_account():
    """Create new user."""
    #information coming from create-account form 
    #make sure that user is New and does not exist in the database
    # import pdb; pdb.set_trace()
    first_name = request.form.get("first-name")
    print(first_name)


    last_name = request.form.get("last-name")
    print(last_name)

    username = request.form.get("username")
    print(username)

    email = request.form.get("email") 
    print(email)

    password = request.form.get("password") 
    print(password)


    user = crud.get_user_by_email(email)
    print(user)

    print('***\n', user)

    if user:
        flash('Cannot create an account with that email. Try again.')
        print('firstname =', first_name, 'lastname =', last_name, 'username =', username, 'password =', password, 'email =', email)
    else:
        crud.create_user(first_name, last_name, username, email, password)
        flash('Account created! Please log in.')

    return redirect('/')


    # display/debug print what you get, when button is clicked
#^^^^^the above is silent/not displayed 


#////////////////////////////////////////////////////Login//////////////////////////////////////////////////  
@app.route('/login', methods=['GET']) 
def display_login():
    """Display Login."""
    

    return render_template('login.html')

@app.route('/login_user', methods=['GET'])
def logging_in_user():
    #the act of login 
    """Redirect to profile."""
    username = request.args.get("username")
    password = request.args.get('password')
    print('username =', username, 'password=', password)
    
    #getting the user object
    db_user = crud.get_username(username)
    
   

    print('******', db_user)

    if db_user is None: 
        flash('Incorrect username/password, please try again.')
        return redirect('/login')
    if db_user.password != password:
        flash('Incorrect username/password, please try again.')
        return redirect('/login')
    else:
        session['user_id'] = db_user.user_id
        return redirect(f'/profile/{db_user.user_id}')




#////////////////////////////////////////////////////Profile/user-id/////////////////////////////////////////



@app.route('/profile/<user_id>')
def show_user(user_id):
    """Show details on a particular user."""
    print('in profile route user_id =', user_id)

    user = crud.get_user_by_id(user_id)

    return render_template('profile.html', user=user)


#Sending Photos to cloudinary 
@app.route('/profile/<user_id>', methods=['POST'])
def upload_images(user_id):
    """Upload images to cloudinary."""

    image = request.files.get("file")
    
    #getting the user id using session
    user_id = session.get('user_id')
    

    if image:
        image_path = cloudinary_image_api.upload_image(image)

        description = request.form.get("user-description")
        print("description:", description)
    
        new_image = crud.create_image(image_path, description, user_id)
    
    return redirect(f'/profile/{user_id}') 
    



#////////////////////////////////////////////////////Feed//////////////////////////////////////////////////

#Images to be displayed in feed
@app.route('/feed')
def all_image_urls():
    """View all images in feed."""

    images = crud.get_images()
    image_urls = []


    for image in images: 
        image_urls.append(image.image_path)
        

    return render_template('feed.html', images=images)

#Send reaction to database
# @app.route('/feed', methods=['GET'])
# def send_reaction():
#     """Send reaction to db."""
    
#     request.args.get("emoji-{{ img.image_id }}")
#     reaction = crud.create_reaction()
    
#     return redirect('feed.html')

#Get reaction value as JSON
# @app.route('/feed.json')
# def get_reaction_value():

    
#     reaction_val = request.args.get("reaction_val")
#     #many values sent to crud 

#     image_id = request.args.get("image_id")

#     #break out reaction_vals into indiv variables that go into crud function

#     print('*************',  reaction_val, '********')
#     print('*************',  image_id, '********')

#     return jsonify({"values" : True })

# @app.route('/feed.json')
# def get_like_value():

#     reaction_val = request.args.get("reaction_val")

#     print('*************',  reaction_val, '********')
    
#     return jsonify({"values" : True })

@app.route('/feed.json', methods=['GET'])
def like_button():
    """Like button."""

    #get user id
    user_id = request.args.get("follows")
    print('*************', user_id, '********')

    #get reaction 1:
    like_button = request.args.get("likes_val")
    print('*************',  like_button, '********')

    #get image id:
    
    # image_id = session.get('image_id')
    # print('*************',  image_id, '********')

    #add to crud
    # reaction = create_reaction(user, reaction=like_button, video=None, image=None)
    
    return jsonify({"likes" : True })


#//////////////////////////////////////////Following/////////////////////////

    
@app.route('/follow/feed.json', methods=['GET'])
def following():
    """Follow button."""


    #get creator id
    user_id = request.args.get("follows")
    print('*************', user_id, '********')

    #get subscriber id 

    #find a way to check if a user is logged in on feed
    #if logged in, then can commit to db
    #else "please log in" msg




    #add to crud: follows

    #create_following(subscriber, creator)
    
    return jsonify({"follows" : True })






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)