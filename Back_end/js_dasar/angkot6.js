// penulisan variabel
var jmlAngkot = 10;
var angkotBeroperasi = 6;
var noAngkot = 1;

// menampilkan no angkot 1,2,3,4,6 beroperasi dengan baik, 5,8, dan 10 sedang lembur
// dan 7,9, sedang tidak beroperasi
// menggunakan while if | else if | else
// while (noAngkot <= jmlAngkot) {
//   if ((noAngkot <= angkotBeroperasi) & (noAngkot !== 5)) {
//     console.log("Angkot NO. " + noAngkot + " beroperasi dengan baik");
//   } else if (noAngkot === 8 || noAngkot === 10 || noAngkot === 5) {
//     console.log("Angkot NO. " + noAngkot + " sedang lembur");
//   } else {
//     console.log("Angkot No. " + noAngkot + " sedang tidak dapat beroperasi");
//   }
//   noAngkot++;
// }

// dengan for
for (var noAngkot = 1; noAngkot <= jmlAngkot; noAngkot++) {
  if ((noAngkot <= angkotBeroperasi) & (noAngkot !== 5)) {
    console.log("Angkot NO. " + noAngkot + " beroperasi dengan baik");
  } else if (noAngkot === 8 || noAngkot === 10 || noAngkot === 5) {
    console.log("Angkot NO. " + noAngkot + " sedang lembur");
  } else {
    console.log("Angkot No. " + noAngkot + " sedang tidak dapat beroperasi");
  }
}
