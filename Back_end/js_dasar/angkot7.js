// const prompt = require("prompt-sync")();
// pengelolaan penumpang
// 1. penumpang naik
//  funtion = tambahPenumpang(namaPenumpang,arrayPenumpang).
//  jika angkot kosong maka penumpang duduk di kursi pertama begitupun penumpang berikutnya secara berurutan kursi ke 2.
//  jika ada kursi kosong(karena penumpang turun), maka penumpang yg naik akan duduk dikursi tsb.
//  asumsi kursi tidak akan penuh dan akan bertambah terus jika ada penumpang naik.
//  nama penumpang tidak boleh sama, u menghindari kebingungan ketika nanti penumpang turun.

// buat array dengan nama penumpang
var penumpang = [];
var tambahPenumpang = function (namaPenumpang, penumpang) {
  // jika angkot kosong
  if (penumpang.length == 0) {
    //tambah penumpang diawal array
    penumpang.push(namaPenumpang);
    //kembalikan isi array & keluar dari function
    return penumpang;
  } else {
    // telusuri seluruh kursi dari awal
    for (var i = 0; i < penumpang.length; i++) {
      // jika ada kursi kosong
      if (penumpang[i] == undefined) {
        //tambah penumpang di kursi tsb
        penumpang[i] = namaPenumpang;
        // kembalikan isi array & keluar dari function
        return penumpang;
      }
      //jika sudah ada nama penumpang yg sama
      else if (penumpang[i] == namaPenumpang) {
        //tampilkan pesan kesalahan
        console.log(namaPenumpang + " sudah ada didalam angkot");
        //kembalikan isi array & keluar dari function
        return penumpang;
      }
      //jika seluruh kursi terisi
      else if (i == penumpang.length - 1) {
        //tambah penumpang di akhir array
        penumpang.push(namaPenumpang);
        //kembalikan isi array & keluar dari function
        return penumpang;
      }
    }
  }
};

//  function = hapusPenumpang(namaPenumpang, penumpang)
//  jika angkot kosong kita tampilkang angkot kosong.
//  jika ada penumpang yg namanya sesuai yg dikirim ke parameter,maka hapus caranya dengan undifined
//  jika kita kirim nama penumpang yg tak ada diangkot, tampilkan pesan kesalahan
var hapusPenumpang = function (namaPenumpang, penumpang) {
  // jika angkot kosong
  if (penumpang.length == 0) {
    console.log("angkot masih kosong bozz");
    // kembalikan isi array & keluar dari function
    return penumpang;
  } else {
    // telusuri seluruh kursi dari awal
    for (var i = 0; i < penumpang.length; i++) {
      // jika nama penumpang sesuai
      if (namaPenumpang == penumpang[i]) {
        // hapus penumpang dengan ubah jadi undifined
        penumpang[i] = undefined;
        // kembalikan isi array & keluar dari function
        return penumpang;
        // jika tak ada nama yg sesuai
      } else if (i == penumpang.length - 1) {
        // tampilkan pesan kesalahan
        console.log(namaPenumpang + ", tidak ada nama tersebut di angkot");
        // kembalikan isi array & keluar dari function
        return penumpang;
      }
    }
  }
};

// console.log(hapusPenumpang("kaka", penumpang));
console.log(tambahPenumpang("kaka", penumpang));
console.log(tambahPenumpang("baba", penumpang));
console.log(tambahPenumpang("asep", penumpang));
console.log(hapusPenumpang("kaka", penumpang));
console.log(hapusPenumpang("kaka", penumpang));
console.log(tambahPenumpang("asep", penumpang));
// console.log(hapusPenumpang("kaka", penumpang));
// console.log(tambahPenumpang("jaja", penumpang));
