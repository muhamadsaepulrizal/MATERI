// note: di js var diganti dengan let
// var = akan menerapkan sebuah konsep hoisting atau function scope
// let = akan error jika console dulu lalu let i = 10, seperti dibahasa lain atau jadi block scope
// const = block scope, tapi conts ini jadi menetapkan nilai tapi gak akan pernah kira rubah nilainya / konstanta
//      bisa diganti asalkan jangan merubah semuanya
// -----------------------------------------------------------------------------------------------
// 1. Cara membuat Object:
//  -object literal (tak efektif untuk object yg banyak)
//      let mhs = {
//        nama: "rizal",
//        energi: 10,
//        makan: function (porsi) {
//          this.energi = this.energi + porsi;
//          console.log(`hallo ${this.nama}, selamat makan`);
//        },
//      };
//      console.log(mhs.makan(2));
//      console.log(mhs);
//
//  -function declaration (harus di return object didalam functionnya yg kosong itu lho)
//   tidak hemat memory dibalik layar.
//      function Mahasiswa(nama, energi) {
//        let mhs = {};
//        mhs.nama = nama;
//        mhs.energi = energi;

//        mhs.makan = function (porsi) {
//          this.energi += porsi;
//          console.log(`hallo ${nama}, selamat makan sebanyak ${porsi} porsi`);
//        };

//        mhs.main = function (jam) {
//          this.energi -= jam;
//          console.log(`${nama} main ${jam}jam`);
//        };
//        return mhs;
//      }
//      let rizal = Mahasiswa("rizal", 10);
//      console.log(rizal);
//      console.log(rizal.makan(5));
//      console.log(`energi sekarang ${rizal.energi}`);
//      let kaka = Mahasiswa("kaka", 20);
//      console.log(kaka);
//      console.log(kaka.main(10));
//      console.log(`energi sekarang ${kaka.energi}`);

//  -construktur function (mirip function declaration hanya pakai this new)
//   tak perlu declar object didalamnya, dan mhs seperti diatas diganti this.
//   dan dipemanggilan function pakai (new) dulu
//      function Mahasiswa(nama, energi) {
//        this.nama = nama;
//        this.energi = energi;

//        this.makan = function (porsi) {
//          this.energi += porsi;
//          console.log(`hallo ${nama}, selamat makan sebanyak ${porsi} porsi`);
//        };

//        this.main = function (jam) {
//          this.energi -= jam;
//          console.log(`${nama} main ${jam}jam`);
//        };
//      }
//      let asep = new Mahasiswa("asep", 10);
//      console.log(asep);
//      console.log(asep.main(5));
//      console.log(`sisa energi ${asep.energi}`);

//  -object create()
//   ribet karena harus mengurus dua object.
//      const methodMahasiswa = {
//        makan: function (porsi) {
//          this.energi += porsi;
//          console.log(`hallo ${this.nama}, selamat makan sebanyak ${porsi} porsi`);
//        },
//        main: function (jam) {
//          this.energi -= jam;
//          console.log(`${this.nama} main ${jam}jam`);
//        },
//        tidur: function (jam) {
//          this.energi += jam * 2;
//          console.log(`${this.nama} selamat tidur`);
//        },
//      };
//      function Mahasiswa(nama, energi) {
//        let mhs = Object.create(methodMahasiswa);
//        mhs.nama = nama;
//        mhs.energi = energi;
//        return mhs;
//      }
//      let agum = Mahasiswa("agum", 20);
//      console.log(agum);
//      console.log(agum.makan(10));
//      console.log(`energi sekarang ${agum.energi}`);
//---------------------------------------------------------------------------------
//
// 2. prototype
//  -(.prototype) buat cek didalamnya ada apa saja
//  -Object dengan prototype inherit
//  -dengan adanya prototype kita tak perlu membuat (const methodMahasiswa) seperti diatas
//      // perubahan diatas dengan Object.creat() + prototype
//      // yg dikelola objectnya cuma 1 tingal ambil prototypenya
//      function Mahasiswa(nama, energi) {
//        //let mhs = Object.create(methodMahasiswa); //Object.create() digunakan untuk menghubungkan dengan method lain
//        //let mhs = {}
//        //let this = Object.create(Mahasiswa.prototype); //ini yg sebenarnya terjadi dibelakang layar jika pakai this
//        this.nama = nama;
//        this.energi = energi;
//        //return mhs;
//        //return this //terjadi dibelakang layar jika pakai this
//      }
//      // ini nempel dengan object mahasiswa diatas
//      Mahasiswa.prototype.makan = function (porsi) {
//        //protoype sebagai pewarisan antara Mahasiswa dengan makan(dll)
//        this.energi += porsi;
//        return `hallo ${this.nama} selamat makan`;
//      };
//      Mahasiswa.prototype.main = function (jam) {
//        this.energi -= jam;
//        return `halllo ${this.nama} selamat bermain`;
//      };
//      Mahasiswa.prototype.tidur = function (jam) {
//        this.energi += jam * 2;
//        return `hallo ${this.nama} selamat tidur`;
//      };
//      let rizal = new Mahasiswa("rizal", 10);
//      console.log(rizal);
//      console.log(rizal.makan(10));
//      console.log(rizal.energi);
//      console.log(rizal.main(5));
//      console.log(rizal.energi);
//      console.log(rizal.tidur(5));
//      console.log(rizal.energi);

