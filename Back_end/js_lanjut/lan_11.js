// - for..of
// mengulang atau menelusuri object2 yg iterable
// seperti = string, array, arguments/NodeList, typeArray, map, set, user-defined itelables

// // case 1 penggunaan for..of ke array, karena array itu iterables
// // const mhs = ["rizal", "koko", "agus"];
// // for biasa
// for (let i = 0; i < mhs.length; i++) {
//   console.log(mhs[i]);
// }

// //forEach, khusu untuk array
// //forEach juga bisa punya 2 parameter satunya lagi untuk index, jadi bisa seperti dibawah
// mhs.forEach((m, i) => {
//   console.log(`${m} adalah mahasiswa ke-${i + 1}`);
// });

// // for..of = kalau for..of secara default gk punya index
// // tapi tetep bisa diakalin caranya pakai .entries() setelah array-nya.
// // didepan deklarasikan indexnya dulu, baru var untuk menampung isi array-nya contoh = [i,m]
// for (const [i, m] of mhs.entries()) {
//   console.log(`${m} adalah mhs ke-${i + 1}`);
// }

// // case 2 penggunaan pada string, karna string iterables
// // tapi string gak bisa pake forEach, karna forEach khusus untuk array
// // const nama = "rizal";
// // for..of. akan me loop tiap-tiap karakter dalam string-nya
// for (const n of nama) {
//   console.log(n);
// }

// // case 3 penggunaan pada NodeList, melakukan QRY pada DOM
// // const liNama = document.querySelectorAll(".nama");
// // pakai forEach
// liNama.forEach((n) => console.log(n.textContent));

// // pakai for..of
// for (let n of liNama) {
//   console.log(n.textContent);
// }

// // loop arguments disini kita bisa tak pakai parameter tapi memanfaatkan for..of
// function jmlAngka() {
//   let jml = 0;
//   for (a of arguments) {
//     jml += a;
//   }
//   return jml;
// }
// console.log(jmlAngka(1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5));

// - for.. in = perhatikan kata in artinya didalam
// hanya untuk properti pada object
// const mhs = {
//   nama: "rizal",
//   umur: 20,
//   email: "2306142@itg.ac.id",
// };
// // jika ingin ambil valuenya kita tinggal jadikan mhs sebagai index, m untuk menangkap valeunya
// for (m in mhs) {
//   console.log(mhs[m]);
// }
