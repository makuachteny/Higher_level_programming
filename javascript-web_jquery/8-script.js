$(document).ready(function () {
  $.get(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data) {
      $.each(data.results, function (index, movie) {
        const newListItem = $('<li>').text(movie.title);
        $('ul#list_movies').append(newListItem);
      });
    }
  );
});
