// gets JSON data and parses it for a specific value.

$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index) {
    $('ul#list_movies').append('<li>' + data.results[index].title + '</li>');
  });
});
