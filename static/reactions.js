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
  console.log(evt.target.parentNode);
  console.log(evt.target.parentNode.parentNode.id);

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


    const formInput = {likes_val : $(evt.target).val(), image_session : $(evt.target.parentNode.parentNode.id).val()};
    
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

// let imagePath = $('#image_path').html(`${res.user_id}`);
  // console.log(imagePath) 








// Follow Button:
$('.follow-button').on('click', (evt) => {
  const btn = evt.target;
  console.log(evt.target)

  if (btn.innerText === 'Follow') {
    btn.innerText = 'Unfollow';
    console.log(btn.innerText)
  } else {
    btn.disabled = true;
    console.log(btn.innerText)
  }
  

  const formInput = {follows : $(evt.target).val()};

  $.get('/follow/feed.json', formInput, (res) => {
      alert('sent to server')
      
  });
});













