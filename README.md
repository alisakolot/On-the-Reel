## On the Reel

'On the Reel' is a social media inspired web app showcasing the best features of Instagram and Facebook. 
The app implements a media uploading feature on each user's profile as well as a dropdown menu displaying the 
user's followers. The backend is built with SQLAlchemy, Postgresql, and Python. Front end features are constructed with Javascript and JQuery, 
styling in HTML/CSS. 

The web app features a Feed page where each user can view all public content and react to it using the 
reaction button toolbar. Each card on the feed features the user's content and a 
and subscriber and view to a user's profile. 

The minimal viable product goals of the project was to create an app that would allow users to have a personal profile 
and display media to their page as well as the feed. 

In the future the app will implement a chat feature that would allow users to message each other. 

## About Me

Alisa Kolot is a composer and musician turned software engineer. Her interest in technology began when she contributed audio to Harvard’s Library Innovation Lab's immersive audio-visual environment, Alterspace. At Alterspace was inspired by the accessibility of the user interfaces that lended agency to the patron, allowing them to manipulate their own immersive audio-visual environment. This sparked her interest in creating 'On the Real,' an web application that facilitates user interaction. In the future she looks forward to making music and visual art more accessible by using touchless technology. 


## <a name="tech-stack"></a>Technologies
* Python
* Flask
* Jinja2
* PostgresQL
* SQLAlchemy ORM
* HTML
* CSS
* Bootstrap
* jQuery
* Cloudinary

## <a name="installation"></a>Installation
To run On the Reel:

Install PostgresQL (Mac OSX)

Clone or fork this repo:
```
https://github.com/alisakolot/HB-Project
```

Create and activate a virtual environment inside your On the Reel directory:
```
virtualenv env
source env/bin/activate
```

Install the dependencies:
```
pip install -r requirements.txt
```

Sign up to use the [Cloudinary API](https://cloudinary.com/)

Save your API keys in a file called <kbd>secrets.sh</kbd> using this format:

```
export CLOUDINARY_API_KEY="YOUR_KEY_HERE"
export SECRET_KEY="YOUR_SECRET_KEY_HERE"
```

Set up and download your Cloudinary API and save to file called <kbd>secrets.sh</kbd>.

Source your keys from your secrets.sh file into your virtual environment:

```
source secrets.sh
```

Set up the database:

```
createdb mediadb
python3 model.py
python3 seed.py
```

Run the app:

```
python3 server.py
```


## <a name="features"></a>Features

#### Homepage

Users can register or login. 

<img width="776" alt="homepage" src="https://user-images.githubusercontent.com/68030340/93289910-27f12100-f7a5-11ea-9b42-39a7194aeb78.png">

Uses modular forms for both login and creating an account. 

![login](https://user-images.githubusercontent.com/68030340/93289860-0859f880-f7a5-11ea-81a3-e2ed0c3f6e92.gif)


#### Profile Page
Users can upload their media using the 'Upload Memories!' button. Supported formats: .jpg, .gif

![upload](https://user-images.githubusercontent.com/68030340/93290149-b1a0ee80-f7a5-11ea-88cd-17f2edf0c1c4.gif)

Users can see their followers

![subscribers](https://user-images.githubusercontent.com/68030340/93289978-4b1bd080-f7a5-11ea-9a0f-369420db91e8.gif)





#### Feed
Users can view uploads on Feed and react react with emoji buttons as well as subscribe/unsubscribe from each other's channels. Users can navigate to each other's accounts. 

![feed](https://user-images.githubusercontent.com/68030340/93290035-6edf1680-f7a5-11ea-8668-d2c3152f6c08.gif)









