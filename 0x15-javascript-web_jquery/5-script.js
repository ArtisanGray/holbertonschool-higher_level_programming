// appends an item to a list on click

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
