const prompt = require('prompt-sync')();

var tanya = true;
while (tanya) {
  //menentukan pilihan player
  var p = prompt('pilih: gajah, semut, orang: ');

  //menangkap pilihan computer
  var com = Math.random();
  // membangkitkan bilangan random 0-1
  if (com < 0.34) {
    com = 'gajah';
  } else if (com >= 0.34 && com < 0.67) {
    com = 'orang';
  } else {
    com = 'semut';
  }

  var hasil = '';
  //menentukan rules
  if (p == com) {
    hasil = 'seri';
  } else if (p == 'gajah') {
    //   if (com == "orang") {
    //     hasil = "menang";
    //   } else {
    //     hasil = "kalah";
    //   }
    hasil = (com = 'orang') ? 'menang' : 'kalah'; // ini bisa menggantikan if else diatas
  } else if (p == 'orang') {
    //   if (com == "gajah") {
    //     hasil = "kalah";
    //   } else {
    //     hasil = "menang";
    //   }
    hasil = (com = 'gajah') ? 'kalah' : 'menang';
  } else if (p == 'semut') {
    hasil = com == 'gajah' ? 'menang' : 'kalah';
  } else {
    hasil = 'pilihan salah';
  }

  // tampilkan hasilya
  console.log('kamu memilih = ' + p + ' dan komputer memilih = ' + com);
  console.log('hasil : ' + hasil);
  var tanya = prompt('apakah lanjut (y/n): ');
  if (tanya == 'n') {
    break;
  }
}
console.log('terima kasih telah bermain suit');
