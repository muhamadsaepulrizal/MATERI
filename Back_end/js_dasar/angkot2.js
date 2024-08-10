// penulisan variabel
var jmlAngkot = 10;
var angkotBeroperasi = 6;
var noAngkot = 1;

// menampilkan no angkot 1-6 beroperasi dengan baik, 7-10 sedang tidak beroperasi
// dengan 2 loop (while & for)
while (noAngkot <= angkotBeroperasi) {
  console.log("Angkot No. " + noAngkot + " beroperasi dengan baik.");
  noAngkot++;
}
for (var noAngkot = angkotBeroperasi + 1; noAngkot <= jmlAngkot; noAngkot++) {
  console.log("Angkot No. " + noAngkot + " sedang tidak beroperasi.");
}
