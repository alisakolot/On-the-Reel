"use strict";


// const button = document.getElementsByClassName("reaction-1");

// button.addEventListener('click', () => {
//   alert('Stop clicking me!');
// });

// $('.reaction').on('click', (evt) => {
//   alert("page connected");
//   console.log(evt.target);

//   const element = $(evt.target);
//     console.log(element)


//   const formInput = {reaction_val : $(evt.target).val(),
//     image_id : attribute};


//   $.get('/feed.json', formInput, (res) => {
//     alert('sent to server')
  

//   });
// });



//Reactions/Like buttons: 

$('.reaction-button').on('click', (evt) => {
  const btn = evt.target;
  console.log(evt.target);
  console.log(evt.target.id);
  console.log('text');
  console.log(evt.target.parentNode);
  console.log(evt.target.parentNode.parentNode);

  console.log('');
  let imageId = evt.target.parentNode.parentNode.id;
  console.log(imageId);
  console.log(typeof imageId);

  // if (btn.innerText === 'Like') {
  //   btn.innerText = 'Dislike';
  //   console.log(btn.innerText)
  // } else {
  //   // btn.innerText = 'Like';
  //   btn.disabled = true;
  //   console.log(btn.innerText)
  // }

  // if (btn.innerText === ':)') {
  //   btn.innerText = ':)';
  //   console.log(btn.innerText)
  // } else {
  //   btn.disabled = true;
  //   console.log(btn.innerText)
  // }

  // if (btn.innerText === 'xD') {
  //   btn.innerText = 'xD';
  //   console.log(btn.innerText)
  // } else {
  //   btn.disabled = true;
  //   console.log(btn.innerText)
  // }

  // if (btn.innerText === ':/') {
  //   btn.innerText = ':/';
  //   console.log(btn.innerText)
  // } else {
  //   btn.disabled = true;
  //   console.log(btn.innerText)
  // }

  // if (btn.innerText === ':C') {
  //   btn.innerText = ':C';
  //   console.log(btn.innerText)

  // } else {
    btn.disabled = true;
    console.log(btn.innerText)
  // }


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
    
  $.get('/feed.json', formInput, (res) => {
        alert('sent img id')
  
  });

});


//Logout
$('.logout').on('click', (evt) => {
  const btn = evt.target;
    
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
      alert('you followed user x');

      btn.innerText = 'Unfollow'; 
    });

  } else if (btn.innerText === 'Unfollow') { 
      $.get('/feed/unfollow', formInput, (res) => {
        alert('you unfollowed user x');
      })
        btn.innerText = 'Follow'; 
        
      
    console.log(btn.innerText)
    console.log(btn.innerText)
  }

  // const formInput = {follows : $(evt.target).val()};

  // $.get('/follow/feed.json', formInput, (res) => {
  //     alert('sent to server')
      
  // });
});

//Unfollow
// $('.unfollow-button').on('click', (evt) => {
//   const btn = evt.target;
//   console.log(evt.target)

//   if (btn.innerText === 'Unfollow') {

  
//   } else {
//     btn.disabled = true;
//     alert('Unfollow?');
//       $.get('/feed/unfollow/', (res) => {
//         alert('you unfollowed user x')
//       })

//     console.log(btn.innerText)
//     console.log(btn.innerText)
//   }
  

//   const formInput = {follows : $(evt.target).val()};
//   console.log(formInput)

//   $.get('/feed/unfollow', formInput, (res) => {
//       alert('sent to server')
      
//   });
// });

//Return to Profile
$('.my-profile').on('click', (evt) => {
  const btn = evt.target;
    
  $.get('/feed/profile/', (res) => {
        let userId=user_id
        alert('redirect to profile?');
        window.location = "http://localhost:5000/profile/{{userId}}"
  });

});














