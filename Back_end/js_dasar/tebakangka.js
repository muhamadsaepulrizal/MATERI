const prompt = require("prompt-sync")();

var tanya = true;
while (tanya) {
  //menentukan pilihan player
  var p = prompt("Tebak angka 1-10: ");

  //menangkap pilihan komputer
  var comp = Math.random();
  // membangkitkan bilangan random
  if (comp < 0.2) {
    comp = "1";
  } else if (comp >= 0.2 && comp < 0.3) {
    comp = "2";
  } else if (comp >= 0.3 && comp < 0.4) {
    comp = "3";
  } else if (comp >= 0.4 && comp < 0.5) {
    comp = "4";
  } else if (comp >= 0.5 && comp < 0.6) {
    comp = "5";
  } else if (comp >= 0.6 && comp < 0.7) {
    comp = "6";
  } else if (comp >= 0.7 && comp < 0.8) {
    comp = "7";
  } else if (comp >= 0.8 && comp < 0.9) {
    comp = "8";
  } else if (comp >= 0.9 && comp < 1.0) {
    comp = "9";
  } else {
    comp = "10";
  }

  var hasil = "";

  if (p == comp) {
    hasil = "tebakan anda benar";
  } else if (p < comp) {
    hasil = "pilihan anda terlalu rendah";
    p = prompt("masukkan angka lagi: ");
    if (p == comp) {
      console.log(hasil);
    }
  } else if (p > comp) {
    hasil = "pilihan anda terlalu besar";
    p = prompt("masukkan angka lagi: ");
    if (p == comp) {
      console.log(hasil);
    }
  } else {
    hasil = "angka salah";
    p = prompt("masukkan angka lagi: ");
    if (p == comp) {
      console.log(hasil);
    }
  }

  //   console.log(hasil);
  // if (hasil == "pilihan anda terlalu rendah") {
  //   p = prompt("masukkan angka lagi: ");
  //   console.log(hasil);
  // } else if (hasil == "pilihan anda terlalu besar") {
  //   p = prompt("masukkan angka lagi: ");
  //   console.log(hasil);
  // } else if (hasil == "angka salah") {
  //   p = prompt("masukkan angka lagi: ");
  //   console.log(hasil);
  // } else {
  //   console.log(hasil);
  //   break;
  // }
}
