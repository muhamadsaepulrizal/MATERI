// higher order function

// contoh sederhana

//function kerjakan tugas bisa disebut Higher Order Function
//function yg disimpan sebagai argument disebut callback
// function kerjaTugas(matkul, selesai) {
//   console.log(`Mulai mengerjakan Tugas ${matkul}`);
//   selesai(); //fungsi dijadikan parameter argument
// }
// function selesai() {
//   console.log("Tugas Selesai");
// }
// kerjaTugas("js lanjut", selesai);

// filter
const angka = [-1, 8, 9, 1, 4, -5, -4, 3, 2, 9];
// mencari angka >= 3
// pakai for
// const newAngka = [];
// for (let i = 0; i < angka.length; i++) {
//   if (angka[i] >= 3) newAngka.push(angka[i]);
// }
// console.log(newAngka);

//// pakai filter (cek satu persatu),
//// lalu pakai juga arrow function, function hilang, return hilang, kurung kurawa diganti (=>)
// const newAngka = angka.filter((a) => a >= 3);
// console.log(newAngka);

//// map
//// kalikan samua angka dengan 2
// const newAngka = angka.map((a) => a * 2);
// console.log(newAngka);

////reduce (melakukan sesuatu terhadap semua elemen array / mengelola), parameternya harus 2
////jumlahkan seluruh elemen pada array
////curentValue = elemen array yg sedang di loop, accumulator = hasil dari prosesnya
// const newAngka = angka.reduce(
//   (accumulator, currentValue) => accumulator + currentValue
// );
// console.log(newAngka);

//// menggabungkan filter,map,reduce diatas
//// method chaining (menggabungkan fungsi fungsi / berantai)
//// cari angka > 5, lalu hasilnya kalikan 3, lalu jumlahkan semua elemen
// const hasil = angka
//   .filter((a) => a > 5)
//   .map((a) => a * 3)
//   .reduce((acc, cV) => acc + cV);
// console.log(hasil);
