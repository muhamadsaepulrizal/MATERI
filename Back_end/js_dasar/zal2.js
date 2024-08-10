const prompt = require("prompt-sync")();
// console.log("hello world");

// pengulangan:

// while
// pakai increment
var ulang = 1;
while (ulang <= 5) {
  console.log("hello world " + ulang + " x");
  ulang++;
}
// while pakai decrement
// var ulang = 5;
// while (ulang >= 1) {
//   console.log("hello world " + ulang + "x");
//   ulang--; // ulang = ulang + 1;
// }

// for
// pakai increment
var nilaiAwal = 1;
for (var i = nilaiAwal; i <= 5; i++) {
  console.log("hello for " + i + " x");
}
// for pakai decrement
// for (nilaiAwal = 5; nilaiAwal >= 1; nilaiAwal--) {
//   console.log("hello for with dec " + nilaiAwal + " x");
// }

// pengkondisian
// contoh sederhana
// var angka = prompt("masukkan angka: ");
// if (angka % 2 === 0) {
//   console.log("genap"); //alert for web
// } else if (angka % 2 === 1) {
//   console.log("ganjil");
// } else {
//   console.log("inputan dilarang angka!!");
// }

// pengkondisian dengan switch

// var angka = prompt("masukkan angka: ");

// switch (angka) {
//   case "1": // case nya string
//     console.log("anda memasukkan angka 1");
//     break;
//   case "2":
//     console.log("anda memasukkan angka 2");
//     break;
//   case "3":
//     console.log("anda memasukkan angka 3");
//     break;
//   default:
//     console.log("angka salah");
//     break;
// }

var item = prompt(
  "masukkan nama makanan / minuman: (cth): nasi, daging, susu, hamburger, softdrink: "
);

switch (item) {
  case "nasi":
  case "daging":
  case "susu":
    console.log("makanan / minuman SEHAT");
    break;
  case "hamburger":
  case "softdrink":
    console.log("makanan / minuman TIDAK SEHAT");
    break;
  default:
    console.log("nama makanan / minuman salah");
    break;
}
