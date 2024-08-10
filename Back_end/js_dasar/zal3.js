const prompt = require("prompt-sync")();

// membuat bintang

var s = ""; // inis var string kosong u menampung bintang & newline

// for (var i = 0; i < 7; i++) {
//   // loop i u baris (newline)
//   for (var j = 0; j <= i; j++) {
//     // loop j u mencetak bintang(*)
//     s += "*";
//   }
//   s += "\n";
// }
// console.log(s);

// for (var i = 7; i >= 0; i--) {
//   for (var j = 1; j <= 7; j++) {
//     s += "*";
//   }
//   s += "\n";
// }
// console.log(s);

// function declaration
// function jmlbil(a, b) {
//   var total;
//   total = a + b;
//   return total;
// }

// console.log(jmlbil(5, 4));

// // function ekspression
// var jumbil = function (a, b) {
//   var total;
//   total = a + b;

//   return total;
// };

// console.log(jumbil(5, 10.7));

// function hitungKubus(a, b) {
//   var kubusA, kubusB, total;
//   kubusA = a * a * a;
//   kubusB = b * b * b;
//   total = kubusA + kubusB;

//   return total;
// }

// console.log(hitungKubus(8, 3));
// console.log(hitungKubus(10, 15));

// function dengan inputan user
// function tambah2Nilai(a, b) {
//   return a + b;
// }

// var ni1 = parseInt(prompt("Masukkan nilai 1: "));
// var ni2 = parseInt(prompt("Masukkan nilai 2: "));

// var hasil = tambah2Nilai(ni1, ni2);

// console.log(hasil);

// contoh function ber argument function
// function tambah(a, b, c) {
//   return a + b;
// }
// function kali(a, b) {
//   return a * b;
// }

// var hasil = kali(tambah(1, 2), tambah(3, 4));
// console.log(hasil);

// var hasil2 = tambah(5, 6);
// console.log(hasil2);

// contoh: nilai argument yg kelebihan sebenarnya ditampung dalam sebuah array yg namanya arguments
// function tambah() {
//   return arguments;
// }
// var cobaArgu = tambah(5, 10, 20, "hi", false);
// console.log(cobaArgu);

// contoh lain nya dalam pemanfaatan array argument
function tambah() {
  var hasil = 0;
  for (var i = 0; i < arguments.length; i++) {
    hasil += arguments[i];
  }
  return hasil;
}

//dgn manfaat arguments pada fungsi diatas kita bisa input nilai nya bebas untuk operasi penjumlahan
var coba = tambah(8, 1, 2, 3, 5.5);
console.log(coba);
