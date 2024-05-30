const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$('document').ready(() => {
  $.get(url, (response) => {
    console.log(response.hello);
    $('#hello').text(response.hello);
  });
});
