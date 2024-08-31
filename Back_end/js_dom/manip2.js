// Dom Manipulation

// // manipulasi element
// // element.innerHTML
// const judul = document.getElementById('judul');
// judul.innerHTML = '<i>rizal judul</i>';

// const sectionA = document.querySelector('section#a');
// sectionA.innerHTML = '<h1>hallo A</h1>';

// // element.style.<property css>
// const judul = document.querySelector('#judul');
// judul.style.color = 'red';

// // atttribute
// const judul = document.getElementsByTagName('h1')[0];
// judul.setAttribute('name', 'rizal');

// const a = document.querySelector('section#a a');
// a.setAttribute('id', 'link');

// const p2 = document.querySelector('.p2');
// p2.setAttribute('class', 'label');
//
//
//
//
//
// //manipulasi node
// buat element baru
const pBaru = document.createElement('p');
const teksPBaru = document.createTextNode('paragraf baru');
// simpan tulisan ke dapam p
pBaru.appendChild(teksPBaru);
// simpan pBaru di akhir section a
const sectionA = document.querySelector('section#a');
sectionA.appendChild(pBaru);

// contoh lain
// buat element baru
const liBaru = document.createElement('li');
// buat tulisan dalam li
const teksLiBaru = document.createTextNode('item baru');
// simpan tulisan ke li
liBaru.appendChild(teksLiBaru);
// simpan setelah item 1 sebeleum li ke 2 dibawah ul
// caranya cari posisi parent dan elemen setelahnya
const ul = document.querySelector('section#b ul');
const li2 = ul.querySelector('li:nth-child(2)');
ul.insertBefore(liBaru, li2);

// remove
// sectionA sudah ditangkap diatas
// tangkap element yg ingin dihapus
const link = sectionA.querySelector('a');
sectionA.removeChild(link);

// replace / mengganti
// tangkap el parent-nya
const sectionB = document.querySelector('section#b');
// tangkap yg ingin diganti
const p4 = sectionB.querySelector('p');
// buat el baru-nya dan teks-nya
const h2Baru = document.createElement('h2');
const teksH2Baru = document.createTextNode('Judul Baru');
h2Baru.appendChild(teksH2Baru);
// lakukan replacenya
sectionB.replaceChild(h2Baru, p4);

// style u element yg baru
pBaru.style.backgroundColor = 'red';
liBaru.style.backgroundColor = 'red';
h2Baru.style.backgroundColor = 'red';