//  -versi class diatas, jadi versi class ini sama aja jalannya seperti prototype diatas cara kejanya
//   hanya dibungkus class supaya lebih bisa dipahami
//      class Mahasiswa {
//        constructor(nama, energi) {
//        this.nama = nama;
//        this.energi = energi;
//        }
//
//        makan(porsi) {
//           this.energi += porsi;
//           return `hallo ${this.nama} selamat makan`;
//        }
//        main(jam) {
//           this.energi -= jam;
//           return `hallo ${this.nama} selamat bermain`;
//        }
//        tidur(jam) {
//           this.energi += jam * 2;
//           return `hallo ${this.nama} selamat tidur`;
//        }
//      }
//      let rizal = new Mahasiswa("rizal", 20);
//      console.log(rizal);
//      console.log(rizal.main(10));
//      console.log(rizal.energi);
//      console.log(rizal);
//      console.log(rizal.makan(20));
//      console.log(rizal.energi);
//      console.log(rizal);
//      console.log(rizal.tidur(10));
//      console.log(rizal.energi);
// --------------------------------------------------------------------------------
//
// 3. Closures u contoh cek file lan_3.js
// -mrupakan kombinasi antara function dan lingkungan leksikal (lexical scope) di dlm function tsb.
// -sebuah function ketika memiliki akses ke parent scope-nya, meskipun parent scope-nya sudah selesai di eksekusi.
// -sebuah function dikembalikan o/ function yg lain, yg punya akses ke lingkungan saat ia diciptakan.
// -sebauh function yg sebelumnya sudah memiliki data, hasil dari function yg lain.
// -kenapa closures
//  1. untuk membuat function factories
//  2. untuk membuat privat method

