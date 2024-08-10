// 1. Cara membuat Object
//  -object literal
// let mhs = {
//   nama: "rizal",
//   energi: 10,
//   makan: function (porsi) {
//     this.energi = this.energi + porsi;
//     console.log(`hallo ${this.nama}, selamat makan`);
//   },
// };
// console.log(mhs.makan(2));
// console.log(mhs);

//  -function declaration
// function Mahasiswa(nama, energi) {
//   let mhs = {};
//   mhs.nama = nama;
//   mhs.energi = energi;

//   mhs.makan = function (porsi) {
//     this.energi += porsi;
//     console.log(`hallo ${nama}, selamat makan sebanyak ${porsi} porsi`);
//   };

//   mhs.main = function (jam) {
//     this.energi -= jam;
//     console.log(`${nama} main ${jam}jam`);
//   };
//   return mhs;
// }
// let rizal = Mahasiswa("rizal", 10);
// console.log(rizal);
// console.log(rizal.makan(5));
// console.log(`energi sekarang ${rizal.energi}`);
// let kaka = Mahasiswa("kaka", 20);
// console.log(kaka);
// console.log(kaka.main(10));
// console.log(`energi sekarang ${kaka.energi}`);

//  -construktur function
// function Mahasiswa(nama, energi) {
//   this.nama = nama;
//   this.energi = energi;

//   this.makan = function (porsi) {
//     this.energi += porsi;
//     console.log(`hallo ${nama}, selamat makan sebanyak ${porsi} porsi`);
//   };

//   this.main = function (jam) {
//     this.energi -= jam;
//     console.log(`${nama} main ${jam}jam`);
//   };
// }
// let asep = new Mahasiswa("asep", 10);
// console.log(asep);
// console.log(asep.main(5));
// console.log(`sisa energi ${asep.energi}`);

//  -object create()
// const methodMahasiswa = {
//   makan: function (porsi) {
//     this.energi += porsi;
//     console.log(`hallo ${this.nama}, selamat makan sebanyak ${porsi} porsi`);
//   },
//   main: function (jam) {
//     this.energi -= jam;
//     console.log(`${this.nama} main ${jam}jam`);
//   },
//   tidur: function (jam) {
//     this.energi += jam * 2;
//     console.log(`${this.nama} selamat tidur`);
//   },
// };
// function Mahasiswa(nama, energi) {
//Object.create() digunakan untuk menghubungkan dengan method lain u dijadikan parentnya yaitu methodMahasiswa
//   let mhs = Object.create(methodMahasiswa);
//   mhs.nama = nama;
//   mhs.energi = energi;

//   return mhs;
// }
// let agum = Mahasiswa("agum", 20);
// console.log(agum);
// console.log(agum.makan(10));
// console.log(`energi sekarang ${agum.energi}`);

// Object dengan prototype inherit
// // perubahan diatas dengan Object.creat() + prototype
// // yg dikelola objectnya cuma 1 tingal ambil prototypenya
// function Mahasiswa(nama, energi) {
//   //let mhs = Object.create(methodMahasiswa); //Object.create() digunakan untuk menghubungkan dengan method lain
//   //let mhs = {}
//   //let this = Object.create(Mahasiswa.prototype); //ini yg sebenarnya terjadi dibelakang layar jika pakai this
//   this.nama = nama;
//   this.energi = energi;
//   //return mhs;
//   //return this //terjadi dibelakang layar jika pakai this
// }
// // ini nempel dengan object mahasiswa diatas
// Mahasiswa.prototype.makan = function (porsi) {
//   //protoype sebagai pewarisan antara Mahasiswa dengan makan(dll)
//   this.energi += porsi;
//   return `hallo ${this.nama} selamat makan`;
// };
// Mahasiswa.prototype.main = function (jam) {
//   this.energi -= jam;
//   return `halllo ${this.nama} selamat bermain`;
// };
// Mahasiswa.prototype.tidur = function (jam) {
//   this.energi += jam * 2;
//   return `hallo ${this.nama} selamat tidur`;
// };
// let rizal = new Mahasiswa("rizal", 10);
// console.log(rizal);
// console.log(rizal.makan(10));
// console.log(rizal.energi);
// console.log(rizal.main(5));
// console.log(rizal.energi);
// console.log(rizal.tidur(5));
// console.log(rizal.energi);

// versi class diatas, jadi versi class ini sama aja jalannya seperti prototype diatas cara kejanya
// hanya dibungkus class supaya lebih bisa dipahami
// class Mahasiswa {
//   constructor(nama, energi) {
// this.nama = nama;
// this.energi = energi;
//   }
//
//   makan(porsi) {
// this.energi += porsi;
// return `hallo ${this.nama} selamat makan`;
//   }
//   main(jam) {
// this.energi -= jam;
// return `hallo ${this.nama} selamat bermain`;
//   }
//   tidur(jam) {
// this.energi += jam * 2;
// return `hallo ${this.nama} selamat tidur`;
//   }
// }
// let rizal = new Mahasiswa("rizal", 20);
// console.log(rizal);
// console.log(rizal.main(10));
// console.log(rizal.energi);
// console.log(rizal);
// console.log(rizal.makan(20));
// console.log(rizal.energi);
// console.log(rizal);
// console.log(rizal.tidur(10));
// console.log(rizal.energi);
//
