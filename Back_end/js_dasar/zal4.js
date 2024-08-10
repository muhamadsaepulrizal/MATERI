// refactoring, ubah kode jadi sederhana mungkin

// dari seperti ini
// function jmlVolumeKubus(a, b) {
//   var kubusA, kubusB, total;
//   kubusA = a * a * a;
//   kubusB = b * b * b;
//   total = kubusA + kubusB;

//   return total;
// }

// console.log(jmlVolumeKubus(8, 3));

// jadi seperti ini
function jmlVolumeKubus(a, b) {
  return a * a * a + b * b * b;
}

console.log(jmlVolumeKubus(8, 3));

// scope: block scope
var i = 2;

if (i % 2 == 0) {
  var genap = true;
}

if (genap) {
  console.log("genap");
}

// rekursif
function tes(n) {
  if (n === 0) return;
  console.log(n);
  return tes(n - 1);
}
tes(10);

function faktorial(n) {
  if (n == 0) return 1;
  return n * faktorial(n - 1);
}
console.log(faktorial(5));

tampilPesan("rizal");
function tampilPesan(nama) {
  console.log("hallo " + nama);
}
