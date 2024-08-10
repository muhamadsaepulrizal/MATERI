// pengelolaan angkot, yg dikelola:
// 1.sopir
// 2.trayek
// 3.kas
// 4.penumpang: penumpang naik, penumpang turun

// membuat object Angkot
function Angkot(sopir, trayek, penumpang, kas) {
  this.sopir = sopir;
  this.trayek = trayek;
  this.penumpang = penumpang;
  this.kas = kas;

  this.penumpangNaik = function (namaPenumpang) {
    this.penumpang.push(namaPenumpang);
    return this.penumpang;
  };

  this.penumpangTurun = function (namaPenumpang, bayar) {
    if (this.penumpang.length === 0) {
      console.log("belum ada penumpang bozz");
      return false; // supaya keluar method
    }

    for (var i = 0; i < this.penumpang.length; i++) {
      if (this.penumpang[i] == namaPenumpang) {
        this.penumpang[i] = undefined;
        this.kas += bayar; // jika penumpang bayar yg dibayarkan penumpang tambahkan ke kas
        return this.penumpang;
      }
    }
  };
}

var angkot1 = new Angkot("rizal", ["garut", "leuwigoong"], [], 0);
var angkot2 = new Angkot("tom", ["garut", "banyuresmi"], [], 0);

//penumpang angkot 1naik
angkot1.penumpangNaik("koko");
console.log(angkot1);

// penumpang angkot2 naik
angkot2.penumpangNaik("ucup");
console.log(angkot2);

// penumpang angkot 1naik
angkot1.penumpangNaik("agus");
console.log(angkot1);

//penumpang angkot 1 turun
angkot1.penumpangTurun("koko", 1000);
console.log(angkot1);

// penumpang angkot1 turun
angkot1.penumpangTurun("agus", 5000);
console.log(angkot1);
