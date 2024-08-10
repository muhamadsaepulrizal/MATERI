// -Execution Context, Hoisting, Scope

// pada creation phase pada global context
// Hoisting meskipun var dibawah maka akan dinaikan
// 1.kalo membuat nama var = undifined
// 2.kalo membuat funvtion = function()
// window = global object
// this = window

// baru execution phase dari atas kebawah

// var nama = "rizal";
// var umur = 20;
// console.log(sayHello());
//
// function sayHello() {
//   return `hallo saya ${nama}, saya ${umur} tahun `;
// }

// function membuat local execution context
// yg di dlmnya terdapat cretaing dan execution phase
// window
// arguments
// hoisting

// tumpukan eksekusi
// contoh kasus supaya gak bingung
// var nama = "zal";
// var userIge = "@zal_204";
//
// function cetakUrl(userIg) {
//   var ig = `http://instagram.com/`;
//   return ig + userIg;
// }
// console.log(cetakUrl(userIge));

// function a() {
//   console.log("ini a");
//
//   function b() {
// console.log("ini b");
//
// function c() {
//   console.log("ini c");
// }
// c();
//   }
//   b();
// }
// a();
