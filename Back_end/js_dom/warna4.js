const tUbahWarna = document.querySelector('#tUbahWarna');
tUbahWarna.addEventListener('click', function () {
  //   document.body.style.backgroundColor = 'blue';
  document.body.classList.toggle('biru-muda');
});

const tAcakWarna = document.createElement('button');
const teksAcakWarna = document.createTextNode('acak Warna');
tAcakWarna.appendChild(teksAcakWarna);
tAcakWarna.setAttribute('type', 'button');

// simpan elemen setelah elemen yg diinginkan dengan method after
tUbahWarna.after(tAcakWarna);

tAcakWarna.addEventListener('click', function () {
  // membuat warna random untuk red, green, & blue
  // cara supaya method random hasil angkanya bulat dengan method round antara 1 - 255
  const r = Math.round(Math.random() * 255 + 1);
  const g = Math.round(Math.random() * 255 + 1);
  const b = Math.round(Math.random() * 255 + 1);

  document.body.style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
});

//permainan slider
const sMerah = document.querySelector('input[name=sMerah]');
const sHijau = document.querySelector('input[name=sHijau]');
const sBiru = document.querySelector('input[name=sBiru]');
//change hanya merubah saat dilepas, input merubah realtime saat disentuh
sMerah.addEventListener('input', function () {
  //value u mengambil nilai min & max di html-nya
  const r = sMerah.value;
  const g = sHijau.value;
  const b = sBiru.value;
  document.body.style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
});
sHijau.addEventListener('input', function () {
  //value u mengambil nilai min & max di html-nya
  const r = sMerah.value;
  const g = sHijau.value;
  const b = sBiru.value;
  document.body.style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
});
sBiru.addEventListener('input', function () {
  //value u mengambil nilai min & max di html-nya
  const r = sMerah.value;
  const g = sHijau.value;
  const b = sBiru.value;
  document.body.style.backgroundColor = 'rgb(' + r + ',' + g + ',' + b + ')';
});

//bermain warna dengan koordinat posisi mouse
const mouse = document.body;
mouse.addEventListener('mousemove', function (event) {
  // posisi mouse dengan method clientX u tahu koordinat sumbu x
  // console.log(event.clientX);
  //ukuran browser
  //lebar document
  // console.log(window.innerWidth);
  const posX = Math.round((event.clientX / window.innerWidth) * 255);
  const posY = Math.round((event.clientY / window.innerHeight) * 255);
  document.body.style.backgroundColor = 'rgb(' + posX + ',' + posY + ',100)';
});
