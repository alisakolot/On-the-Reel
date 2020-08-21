"""Server for Video/Image app."""

from flask import (Flask, render_template, request, flash, session,
                redirect)
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
        return redirect(f'/profile/{db_user.user_id}')




#////////////////////////////////////////////////////Profile/user-id/////////////////////////////////////////



@app.route('/profile/<user_id>')
def show_user(user_id):
    """Show details on a particular user."""
    print('in profile route user_id =', user_id)

    user = crud.get_user_by_id(user_id)
    
    return render_template('profile.html', user=user)


#Sending Photos to cloudinary - DONT TOUCH THIS CODE. ##########################
@app.route('/profile/<user_id>', methods=['POST'])
def upload_images(user_id):
    """Upload images to cloudinary."""

    image = request.files.get("file")
    
    if image:
        image_path = cloudinary_image_api.upload_image(image)

        #image link/path going into description
        # image_name = request.form.get("submit-media")
        
        description = request.form.get("user-description")

        # user = crud.get_user_by_id(user_id)
        # user = user_id


        new_image = crud.create_image(image_path, description)
    
    return redirect('/feed') #<= THIS IS A TEST. WE NEED IT TO REDIRECT TO THE PROFILE PAGE WITH MORE PHOTOS


# ###################### DONT TOUCH THIS CODE ###################################

# Display images to user on page
# @app.route('/profile/<username>')
#make a loop for user image in profile.html




#////////////////////////////////////////////////////Feed//////////////////////////////////////////////////

#Images to be displayed in feed
@app.route('/feed')
def all_image_urls():
    """View all images in feed."""

    images = crud.get_images()
    image_urls =  []


    for image in images: 
        image_urls.append(image.image_path)
        

    return render_template('feed.html', image_urls=image_urls)



#////////////////////////////////////////////////////Videos//////////////////////////////////////////////////
#TO BE SEEN IN PROFILE
# @app.route('/feed')
# def all_videos():
#     """View all videos."""

#     videos = crud.get_videos()
#     print(videos)

#     return render_template('/feed.html', videos=videos)


# @app.route('/feed/<video_id>')
# def show_video(video_id):
#     """Show details on a particular video."""

#     video = crud.get_video_by_id(video_id)

#     return render_template('/profile.html', video=video)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)