"""Server for Video/Image app."""

from flask import (Flask, render_template, request, flash, session,
                redirect)
from model import connect_to_db
import crud

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
    

    print(db_user)

    if username != db_user.username: 
        flash('Incorrect username/password, please try again.')
    else:
        print('/login_user', f'/profile/{db_user.user_id}' )
        return redirect(f'/profile/{db_user.user_id}')




#////////////////////////////////////////////////////Profile//////////////////////////////////////////////////

@app.route('/profile', methods=['GET']) 
def display_user():
    """Display User Profile."""
    

    return render_template('profile.html')



@app.route('/profile/<user_id>')
def show_user(user_id):
    """Show details on a particular user."""
    print('in profile route user_id =', user_id)

    user = crud.get_user_by_id(user_id)
    
    return render_template('profile.html', user=user)

@app.route('/profile/<user_id>')
def upload_images():
    """Upload images."""
    image = request.files.get("media-file")
    user_id = session.get('user_id')

    if image:
        image_url = api.upload_image(image)
        image_name = request.form.get("submit-media")
        new_image = crud.create_image(user_id, image_name, image_url)
    
    album = api.view_album()
    
    return render_template('/profile/upload_file.php', image_url=image_url, album=album)

@app.route('/profile/upload_file.php')
def upload_image_to_profile():
    """Upload images."""
    
    album = api.view_album()
    
    return redirect('/profile/', image_url=image_url, album=album)





#

#////////////////////////////////////////////////////Feed//////////////////////////////////////////////////


#////////////////////////////////////////////////////Videos//////////////////////////////////////////////////
#TO BE SEEN IN PROFILE
@app.route('/feed')
def all_videos():
    """View all videos."""

    videos = crud.get_videos()
    print(videos)

    return render_template('/feed.html', videos=videos)


# @app.route('/feed/<video_id>')
# def show_video(video_id):
#     """Show details on a particular video."""

#     video = crud.get_video_by_id(video_id)

#     return render_template('/profile.html', video=video)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)