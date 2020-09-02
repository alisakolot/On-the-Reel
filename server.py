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

    #setting the session

 
    if db_user is None: 
        flash('Incorrect username/password, please try again.')
        return redirect('/login')
    if db_user.password != password:
        flash('Incorrect username/password, please try again.')
        return redirect('/login')
    else:
        session['user_id'] = db_user.user_id
        return redirect(f'/profile/{db_user.user_id}/images')



#////////////////////////////////////////////////////Profile/user-id/////////////////////////////////////////



@app.route('/profile/<user_id>')
def show_user(user_id):
    """Show details on a particular user on profile page."""
    print('in profile route user_id =', user_id)

    user = crud.get_user_by_id(user_id)

    return render_template('profile.html', user=user)


#Show user photos in desc order
@app.route('/profile/<user_id>/images')
def profile_image(user_id):
    """Show user's images."""

    user = crud.get_user_by_id(user_id)
    images = crud.get_image_by_user_id(user_id)

    return render_template(f'profile.html', images=images, user=user)


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
    
    return redirect(f'/profile/{user_id}/images') 




 


#Store user bio
# @app.route('/profile/<user_id>/submit', methods=['POST'])
# def submit(user_id):

#     user = crud.get_user_by_id(user_id)
#     session['user_id'] =  user

#     return  redirect(f'/profile/{user_id}')
#     return 'You entered: {}'.format(request.form['text'])



@app.route('/profile/<user_id>', methods=['GET']) 
def display_logout():
    """Display Logout button."""
    
    return redirect('login.html')


#////////////////////////////////////////////////////Feed//////////////////////////////////////////////////

#Images to be displayed in feed
@app.route('/feed')
def all_image_urls():
    """View all images in feed."""

    images = crud.get_images_eager()
    image_urls = []
    # image_id_list = []

    for image in images: 
        image_urls.append(image.image_path)
        # image_id_list.append(image.image_id)
        # image_id_list = sorted(image_id_list, reverse=True)
        
    print(images[1].user.username)
    return render_template('feed.html', images=images)




@app.route('/feed')
def logged_in_user():
    """Information of user browsing feed."""

    #making sure that the user info is in session
    # session['user_id'] = db_user.user_id

    user_id = session['user_id'] #will overwrite the previous session when a new user(info) is in session
    
    print(">>>>>>>>>>>SESSION/USER_ID:", user_id)
    return render_template('feed.html', user_id=user_id)

# @app.route('/feed')
# def show_creator_images():
#     """Show details on a particular user in feed."""
    
#     user_id = session.get('img.user_id')
#     print("CREATORS USER ID:" , user_id, type(user_id))

#     user = crud.get_user_by_id(user_id)

#     return render_template('feed.html', user=user)



@app.route('/feed.json', methods=['GET'])
def like_button():
    """Like button."""

    #get reaction:
    like_button = request.args.get("likes_val")
    reaction = like_button #test
    

    #subscriber/viewer id
    user_id = session['user_id'] #will overwrite the previous session when a new user(info) is in session
    user = crud.get_user_by_id(user_id)
 
    
    #get image id:
    image_id = request.args.get("image_session")
    image = crud.get_image_by_id(int(image_id))
    print('*************',  image_id, image, '********')


    print("REACTION BUTTON:", like_button, int(like_button))
    print('GET IMAGE ID FROM JS:', image,  '********')

    video=None
    #add to crud
    reaction = crud.create_reaction(user, video, image, int(reaction))
    print("REACTION:", reaction)
    return jsonify({"likes" : True })

@app.route('/feed/', methods=['GET']) 
def display_feed_logout():
    """Display Logout button."""
    
    return redirect('login.html')


#//////////////////////////////////////////Following/////////////////////////

    
@app.route('/follow/feed.json', methods=['GET'])
def following():
    """Follow button."""


    #get creator id
    creator_id = request.args.get("follows")
    creator = crud.get_user_by_id(int(creator_id))
    print('CREATOR ID:', creator, '********')


    #get subscriber id 
    subscriber_id = session['user_id'] 
    subscriber = crud.get_user_by_id(int(subscriber_id))
    print('SUBSCRIBER ID:', subscriber, '********')

    #get following relationships from crud
    follow_subscr = crud.get_following_by_subscriber(subscriber_id)
    print("FOLLOW SUBSCR:", follow_subscr)

    #add to crud: follows
    if subscriber_id not in follow_subscr:
        new_following = crud.create_following(subscriber, creator)
        subscriber_id == creator_id
        flash("you already follow this user")
        

    return jsonify({"follows" : True })


#find a way to check if a user is logged in on feed
    #if logged in, then can commit to db
    #else "please log in" msg



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)