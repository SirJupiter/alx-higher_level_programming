const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$('document').ready(() => {
  $.get(url, (response) => {
    for (const value of Object.values(response.results)) {
      console.log(value.title);
      const movieTitle = `<li>${value.title}</li>`;
      $('#list_movies').append(movieTitle);
    }
  });
});
