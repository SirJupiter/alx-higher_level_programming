
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$('document').ready(() => {
  $.get(url, (response) => {
    console.log(response);
    const characterName = response.name;
    $('#character').text(characterName);
  });
});

// $(document).ready(function () {
//   $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
//     $('DIV#character').text(data.name);
//   });
// });