// 1. closures

// code 1
// function init() {
//   let nama = "rizal"; //lokal variabel, hanya di functio ini()

//   // inner function (closure*)
//   function tampilNama() {
//     // punya akses ke parent variabel, si nama ketika dipanggil akan ngecek di dirinya.
//     // jika tak ada akan cek ke parentnya.
//     // kalo gak ada akan ngecek terus ke atas mencari si nama.
//     // nah karena inner function perlu var ke parent nya maka ini disebut closure*
//     console.log(nama);
//   }
//   tampilNama();
// }
// init();

// code  2
// function init() {
//   //   let nama = "rizal"; //lokal variabel, hanya di functio ini()

//   // inner function (closure*)
//   return function (nama) {
//     // punya akses ke parent variabel, si nama ketika dipanggil akan ngecek di dirinya.
//     // jika tak ada akan cek ke parentnya.
//     // kalo gak ada akan ngecek terus ke atas mencari si nama.
//     // nah karena inner function perlu var ke parent nya maka ini disebut closure*
//     console.log(nama);
//   };
// }
// let panggilNama = init();
// panggilNama("kaka");

// code 3, buat function yg sesuai dengan function yg lain
// function ucapSalam(waktu) {
//   return function (nama) {
//     console.log(`Hallo ${nama}, selamat ${waktu}, semoga bahagia`);
//   };
// }
// let pagi = ucapSalam("pagi");
// let siang = ucapSalam("siang");
// let malam = ucapSalam("malam");
// pagi("Rizal");
// malam("asep");

// code 4
// let add = function () {
//   let counter = 0; //counternya jadi privet gak bisa di akses dari luar, tapi nilainya tetap karena jadi closure
//   return function () {
//     return ++counter;
//   };
// };
// let a = add(); // add() menjalankan function add, a menjalankan inner function didalamnya
// console.log(a());
// console.log(a());

// ada cara supaya code 4 gak perlu di tampung ke let a
let add = (function () {
  let counter = 0; //counternya jadi privet gak bisa di akses dari luar, tapi nilainya tetap karena jadi closure
  return function () {
    return ++counter;
  };
})();
// add(); // ini gak perlu
console.log(add());
console.log(add());
