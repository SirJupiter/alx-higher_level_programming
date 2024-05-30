$('document').ready(() => {
  let state = false;
  $('#toggle_header').click(() => {
    if (!state) {
      $('header').addClass('red').removeClass('green');
      state = true;
    } else {
      $('header').addClass('green').removeClass('red');
      state = false;
    }
  });
});


// $('document').ready(() => {
//   $('#toggle_header').click(() => {
//     $('header').toggleClass('red green');

//   });
// });
