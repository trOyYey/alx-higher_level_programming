$(document).ready(() => {
  $('DIV#add_item').on('click', () => {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').on('click', () => {
    $('UL.my_list LI').last().remove();
  });

  $('DIV#clear_list').on('click', () => {
    $('UL.my_list LI').remove();
  });
});
