const new_element = '<li>Item</li>';

$('document').ready(() => {
  $('#add_item').click(() => {
    $('UL.my_list').append(new_element);
  });
});
