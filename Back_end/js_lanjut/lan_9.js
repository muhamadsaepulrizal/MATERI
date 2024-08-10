// destructuring assignment / avariabel
// // contoh dengan array
// const coba = ["satu", "dua", "tiga"];
// const [a, b, c] = coba;
// console.log(a); //satu
// console.log(b); //dua
// console.log(c); //tiga
// //contoh dengan object
// const mhs = {
//   nama: "rizal",
//   umur: 20,
//   email: "2306142@gmail.com",
// };
// const { nama, umur, email } = mhs;
// console.log(nama);
// console.log(umur);
// console.log(email);

// // contoh lain array
// const perkenalan = ["hallo", "nama", "saya", "rizal"];
// // const [sapa, satu, dua, nama] = perkenalan;
// // bisa di skip tapi komamya harus tetap ada
// const [sapa, , , nama] = perkenalan;
// console.log(sapa);

// // dipakai untuk swap item
// let a = 1;
// let b = 2;
// [a, b] = [b, a]; //bisa langsung ditukar dengan cara begini
// console.log(a);

// // bisa juga return value pada function
// function coba() {
//   return [1, 2];
// }
// // const a = coba(); //tipe a jadi array
// // console.log(a[1]);
// // cara diatas bisa langsung dipecah tanpa tulis indexnya saat dipanggail
// const [a, b] = coba(); //tipe a jadi array
// console.log(a, b);

// // rest parameter supaya mengatasi jika elemennya terus bertambah
// const [a, ...args] = [1, 2, 3, 4, 5];
// console.log(a);
// console.log(args[0]); //tapi ini jadi berbentuk array lagi

// // contoh lain object
// const mhs = {
//   nama: "rizal",
//   umur: 20,
// };
// const { nama, umur } = mhs; //harus sama nama untuk nama, umur untuk umur
// console.log(nama);

// // assignment tanpa deklarasi object & const tapi tambah kurung diawal dan diakhir sebelum titik koma
// ({ nama, umur } = {
//   nama: "rizal",
//   umur: 20,
// });
// console.log(nama);

// // assign ke variabel baru
// const mhs = {
//   nama: "rizal",
//   umur: 20,
// };
// const { nama: n, umur: u } = mhs; //bisa tidak harus sama caranya tambah (:) lalu nama atau singkatan baru
// console.log(n);

// // memberikan default value
// const mhs = {
//   nama: "rizal",
//   umur: 20,
//   email: "2306142@gmail.com",
// };
// // bisa memberi default jika tidak ada seperi dibawah, jadi cek dulu ke object kalo gak ada baru default jalankan
// const { nama, umur, email = "email@default" } = mhs;
// console.log(email);

// // memeberi default value + assign ke var baru
// const mhs = {
//   nama: "rizal",
//   umur: 20,
// };
// const { nama: n, umur: u, email: e = "gak ada email bos" } = mhs;
// console.log(e);

// // bisa juga pakai rest parameter
// const mhs = {
//   nama: "rizal",
//   umur: 20,
//   email: "2306142@itg.ac.id",
// };
// const { nama, umur, ...args } = mhs; //...args -nya dalam bentuk object
// console.log(args);

// // mengambil field pada object, beres dikirim sbg parameter oleh function
// const mhs = {
//   id: 123,
//   nama: "rizal",
//   umur: 20,
//   email: "2306142@itg.ac.id",
// };
// // dibongkar lalu yg diambil hanya id nya, dengan cara di ()parameter masukkan kurungKurawa{properti}
// function getIdMhs({ id }) {
//   return id;
// }
// console.log(getIdMhs(mhs));
