const text = "New Header!!!";

$('document').ready(() => {
  $('#update_header').click(() => {
    $('header').text(text);
  });
});
