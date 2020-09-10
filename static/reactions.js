"use strict";

$(document).ready(() => {


  //Reactions/Like buttons: 

  $('.reaction-button').on('click', (evt) => {
    let btn = evt.target;
    let imageId = btn.parentNode.parentNode.parentNode.id;
    console.log(imageId);
    console.log(typeof imageId);

      btn.disabled = true;
      console.log(btn.innerHTML)

      const formInput = {likes_val : $(evt.target).val(), image_session : imageId};
        console.log(formInput)

    $.get('/feed.json', formInput, (res) => {
          alert('sent to server')
    
    });

  });




  //Get Image Id

  $('.image-id').on('click', (evt) => {
    const btn = evt.target;

    const formInput = {image_id : $(evt.target).val()};
    console.log(btn)
      
    $.get('/feed.json', formInput, (res) => {
          alert('sent img id')
    
    });

  });


  //Logout
  console.log("hey we're here")

    console.log("now we're ready")
    $('.logout').on('click', (evt) => {
      const btn = evt.target;
      $.get('/feed', (res) => {
            alert('Logout?');
            window.location = "http://localhost:5000/"
      });
    });




  $('#logout').on('click', (evt) => {
    const btn = evt.target;
    console.log("logging out ")
    $.get('/feed', (res) => {
          alert('Are you sure you want to Logout?');
          window.location = "http://localhost:5000/"
    });

  });
  $('#logout').on('click', (evt) => {
    const btn = evt.target;
    console.log("logging out ")
    $.get('/feed', (res) => {
          alert('Logout?');
          window.location = "http://localhost:5000/login"
    });

  });



  // Follow Button:
  $('.follow-button').on('click', (evt) => {
    evt.preventDefault();
    const btn = evt.target;
    console.log(evt.target)

    const formInput = {creatorId : $(evt.target).val()};

    if (btn.innerText === 'Follow') {
      $.get('/follow/feed.json', formInput, (res) => {
        btn.innerText = 'Unfollow'; 
      });

    } else if (btn.innerText === 'Unfollow') { 
        $.get('/feed/unfollow', formInput, (res) => {
        })
          btn.innerText = 'Follow'; 
          
        
      console.log(btn.innerText)
      console.log(btn.innerText)
    }


  });



})














