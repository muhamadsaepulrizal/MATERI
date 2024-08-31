// // DOM selection
// // document.getElementById()
// const judul = document.getElementById('judul'); //tampung ke variabel
// judul.style.color = 'red'; //ubah warna tulisan
// judul.style.backgroundColor = 'orange'; //ubah warna backgrounr
// judul.innerHTML = 'bambang'; //bisa merubah tanpa menyentuh html

// // document.getElementsByTagName()
// let p = document.getElementsByTagName('p');
// console.log(p);
// // for (let i = 0; i < p.length; i++) {
//   // p[i].style.backgroundColor = 'blue';
// // }

// for (const warna of p) {
//   warna.style.backgroundColor = 'blue';
// }

// const h1 = document.getElementsByTagName('h1')[0];
// h1.style.fontSize = '100px';

// // document.getElementsByClassName()
// const p1 = document.getElementsByClassName('p1');
// p1[0].style.fontSize = '50px';
// p1[0].innerHTML = 'diubah di js';

// // document.querySelector(), menghasilkan element
// const p4 = document.querySelector('#b p');
// p4.style.color = 'green';
// p4.style.fontSize = '30px';

// const li2 = document.querySelector('section#b ul li:nth-child(2)');
// li2.style.backgroundColor = 'red';

// // document.querySelectorAll()
// const p = document.querySelectorAll('p');
// // p[2].innerHTML = 'ini diubah di js';
// for (const warnap of p) {
//   warnap.style.color = 'green';
// }

// // mengubah node root, root yg asalnya document, diperkcil jadi sectionB
// const sectionB = document.getElementById('b');
// const p4 = sectionB.querySelector('p');
// p4.style.backgroundColor = 'blue';
