// // Event Handler
// const p3 = document.querySelector('.p3');

// function ubahWarna() {
//   p2.style.backgroundColor = 'lightblue';
// }

// const p2 = document.querySelector('.p2');
// p2.onclick = ubahWarna;

// // addEventListener()
// const p4 = document.querySelector('section#b p');
// p4.addEventListener('click', function () {
//   const ul = document.querySelector('section#b ul');
//   const liBaru = document.createElement('li');
//   const teksLiBaru = document.createTextNode('item baru');
//   liBaru.appendChild(teksLiBaru);
//   ul.appendChild(liBaru);
// });

// perbedaan
const p3 = document.querySelector('.p3');
// // Event Handler
// p3.onclick = function () {
//   p3.style.backgroundColor = 'lightblue';
// };
// p3.onclick = function () {
//   p3.style.color = 'red';
// };

// // addEventListener()
p3.addEventListener('dblclick', function () {
  p3.style.backgroundColor = 'lightblue';
  p3.style.color = 'red';
  p3.style.fontSize = '50px';
});
// p3.addEventListener('click', function () {
//   p3.style.color = 'red';
// });
