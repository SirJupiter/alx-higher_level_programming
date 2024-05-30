
// document.addEventListener('DOMContentLoaded', () => {
//   const addItem = document.querySelector('#add_item');
//   const removeItem = document.querySelector('#remove_item');
//   const clearList = document.querySelector('#clear_list');
//   const myList = document.querySelector('UL.my_list');

//   addItem.addEventListener('click', () => {
//     const newItem = document.createElement('li');
//     newItem.textContent = 'Item';
//     myList.appendChild(newItem);
//   });

//   removeItem.addEventListener('click', () => {
//     if (myList.lastElementChild) {
//       myList.removeChild(myList.lastElementChild);
//     }
//   });

//   clearList.addEventListener('click', () => {
//     while (myList.lastElementChild) {
//       myList.removeChild(myList.lastElementChild);
//     }
//   });
// });

$(document).ready(function () {
  // Add item
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  // Remove item
  $('DIV#remove_item').click(function () {
    $('UL.my_list LI:last-child').remove();
  });

  // Clear list
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
