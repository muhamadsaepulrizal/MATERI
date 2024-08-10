// Arrow Function?
// let tampilPesan = (nama) => {
//   console.log(`hallo ${nama}`);
// };
// tampilPesan("koko");

// function expression
// const tampilPesan = function (nama) {
//   return `hallo ${nama}`;
// };
// console.log(tampilPesan("ajat"));

// rubah ke arrow function menjadi: implisit return (1 parameter, 1 return)
// const tampilPesan = (nama) => `hallo ${nama}`;
// console.log(tampilPesan("baba"));

// contoh lain:
// const tampilNama = (nama, waktu) => {
//   return `Selamat ${waktu}, ${nama}`;
// };
// console.log(tampilNama("rizal", "sore"));

// contoh lain arrow function:
// let mhs = ["kaka", "rizal", "jojo"];
// let jmlHuruf = mhs.map(function (nama) {
//   return nama.length;
// });
// console.log(jmlHuruf);

// jmlHuruf diubah ke arrow function jauh lebih ringkas
// let jmlHuruf = mhs.map((nama) => nama.length);
// console.log(jmlHuruf);

// jika ingin dikembalikan dalam bentu object{} si ({}) dibungkus dengan kurung supaya dianggap obejct
// let jmlHuruf = mhs.map((nama) => ({ nama: nama, jumHur: nama.length }));
// console.table(jmlHuruf); //.table artinya tampilan di console berupa table
