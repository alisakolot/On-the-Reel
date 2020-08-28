"use strict";


// const button = document.getElementsByClassName("reaction-1");

// button.addEventListener('click', () => {
//   alert('Stop clicking me!');
// });

$('.reaction').on('click', (evt) => {
  alert("page connected");
  console.log(evt.target);

  const element = $(evt.target);
    console.log(element)


  const formInput = {reaction_val : $(evt.target).val(),
    image_id : attribute};


  $.get('/feed.json', formInput, (res) => {
    alert('sent to server')
  
 
  });
});

//get image id






// //GET ALL ELEMENTS IN CLASS: 
// 









