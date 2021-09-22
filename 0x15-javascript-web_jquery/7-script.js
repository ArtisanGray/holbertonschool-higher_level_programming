// gets JSON data and parses it for a specific value.

$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
