// updates the class of a element.

$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').toggleClass('green');
  } else {
    $('header').removeClass('green');
    $('header').toggleClass('red');
  }
});
