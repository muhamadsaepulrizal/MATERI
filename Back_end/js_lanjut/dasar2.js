// 12 refactoring
// -sebuah proses mengubah kode agar menjadi lebih 'baik' tanpa mengubah fungsionalitas
// kenapa?
// -kemudahan dlm dibaca programnya(readability)
// -don't repeat yourself (DRY)
// -testability, penulisan kode agar mudah saat dilakukan pengujian
// -performance, bagaimana menulis kode yg dpr meningkatkan performance sebuah program
// -maintainbility, kode kedepannya dpt dengan mudah dikembangkan
// note: sebisa mungkin lakukan diakhir pembuatan program
//      periksa apakah ada penulisan yg tidak perlu tanpa mengurangi fungsionalitas
// dari seperti ini
//      function jmlVolumeKubus(a, b) {
//        var kubusA, kubusB, total;
//        kubusA = a * a * a;
//        kubusB = b * b * b;
//        total = kubusA + kubusB;
//
//        return total;
//      }
//
//      console.log(jmlVolumeKubus(8, 3));
//
// jadi seperti ini
//      function jmlVolumeKubus(a, b) {
//        return a * a * a + b * b * b;
//      }
//
//      console.log(jmlVolumeKubus(8, 3));
// ------------------------------------------------------------------------------------
//
// 13 scope = lingkup variabel
// -block scope (C,java) = secara sederhana variabel di dalam scope tertenru ({})
//  belum tentu bisa dipanggil di dalam scope ({}) lain
// -function scope (javascript) = secara sederhana variabel didalam scope tertentu ({})
//  bisa saja dipanggil dan digunakan di dlm scope lain ({})
// -contoh variabel global (berada di paling luar)
//  var i = 1;
// -contoh function scope
//  function tes(){
//         var b = 2;
//  }
//  si var b tidak bisa langsung dipanggi di luar function
// -tapi didalam function scope kita bisa gunakan variabel global scope begitupun sebaliknya
// -dan dalam function scope tak bisa menimpa nilai variabel global, kecuali
//  didalam function scope kita jangan mendeklarasikan (var) langsung saja nama variabelnya + nilai baru
// -note = pelajari "use strict";
// -------------------------------------------------------------------------------------
//
// 14 rekursif = sebuah function yg memanggil dirinya sendiri
// -Base case = kodisi akhir dari rekursif yg menghasilkan nilai
// -contoh rekursif dengan base case
//      function tes(n) {
//        if (n === 0) return; (ini base case rekursifnya)
//        console.log(n);
//        return tes(n - 1);
//      }
//      tes(10);
// -contoh lain dlm faktorial
//      function faktorial(n) {
//        if (n == 0) return 1;
//        return n * faktorial(n - 1);
//      }
//      console.log(faktorial(5));
// -note = semua loop bisa dibuat rekursif, tapi tidak sebaliknya
// -implementasi rekursif
//  1.mengganti looping
//  2.deret fibonacci, faktorial
//  3.pencarian dan penelusuran pada struktur data list & tree
//  4.digunakan b.pemrograman yg tidak punya looping (Haskel, Erlang, Prolog, dll)
//  5.pembuatan game, dll
// -----------------------------------------------------------------------------------
//
// 15. perbandingan Function declaration & function expression
// -struktur function declaration : function namaFunction (parameterList opt) {functionBody}
//  lebih fleksibel(dpt ditulis dimanapun) karena ada konsep Hoisting.
//  Mudah dipahami.
// -struktur function expression : var eks = function namaFunction opt (parameter opt) {functionBody}
//  Biasa disimpan kedalam sebuah variabel.
//  Harus didefiniskan terlebih dahulu sebelum dipanggil.
//  Lebih powerfull: (sebagai closure, sebagai argument u function lain,
//                   IIFE(Immediately Invoked Function Expression) ).
// ----------------------------------------------------------------------------------------
// 16. Array (variabel jamak) = tipe data yg digunakan u mendeskripsikan kumpulan elmen (nilai / variabel)
//  -yg tiap tiap elmennya meiliki index, index dimulai dari nol(0)
//  -sebuah variabel yg bisa menampung lebih dari 1 nilai dengan tipe data yg sama ataupun berbeda
//  -contoh penulisan array : var hari = ["senin"(index-0),"selasa"(index-1),"rabu"(index-2)];
//  -kenapa array?
//      1.mempermudah pengelolaan penelusuran & pencarian nilai / value / data
//      2.manajemen memory
//  -kumpulan pasangan key(index) dan nilai / key and value pair
//  -Array pada javascript bertipe object
//  -Array pd js memiliki fungsi length u menghitung jumlah elemen didalamnya
//  -elmen pada array boleh punya tipe data yg berbeda
//  1.key and value pair
//  -didalam array bisa menyimpan tipe data yg berbeda, bisa simpan function expression.
//  -bisa juga masukkan array didalam array, jadi array multi dimensi
// -Manipulasi array
//  1.menambah elemen pd array
//  2.menghapus elemen pd array
//  3.menampilkan seluruh isi array
//
// -Method untuk membantu array
//  1.length = u tahu berapa jml elemen pd array
//  2.join(masukan pemisahnya bisa="-",dll) = menggabungkan seluruh array dan mengubah jadi string
//  3.push (menambah bisa beberapa elemen array di akhir)
//  4.pop (menghilangkan elemen terakhir sebuah array satu-persatu)
//  5.unshift (menambah bisa beberapa elemen array di awal)
//  6.shift (menghilangkan elemen pertama sebuah array)
//  7.slice(indexAwal, indexAkhir) = (mengiris / mengambil beberapa bagian array u jadi array baru)
//      aturan slice yg terakhir tak diambil jadi jika ingin ambil 2, maka indexAkhirnya harus 3
//      contoh var arr2 = arr.slice(2, 4); = ambil array index-2 & 3 dari arr ke arr2
//  8.splice(indexAwal, mauDihapusBerapa(opt), elemenBaru(opt), elBaru2, ...) = (menyambung / menambal array)
//      contoh splice = arr.splice( 2(posisiIndex), 0(tak da yg dihapus), "bud"(el baru) )
//  9.forEach = loop pada array
//  contoh =
//      var angka = [1,2,3,4,5,6,7,8];
//      angka.forEach(function (e) {
//        console.log(e);
//      });
//  contoh lain =
//      var nama = ["jaja", "gugu", "kaka"];
//      nama.forEach(function (e, i) {
//        console.log("Mahasiswa ke-" + (i + 1) + " adalah: " + e);
//      });
//  10.map  = loop pada array, sama seperti forEach tapi better
//  contoh =
//      var angka1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
//      var angka2 = angka1.map(function (e) {
//        return e * 2;
//      });
//      console.log(angka2.join("\n"));
//  11.sort (mengurutkan isi array)
//  contoh =
//      var angka1 = [1, 2, 4, 5,20,10, 3, 8, 9, 6, 7];
//      angka1.sort(function (a,b){
//          return a-b;
//      });
//      console.log(angka1.join("\n"));
//  -hati2 sort diatas akan mengurutkan sesuai urutan depan jadi diperlukan sebuah function perbandingan angka
//  12.filter = mencari elmen pada array(banyak nilai)
//      var angka1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
//      var angka2 = angka1.filter(function (x) {
//        return x >= 5;
//      });
//      console.log(angka2.join(" "));
//  maka hasilnya = 5 6 7 8 9
//  13.find = mencari elemen pada array(satu elemen)
//      var angka1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
//      var angka2 = angka1.find(function (x) {
//        return x >= 5;
//      });
//      console.log(angka2);
//  maka hasilnya = 5. dan u find tidak bisa pake (.join) karena hasilnya bukan 1 / hanya satu nilai
//  -note : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
// ---------------------------------------------------------------------------------
//
// 17. object (kumpulan nilai sama dengan array, tapi punya nama bukan index)
// -jika array pakai kurungSiku[], object pakai kurungKurawa{}
//
// -cara buatnya secara sedrehana =
//      var mhs = {
//        nama : "rizal",
//        lulus : true
//      }
// -variabel di dlm object disebut properti dipisah dengan tanda koma(,)
// -bisa memasukkan function di dalam object biasa disebut dengan method
//
// -contoh lebih kompleks dengan beberapa cara pemanggilannya
//      var mhs = {
//        nama: "rizal",
//        umur: 20,
//        ips: [3.6, 3.9],
//        alamat: {
//            jalan: "KH. Hasan Arif",
//            kp: "babakan cibudug",
//            kab: "garut",
//        },
//      };
//      console.log(mhs.alamat);
//      console.log(mhs["umur"]);
//      console.log(mhs.ips[1]);
//      console.log(mhs.alamat.kp);
//
// -cara membuat object
//  1.object literal seperti 2 contoh diatas
//      var mhs_1 = {
//        // key : value,
//        nama: "rizal",
//        nim: "2306142",
//        email: "2306142@itg.ac.id",
//        jurusan: "teknik informatika",
//      };
//
//  2.object: function declaration
//      function buatObjectMhs(nama, nim, email, jurusan) {
//        // buat object kosong
//        var mhs = {};
//        // isi object dengan parameter diatas
//        mhs.nama = nama;
//        mhs.nim = nim;
//        mhs.email = email;
//        mhs.jurusan = jurusan;
//        // kembalikan nilai objectnya
//        return mhs;
//      }
//      // tampung function ke sebuah variabel
//      var mhs_3 = buatObjectMhs(
//        // masukkan nilai(argument) sesuai urutan parameter
//        "ahmad",
//        "2306143",
//        "2306143@itg.ac.id",
//        "teknik informatika"
//      );
//      console.log(mhs_3);
//
//  3.constructor function (keyword new & this) (ini yg akan sering dipakai)
//      function Mahasiswa(nama, nim, email, jurusan) {
//        this.nama = nama;
//        this.nim = nim;
//        this.email = email;
//        this.jurusan = jurusan;
//      }
//      var mhs_4 = new Mahasiswa(
//        "asep",
//        "2306140",
//        "2306140@itg.ac.id",
//        "teknik informatika"
//      );
//      console.log(mhs_4);
//  4.object.creat() (pakai method .creat() )
// ----------------------------------------------------------------------------------
//
// 18. this = sebuah keyword special yg otomatis di definisikan pada setiap function/object
// -pembuatan object harus sesuai dengan context (sesuai dengan keadaan) dimana contextnya berbeda2
// -disebut dengan object global == window
// -this pada function declaration contextnya mengembalikan object global
// -this pada object literal contextnya mengembalikan object yg bersangkutan / object itu sendiri
// -this pada construktor contextnya mengembalikan object yg baru dibuat
// ----------------------------------------------------------------------------------