// -lexical scope
// -Execution Context, Hoisting, Scope
//  1.fase pada Execution Context (cek di file lan_2.js)
//  -creation
//  -execution
// --------------------------------------------------------------------------------
//
// 4. Arrow function (bentuk lain yg lebih ringkas dari function expresion)
// -contoh sederhana
//      let tampilPesan = (nama) => {
//        console.log(`hallo ${nama}`);
//      };
//      tampilPesan("koko");
//  1. tulisan function-nya hilang terus setelah (parameter) tulis (=>) lalu body {}
//  2. kalo parameternya 1 gak usah pake kurung, kalo 2 baru harus pake kurung
//  3. lebih ringkasnya lagi gak perlu pakai return, dan kurung kurawa
//
//  4. berikut syntax lebih ringkas dari yg diatas: disebut implisit return
//      const tampilPesan = (nama) => `hallo ${nama}`;
//      console.log(tampilPesan("baba"));
//
// -contoh lain, parameter 2
//      const tampilNama = (nama, waktu) => {
//        return `Selamat ${waktu}, ${nama}`;
//      };
//      console.log(tampilNama("rizal", "sore"));
//
// -contoh lain arrow function: u mengetahui jumlah huruf nama di array
//      let mhs = ["kaka", "rizal", "jojo"];
//      let jmlHuruf = mhs.map(function (nama) {
//        return nama.length;
//      });
//      console.log(jmlHuruf);
//  1.jmlHuruf diubah ke arrow function jauh lebih ringkas, seperti berikut
//      let jmlHuruf = mhs.map((nama) => nama.length);
//      console.log(jmlHuruf);
//  2.jika ingin dikembalikan dalam bentu object{} si ({}) dibungkus dengan kurung supaya dianggap obejct
//      let jmlHuruf = mhs.map((nama) => ({ nama: nama, jumHur: nama.length }));
//      console.table(jmlHuruf); //.table artinya tampilan di console berupa table
// ----------------------------------------------------------------------------------
//
// 5. Higher Order Function
// -Function yg beroperasi pada function yg lain. Baik itu dugunakan dalam argument, maupun sebagai return value.
// -contoh sederhana
//      //function kerjakanTugas bisa disebut Higher Order Function
//      //function yg disimpan sebagai argument disebut callback
//      function kerjaTugas(matkul, selesai) {
//        console.log(`Mulai mengerjakan Tugas ${matkul}`);
//        selesai(); //fungsi dijadikan parameter argument
//      }
//      function selesai() {
//        console.log("Tugas Selesai");
//      }
//      kerjaTugas("js lanjut", selesai);
// -kenapa Higher Order Function perlu?
//  1. Abstraksi (kode yg dibuat lebih sederhana/simple)
// -yg sering digunakan dalam Higher Order Function: filter, map, reduce
// -sebuah prototype dari array
//      const angka = [-1, 8, 9, 1, 4, -5, -4, 3, 2, 9];
//      // mencari angka >= 3
//      // pakai for
//      const newAngka = [];
//      for (let i = 0; i < angka.length; i++) {
//        if (angka[i] >= 3) newAngka.push(angka[i]);
//      }
//      console.log(newAngka);
//
//      // filter (cek satu persatu),
//      // lalu pakai juga arrow function, function hilang, return hilang, kurung kurawa diganti (=>)
//      const newAngka = angka.filter((a) => a >= 3);
//      console.log(newAngka);
//
//      // map
//      // kalikan samua angka dengan 2
//       const newAngka = angka.map((a) => a * 2);
//       console.log(newAngka);
//
//      //reduce (melakukan sesuatu terhadap semua elemen array / mengelola), parameternya harus 2
//      //jumlahkan seluruh elemen pada array
//      //curentValue = elemen array yg sedang di loop, accumulator = hasil dari prosesnya
//      //dibawah ada 0 dimana 0 adalah nilai awal yg bisa diobah,
//      //karena disini saya 0-nya tidak ingin mengganggu operasi saya tidak rubah
//       let newAngka = angka.reduce(
//         (accumulator, currentValue) => accumulator + currentValue, 0
//       );
//       console.log(newAngka);
//
//      // menggabungkan filter,map,reduce diatas
//      // method chaining (menggabungkan fungsi fungsi / berantai)
//      // cari angka > 5, lalu hasilnya kalikan 3, lalu jumlahkan semua elemen
//       const hasil = angka
//         .filter((a) => a > 5)
//         .map((a) => a * 3)
//         .reduce((acc, cV) => acc + cV);
//       console.log(hasil);
// ------------------------------------------------------------------------------------------
//
// 6. tamplate literals
// -adalah string literal yg memungkinkan adanya expression(memasukkan let,dll) didalamnya
// -kenapa tamplate literal
//  1. multi-line string (enter / \n) tanpa harus menutup stringnya
//  2. embeded expression (menambahkan ${expression} ). expression (bisa operasi matematika, var, let, function dll)
//      bisa juga seperti ini =
//      const x = 11;
//      console.log(`${x % 2 == 0 ? "genap" : "ganjil"}`);
//  3. HTML fragments = cek file lan_7.js
//      const mhs = {
//        nama: "rizal",
//        umur: 20,
//        nim: "2306142",
//      };
//      let el = `<div class="mhs">
//           <h2>${mhs.nama}</h2>
//           <span class="nim>${mhs.nim}</span>
//      </div>`;
//      console.log(el);
//  4. expression interpolation
//  5. tagged tamplate  tag = `string text ${expression} `
//  -bisa di cek di file lan_8.js untuk contohnya
//  -bentuk yg lebih kompleks dari tamplate literals, memungkinkan kita u membaca lewat sebuah function
//  -kenapa perlu ini?
//   1. escaping HTML tags
//   2. translation & internationalization (alih bahasa)
//   3. styled components
// ----------------------------------------------------------------------------------------------------------
