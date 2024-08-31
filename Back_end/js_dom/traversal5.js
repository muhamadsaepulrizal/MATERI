//js Event Hilang
// const card = document.querySelector('.card');
// const close = document.querySelector('.close');
// close.addEventListener('click', function () {
//   card.style.display = 'none';
// });

// //dom traversal
// const close = document.querySelectorAll('.close');
// //pakai for
// // const card = document.querySelectorAll('.card');
// // for (let i = 0; i < close.length; i++) {
// //   close[i].addEventListener('click', function (e) {
// //     // close[i].parentElement.style.display = 'none';
// //     e.target.parentElement.style.display = 'none';
// //   });
// // }

// //pakai forEach, parentElement untuk meneulisuri
// close.forEach(function (el) {
//   el.addEventListener('click', function (e) {
//     e.target.parentElement.style.display = 'none';
//     e.preventDefault();
//     e.stopPropagation();
//   });
// });

// const cards = document.querySelectorAll('.card');
// cards.forEach(function (card) {
//   card.addEventListener('click', function (e) {
//     alert('ok');
//   });
// });

// // //card pertama, ambil nama
// // const namaCard1 = document.querySelector('.nama');

//// cara lain supaya bisa di edit instan/realtime di browser
const container = document.querySelector('.container');
container.addEventListener('click', function (e) {
  if (e.target.className == 'close') {
    e.target.parentElement.style.display = 'none';
    e.preventDefault();
  }
});
