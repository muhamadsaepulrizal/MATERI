// membuat object

// var mhs = {
//   nama: "rizal",
//   umur: 20,
//   ips: [3.6, 3.9],
//   alamat: {
//     jalan: "KH. Hasan Arif",
//     kp: "babakan cibudug",
//     kab: "garut",
//   },
// };

// console.log(mhs.alamat);
// console.log(mhs["umur"]);
// console.log(mhs.ips[1]);
// console.log(mhs.alamat);
// console.log(mhs.alamat.kp);

// cara membuat object

//1. object literal
var mhs_1 = {
  // key : value,
  nama: "rizal",
  nim: "2306142",
  email: "2306142@itg.ac.id",
  jurusan: "teknik informatika",
};
var mhs_2 = {
  // key : value,
  nama: "saepul",
  nim: "2306136",
  email: "2306136@itg.ac.id",
  jurusan: "teknik informatika",
};
console.log(mhs_1);
console.log(mhs_2);

//2. pakai function declaration
function buatObjectMhs(nama, nim, email, jurusan) {
  // buat object kosong
  var mhs = {};
  // isi object dengan parameter diatas
  mhs.nama = nama;
  mhs.nim = nim;
  mhs.email = email;
  mhs.jurusan = jurusan;
  // kembalikan nilai objectnya
  return mhs;
}
// tampung function ke sebuah variabel
var mhs_3 = buatObjectMhs(
  // masukkan nilai(argument) sesuai urutan parameter
  "ahmad",
  "2306143",
  "2306143@itg.ac.id",
  "teknik informatika"
);
console.log(mhs_3);

// 3. constructor ini yg sering dipakai
function Mahasiswa(nama, nim, email, jurusan) {
  this.nama = nama;
  this.nim = nim;
  this.email = email;
  this.jurusan = jurusan;
}
var mhs_4 = new Mahasiswa(
  "asep",
  "2306140",
  "2306140@itg.ac.id",
  "teknik informatika"
);
console.log(mhs_4);
