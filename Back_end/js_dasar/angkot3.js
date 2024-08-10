// penulisan variabel
var jmlAngkot = 10;
var angkotBeroperasi = 6;
var noAngkot = 1;

// menampilkan no angkot 1-6 beroperasi dengan baik, 7-10 sedang tidak beroperasi
//dengan 1 loop didalammnya ada perkondisian if else
while (noAngkot <= jmlAngkot) {
  if (noAngkot <= angkotBeroperasi) {
    console.log("Angkot No. " + noAngkot + " beroperasi dengan baik");
  } else {
    console.log("Angkot No. " + noAngkot + " sedang tidak beroperasi");
  }
  noAngkot++;
}

// dengan for
// for (var noAngkot = 1; noAngkot <= jmlAngkot; noAngkot++) {
//   if (noAngkot <= angkotBeroperasi) {
//     console.log("Angkot No. " + noAngkot + " beroperasi dengan baik");
//   } else {
//     console.log("Angkot No. " + noAngkot + " sedang tidak beroperasi");
//   }
// }
