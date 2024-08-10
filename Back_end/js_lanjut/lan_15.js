// const prompt = require("prompt-sync")();

// // contoh 1 synchronous callback
// // function halo(nama) {
// //   alert(`hallo, ${nama}`);
// // }
// function tampilPesan(callback) {
//   var nama = prompt("masukkan nama: ");
//   callback(nama);
// }
// // tampilPesan(halo); //gak pake kurung supaya gak langsung dieksekusi jadi nunggu dipanggil

// // bisa juga gak pake function diatas langsung saja seperi begini: pakai arrow function
// tampilPesan((nama) => alert(`hallo bro kaka, ${nama}`));

// // contoh 2 ada object didalam array
// const mhs = [
//   {
//     nama: "kaka",
//     nim: "2306142",
//     email: "kaka@gmail",
//     jurusan: "infor",
//     idDosen: 1,
//   },
//   {
//     nama: "coco",
//     nim: "2306143",
//     email: "coco@gmail",
//     jurusan: "infor",
//     idDosen: 2,
//   },
//   {
//     nama: "erik",
//     nim: "2306144",
//     email: "erik@gmail",
//     jurusan: "infor",
//     idDosen: 3,
//   },
// ];
// // synchronous
// // saya ingin menampilkan nama mahasiswanya saja
// // buat seolah2 proses forEach lama
// console.log("mulai");
// mhs.forEach((m) => {
//   for (var i = 0; i < 10000000; i++) {
//     let date = new Date();
//   }
//   console.log(m.nama);
// });
// console.log("selesai");

// // contoh 3sekarang kita ke Asynchronous callback
// // url untuk ke file tujuan, success & error adl callback
// function getDataMhs(url, success, error) {
//   let xhr = new XMLHttpRequest();

//   xhr.onreadystatechange = function () {
//     //artinya 4 itu sudah ready
//     if (xhr.readyState === 4) {
//       //kalau statusnya 200, 200 itu oke, bisa akses halaman (mahasiswa.json)
//       if (xhr.status === 200) {
//         success(xhr.response);
//         //kalau 404, 404 itu error
//       } else if (xhr.status === 404) {
//         error();
//       }
//     }
//   };
//   //jalankan ajax-nya
//   xhr.open("get", url);
//   xhr.send();
// }

// console.log("mulai");
// //ini Asynchronous
// getDataMhs(
//   "data_lan_15/mahasiswa.json",
//   //untuk success
//   (result) => {
//     //jika ingin dalam bentuk object result kita parse dulu (JSON.parse)
//     const mhs = JSON.parse(result);
//     //tampilkan nama-nya saja
//     mhs.forEach((m) => console.log(m.nama));
//   },
//   //untuk error
//   () => {}
// );
// console.log("selesai");

// // contoh lebih gampang dari javascript murni diatas yaitu pakai jquery, panggil jquery di html
// // JQuery
// console.log("mulai");
// $.ajax({
//   url: "data_lan_15/mahasiswa.json",
//   success: (mhs) => {
//     mhs.forEach((m) => console.log(m.nama));
//   },
//   error: (e) => {
//     console.log(e.responseText);
//   },
// });
// console.log("selesai");
