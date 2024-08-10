// 8. Destructuring Function

// // 1. destructur  return value
// function tambahKali(a, b) {
//   return [a + b, a * b];
// }
// // ini agak ribet karena harus tuliskan indexnya
// const jumlah = tambahKali(2, 3);
// console.log(jumlah[0]);
// console.log(jumlah[1]);

// // case 1
// // kita pecah aja / destructuring
// const [tambah, kali] = tambahKali(2, 3);
// console.log(kali);

// // case 2
// function opMath(a, b) {
//   return {
//     tambah: a + b,
//     kurang: a - b,
//     kali: a * b,
//     bagi: a / b,
//   };
// }
// const { kali, kurang, bagi, tambah } = opMath(5, 5);
// console.log(bagi);

// // 2. destructur arguments
// // case 3
// const mhs1 = {
//   nama: "rizal",
//   umur: "20",
//   email: "2306142@itg.ac.id",
//   nilai: {
//     tugas: 80,
//     uts: 85,
//     uas: 75,
//   },
// };
// // destructur dipecah object mhs1 disini hanya nama,umur pakai kurungKurawa
// // lalu kita bisa lakukan destructur bersarang seperti dibawah pemecahan dilakukan pakai tanda (:)
// function cetakMhs({ nama, umur, nilai: { uas } }) {
//   return `Hallo nama saya ${nama}, umur saya ${umur} tahun, dan nilai uas saya adalah ${uas}`;
// }
// console.log(cetakMhs(mhs1)); //object masuk kesini
