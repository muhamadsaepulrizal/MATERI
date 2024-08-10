// penulisan variabel
var jmlAngkot = 10;
var angkotBeroperasi = 6;
var noAngkot = 1;

// menampilkan no angkot 1-6 beroperasi dengan baik, 8 sedang lembur
// dan 7,9,10 sedang tidak beroperasi
// menggunakan while if | else if | else
while (noAngkot <= jmlAngkot) {
  if (noAngkot <= angkotBeroperasi) {
    console.log("Angkot NO. " + noAngkot + " beroperasi dengan baik");
  } else if (noAngkot === 8) {
    console.log("Angkot No. " + noAngkot + " sedang lembur");
  } else {
    console.log("Angkot NO. " + noAngkot + " sedang tidak beroperasi");
  }
  noAngkot++;
}

// dengan for
for (var noAngkot = 1; noAngkot <= jmlAngkot; noAngkot++) {
  if (noAngkot <= angkotBeroperasi) {
    console.log("Angkot NO. " + noAngkot + " beroperasi dengan baik");
  } else if (noAngkot === 8) {
    console.log("Angkot No. " + noAngkot + " sedang lembur");
  } else {
    console.log("Angkot NO. " + noAngkot + " sedang tidak beroperasi");
  }
}
