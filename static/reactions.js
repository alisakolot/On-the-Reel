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

$('.likes').on('click', (evt) => {
  const btn = evt.target;
  console.log(evt.target)

  if (btn.innerText === 'Like') {
    btn.innerText = 'Dislike';
    console.log(btn.innerText)
  } else {
    // btn.innerText = 'Like';
    btn.disabled = true;
    console.log(btn.innerText)
  }

  if (btn.innerText === ':)') {
    btn.innerText = ':)';
    console.log(btn.innerText)
  } else {
    btn.disabled = true;
    console.log(btn.innerText)
  }

  if (btn.innerText === 'xD') {
    btn.innerText = 'xD';
    console.log(btn.innerText)
  } else {
    btn.disabled = true;
    console.log(btn.innerText)
  }

  if (btn.innerText === ':/') {
    btn.innerText = ':/';
    console.log(btn.innerText)
  } else {
    btn.disabled = true;
    console.log(btn.innerText)
  }

  if (btn.innerText === ':C') {
    btn.innerText = ':C';
    console.log(btn.innerText)
  } else {
    btn.disabled = true;
    console.log(btn.innerText)
  }

    const formInput = {likes_val : $(evt.target).val()};

  $.get('/feed.json', formInput, (res) => {
        alert('sent to server')
  
  });

});

//get image id









// Follow Button:
$('.follow-button').on('click', (evt) => {
  const btn = evt.target;
  console.log(evt.target)

  if (btn.innerText === 'Follow') {
    btn.innerText = 'Unfollow';
    console.log(btn.innerText)
  } else {
    // btn.innerText = 'Like';
    btn.disabled = true;
    console.log(btn.innerText)
  }
  const formInput = {likes_val : $(evt.target).val()};

  $.get('/follow/feed.json', formInput, (res) => {
        alert('sent to server')
  
  });

});


// 









