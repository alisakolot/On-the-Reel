from flask import (Flask, render_template, request, flash, session, redirect, url_for)
import requests
import os
import crud

import cloudinary
import cloudinary.uploader
import cloudinary.api



app = Flask(__name__)

cloud_name = os.environ["CLOUD_NAME"]
cloudinary_api_key = os.environ["API_KEY"]
cloudinary_api_secret = os.environ["API_SECRET"]

cloudinary.config(
    cloud_name = cloud_name, 
    api_key = cloudinary_api_key, 
    api_secret = cloudinary_api_secret
)



def upload_image(image):
    """Upload image to cloudinary and return url."""
    if image:
        response = cloudinary.uploader.upload(image)
        image_path = response['secure_url']
    
    return image_path

# profile_user_id
#something inside the response secure_url





if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)

