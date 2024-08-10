// array
// var hari = ["senin", "salasa", "rabu", 4, true, [4, 5, 6]];

// console.log(hari.length);
// console.log(hari.length);

// console.log(hari[5][1]);

// manipulasi array

// 1.menambah isi array cara manual
// var arr = [];
// arr[0] = ["muhamad"];
// arr[1] = ["saepul"];
// arr[2] = ["rizal"];
// arr[6] = ["kakang"];
// console.log(arr);

// 2.menghapus array cara manual
// var arr = ["riz", "zal", "sap"];
// arr[1] = undefined;
// console.log(arr);

// 3.menampilkan array
// var arr = ["riz", "zal", "sap", "kang", "sep"];
// for (var i = 0; i < arr.length; i++) {
//   console.log("Mahasiswa ke-" + (i + 1) + ": " + arr[i]);
// }

// method pada array
// var arr = ["riz", "zal", "sap", "kang", "sep"];
// join
// console.log(arr.join("\n"));

// push
// arr.push("jum");
// console.log(arr.join("\n"));

// pop
// arr.pop();
// arr.pop();
// console.log(arr.join("\n"));

// ushift
// arr.unshift("gon", "min");
// console.log(arr.join("\n"));

// shift
// arr.shift();
// console.log(arr.join("\n"));

// splice
// arr.splice(2, 0, "bud"); //mulai index2, menghapus 0(tak da), "menambah bud"
// arr.splice(2, 3, "bud", "jin", "son"); //mulai index2, hapus 3, "menambah 3"
// console.log(arr.join("\n"));

// slice
// var arr = ["riz", "zal", "sap", "kang", "sep"];
// var arr2 = arr.slice(2, 4);
// console.log(arr2.join("\n"));

// foreach
// var angka = [1, 2, 3, 4, 5, 6, 7, 8];
// var nama = ["jaja", "gugu", "kaka"];
// for (var i = 0; i < angka.length; i++) {
//   console.log(angka[i]);
// }
// bisa diganti jadi
// angka.forEach(function (e) {
//   console.log(e);
// });

// nama.forEach(function (e, i) {
//   console.log("Mahasiswa ke-" + (i + 1) + " adalah: " + e);
// });

// map
// var angka1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
// var angka2 = angka1.map(function (e) {
//   return e * 2;
// });
// console.log(angka2.join("\n"));

// sort
// var angka1 = [1, 2, 4, 5, 3, 10, 20, 8, 9, 6, 7];
// console.log(angka1.join("-"));
// angka1.sort(function (a, b) {
//   return a - b;
// });
// console.log(angka1.join("-"));

// filter
var angka1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var angka2 = angka1.find(function (x) {
  return x >= 5;
});
console.log(angka2);
