$(document).ready(function () {
  // Send an AJAX request to the URL to fetch the character data
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // Update the text content of the character div element with the character name
      $('div#character').text(data.name);
    },
    error: function (xhr, status, error) {
      console.log('Error:', error);
    }
  });
});
