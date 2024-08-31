function getPilihanComputer() {
  //menangkap pilihan computer
  const comp = Math.random();
  // membangkitkan bilangan random 0-1
  if (comp < 0.34) return 'gajah';
  if (comp >= 0.34 && comp < 0.67) return 'orang';
  return 'semut'; //pilhan akhir seperti else
}

function getHasilSuit(comp, player) {
  //menentukan rules
  if (player == comp) return 'seri';
  if (player == 'gajah') return comp == 'orang' ? 'Anda menang' : 'Anda KALAH'; //menang jika comp pilih orang
  if (player == 'semut') return comp == 'orang' ? 'Anda kalah' : 'Anda MENANG'; //menang jima comp pilih gajah
  if (player == 'orang') return comp == 'gajah' ? 'Anda kalah' : 'Anda MENANG'; //menang jika comp pilih semut
}
//animasi supaya pilihan comp muter atau kaya mikir hhe
function putarGambar() {
  const imgComp = document.querySelector('.img-komputer');
  const gambar = ['gajah', 'orang', 'semut'];
  let i = 0;
  const wMUlai = new Date().getTime(); //mendapat waktu saat itu
  setInterval(function () {
    //loop waktu sampe 1 detik jika sudah 1 detik hentikan
    if (new Date().getTime() - wMUlai > 1000) {
      clearInterval;
      return;
    }
    imgComp.setAttribute('src', 'img/' + gambar[i++] + '.png');
    if (i == gambar.length) i = 0;
  }, 50); // 50 adalah waktu intervar 0,05 detik
}

//dengan looping supaya lebih ringkas dari yang manual dibawah pGajah,orang,semut diganti dengan i untuk setiap elemen dlm loop
const pilihan = document.querySelectorAll('li img');
//i u parameter looping dari setiap elemen-nya
pilihan.forEach(function (i) {
  i.addEventListener('click', function () {
    //ambil pilihan computer
    const pilihanComputer = getPilihanComputer();
    //ambil pil player, dengan nama class-nya, yg kebetulan sama
    const pilihanPlayer = i.className;
    const hasilSuit = getHasilSuit(pilihanComputer, pilihanPlayer);

    //panggil fungsi putarGambar u animasi comp memilih
    putarGambar();

    //buat juga si pilihan computer menunggu selama 1 detik
    setTimeout(function () {
      //merubah gambar computer secara random
      const imgComputer = document.querySelector('.img-komputer');
      imgComputer.setAttribute('src', 'img/' + pilihanComputer + '.png');
      //menaruh hasil ke kolom info
      const info = document.querySelector('.info');
      info.innerHTML = hasilSuit;
    }, 1000);
  });
});

//manual tanpa looping
// const pGajah = document.querySelector('.gajah');
// pGajah.addEventListener('click', function () {
//   //ambil pilihan computer
//   const pilihanComputer = getPilihanComputer();
//   //ambil pil player, dengan nama class-nya, yg kebetulan sama
//   const pilihanPlayer = pGajah.className;
//   const hasilSuit = getHasilSuit(pilihanComputer, pilihanPlayer);
//   //merubah gambar computer secara random
//   const imgComputer = document.querySelector('.img-komputer');
//   imgComputer.setAttribute('src', 'img/' + pilihanComputer + '.png');
//   //menaruh hasil ke kolom info
//   const info = document.querySelector('.info');
//   info.innerHTML = hasilSuit;
// });

// const pOrang = document.querySelector('.orang');
// pOrang.addEventListener('click', function () {
//   //ambil pilihan computer
//   const pilihanComputer = getPilihanComputer();
//   //ambil pil player, dengan nama class-nya yg kebetulan sama
//   const pilihanPlayer = pOrang.className;
//   const hasilSuit = getHasilSuit(pilihanComputer, pilihanPlayer);
//   //merubah gambar computer secara random
//   const imgComputer = document.querySelector('.img-komputer');
//   imgComputer.setAttribute('src', 'img/' + pilihanComputer + '.png');
//   //menaruh hasil ke kolom info
//   const info = document.querySelector('.info');
//   info.innerHTML = hasilSuit;
// });

// const pSemut = document.querySelector('.semut');
// pSemut.addEventListener('click', function () {
//   //ambil pilihan computer
//   const pilihanComputer = getPilihanComputer();
//   //ambil pil player, dengan nama class-nya yg kebetulan sama
//   const pilihanPlayer = pSemut.className;
//   const hasilSuit = getHasilSuit(pilihanComputer, pilihanPlayer);
//   //merubah gambar computer secara random
//   const imgComputer = document.querySelector('.img-komputer');
//   imgComputer.setAttribute('src', 'img/' + pilihanComputer + '.png');
//   //menaruh hasil ke kolom info
//   const info = document.querySelector('.info');
//   info.innerHTML = hasilSuit;
// });
