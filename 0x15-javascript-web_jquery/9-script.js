// gets JSON data and parses it for a specific value.

$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div#hello').text(data.hello);
  });
});
