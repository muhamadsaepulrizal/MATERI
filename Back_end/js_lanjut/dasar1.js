// program adalah kumpulan / instruksi yg dirancang agar komputer dpt berperilaku sesuai dengan ketentuan
// dengan tujuannya untuk menyelesaikan sebuah pekerjaan
// console.log("hello world");
// khusus untuk web
// tak ada integer yg ada float (pecahan) angka yg dpt ditampung 64-bit
// koma pakai titik(.) di javascript max 17 digit dibelakang koma
// jangan pernah mengawali angka dengan nol (0) karena bisa dianggap bil oktal
// jangan pernah juga mengawali angka dengan 0x karena bisa dianggap hexadesimal
// ada angka spesial infinity, -infinity, NaN = pembagian dengan 0, 0 dengan 0, pemnbagian dengan angka
// hati2 juga jika pembagian sebuah bilangan dgn string tapi didalam string ada angka
// 2/0 = infinity, 2/"hallo"= NaN,

// 1. operator pada  javascript
// operator binary: butuh 2 operand(nilai) (operand operator  operand)
// aritmatika = +, -, *, /, modulus(%), . urutan operasi berlaku (kukabataku)
// penugasan (assignment) = tanda sama dengan (=) memberi nilai ke var,
//      += (x=10, x+=1 = 11), -=, *=, /=, %=
// perbandingan = komparasi hasillnya boolean (true/false)
//      ==(sama dengan), !=(tidak sama dengan),
//      operator identitas (tipe datanya dibandigkan): ===(strict sama dengan), !==(strict tidak sama dengan)
//      >(lebih besar dari), <(lebih kecil dari), >=(lebih besar sama dengan), <=(lebih kecil sama dengan)
// logika = menentukan logika dari beberapa ekspresi dibawah:
//      && / & = and (semua kondisi harus benar baru nilainya true)
//      || = or (salah satu kondisi benar bisa true)
//          (bisa juga dipakai di else if jika ingin 2 kondisinya (yg berbeda kondisi) dalam satu else if)
//      ! = not (membalikan hasil dari true jadi false)
// string = dengan tanda plus(+) bisa menggambungkan string
//      jika (+) salah satu string satu angka maka hasil akan dibaca sebagai string

// operator ternary : butuh 3 operand
// kondisional = u dilakukan pengecekan pada sebuah kondisi dan menentukan nilai yang dihasilkan
//      ketika kondisinya bernilai true / false cara penulisannya :
//      (kondisi) ? benar : salah

// operator unari: butuh 1 operand (operator operand)/(operand operator)
// typeof = u mengetahui tipe data apa dari nilai yg dimasukkan
// -------------------------------------------------------------------------------------------------------------

// 2. Tipe data string = u merepresentasikan data tekstual
//- caranya membungkus teks dengan "teks" / 'teks'
//- bisa juga kombinasi : "hari ini hari jum'at" / 'dilarang "buang sampah" disini'
//- ini dilarang = ""gerakan anti korupsi" dilakukan serentak jum'at"
//- cara mengatasinya pakai escape character tanda \" dan \' contoh seperti ini
//- '"gerakan pungut sampah" dilaksanakan pada hari jum\'at'
//- macam macam escape character sebagai string:
//-     \0 (karakter null), \' ('), \" ("), \\(\), \n(newline), \t(tab), \b(backspace).
//      \uXXX(unicode) : \u00A9 = tanda copyright, \u00AE = tanda R bulat, \u00B1 = tanda kurang lebih,
//      \u00B5 = 4 terbalik, \u2122 = TM, dll
//- dalam string ada concatenation (+) = menggabungkan 2 atau lebih string
//- dalam string ada sebuah fungsi (.length) = menghitung panjang string (spasi dihitung)
// ----------------------------------------------------------------------------------------------------------------

// 3. boolean = tipe data u merepresentasikan logika true(1/benar) atau false(0/salah)
//- penemu george boole ahli math bidang logika
//- biasa dugunakan di pengkondisian, u mnentukan aksi yg berbeda dan mengatur alur kendali program
//- bisa dilakukan pengecekan trua/false dengan fungsi berikut = Boolean(nilai yg dibandingkan);
//- truthy(mengasilkan true) = true, non-zero number, "string", object, arrays, functions
//- falsy(menghasilkan false) = false, 0, "",
//      undifined (sebuah tipe yg dihasilkan ketika mendeklarasikan variabel yg belum diisi nilai),
//      null (nilai kosong yg bisa diberikan pada sebuah variabel), NaN
// ------------------------------------------------------------------------------------------------------------

// 4. Variabel = sebuah wadah yg punya nama, dan digunakan u menyimpan nilai dan nilainya dpt diubah-ubah
//- harus paham 3 berikut: deklarasi, inisialisasi, assignment
//      1. deklarasi = mendaftarkan var ke dalam lingkup yg sesuai
//      2. inisialisasi = menyediakan memori u variabel
//      3. assignment = menetapkan nilai yg spesifik kedalam variabel
// contoh u menghindari hal-hal yg tidak diinginkan:
// var x; (deklarasi dan inisialisai)
// x = 20; (assignment)
// contoh variabel dengan keyword lain selain var: let, const yg masing-masing punya perilaki berbeda
// aturan memberi nama variabel:
//- gak boleh pake spasi jika lebih dari 1 pakai(_), boleh pake angka tapi tidak diawal angkanya,
//  boleh pake simbol khusus juga
//  penulisan variabel yg sering digunakan oleh prorammer javascript = var namaVariabelPanjang / camelCase
//- kata yg tak boleh dipakai sebagai nama variabel (keyword & reserved word)
//  atau sebuah kata yg ada sebagai syntax atau fungsi di javascript
//- shorthand u menyingkat penulisan variabel seperti berikut u variabel berikutnya diselang pake koma(,):
//   var nama = "rizal",
//     umur = 31,
//    lulus = true;
//- variabel scope =
// -------------------------------------------------------------------------------------------------------------

// 5. menulsi script di web
//- internal = langsung di html
//      1.penulisan bisa dibagian head dengan tag script
//      2.dibody dibagian akhir sebelum tutup tag body
//- eksternal = file terpisah dengan format file .js contoh (script.js)
//- cara menghubungkan javascript ke html pakai tag script di akhir sebelum tutup tag body dengan tambahan src
//      contoh <script src="namaFile.js"> </script>. relative url berlaku
// -------------------------------------------------------------------------------------------------------------
//
// 6. popUp box/ dialog box
//- alert = memberi pesan sederhana pada user berbentuk kotak dengan tombol ok
//- prompt = sama dengan alert tapi ada teks box u memasukkan inputan (megembalikan inputan user)
//      segala yg diinputkan oleh prompt berupa string,
//      jika ingin angka maka tambahkan syntax (paseInt) sebelum syntax prompt
//- confirm = sama seperi alert tapi fungsinya untuk memberikan konfirmasi (mengembalikan nilai boolean)
//------------------------------------------------------------------------------------------------------------
//
//7. control flow = alur kendali dari sebuah program
//- normal flow = apabila program punya lebih dari 1 statement, maka statement tsb akan dieksekusi
//      dari atas kebawah atau dari kiri kekanan
//- selain normal flow porgram juga dpt diatur dengan pengulangan & pengkondisian
//- pengulangan (loop/iterasi) = mengeksekusi sebauh statement secara berulang
//      for, while, do while
//- pengkondisian(percabangan) = program dpt memilih mengeksekusi statement yg berbeda sesuai dengan kodisi yg diberikan
//      (if) (if | else) (if |else if |else) (switch)
//--------------------------------------------------------------------------------------------------------------
//
//8. pengulangan = for, while, do while
//- contoh syntax sederhana while
//      var ulang = 1; / nilai awal
//      while (ulang <= 5)/ kondisi terminasi {
//        console.log("hello world"); / aksinya
//        ulang++; / increment(penambahan nilai awal) atau decrement(pengurangan nilai awal)
//      }
// - contoh syntax sederhana for
//      for (nilaiAwal = 1; nilaiAwal <= 5; nilaiAwal++) {
//        console.log("hello for" + nilaiAwal + " x");
//      }
// --------------------------------------------------------------------------------------------------------------
//
// 9. tabel penelusuran
//-untuk cek cara kerja program kita
//-caranya tuliskan varabel-variabel yg kemungkinan berubah,kondisi, dll cara penulisan nya ada di hpanda
// --------------------------------------------------------------------------------------------------------------
//
// 10. pengkondisian = (if) (if | else) (if |else if |else) (switch)
//- syntax dasarnya
//      if(kondisi){
//        aksi
//      }
//      ...
//- sytntax lain if|else:
//       var angka = 5;
//       if (angka % 2 == 0) {
//         console.log("genap"); //alert for web
//       } else {
//         console.log("ganjil");
//       }
// -note : ketika salah satu if atau else if dikerjakan yg lain tidak dikerjakan
//      jadi cara kerja pengkondisian hanya 1 kondisi yg dikerjakan jika kondisi yg sesuai ditemukan
//      jika kondisi tidak ditemukan yg sesuai maka else yg akan dikerjakan senagai pilah terakhir (aksi default)
//- switch : mirip if, tapi kondisinya hanya ada 1 dan akan mengecek nilai dari hasil kondisinyas
//      1. berikut syntax sederhana nya:
//          var angka = prompt("masukkan angka: ");
//          switch (angka) {
//            case "1": // case nya string
//              console.log("anda memasukkan angka 1");
//              break;
//            case "2":
//              console.log("anda memasukkan angka 2");
//              break;
//            case "3":
//              console.log("anda memasukkan angka 3");
//              break;
//            default:
//              console.log("angka salah");
//              break;
//          }
//      2. syntax lain sebagai contoh dari switch:
//          var item = prompt(
//            "masukkan nama makanan / minuman: (cth): nasi, daging, susu, hamburger, softdrink: "
//          );
//          switch (item) {
//            case "nasi":
//            case "daging":
//            case "susu":
//              console.log("makanan / minuman SEHAT");
//              break;
//            case "hamburger":
//            case "softdrink":
//              console.log("makanan / minuman TIDAK SEHAT");
//              break;
//            default:
//              console.log("nama makanan / minuman salah");
//              break;
//          }
// - note : u switch hanya bisa memasukkan value di casenya dan tipe datanya harus sama
// -----------------------------------------------------------------------------------------------------------------
//
// 11. funtion = kunci utama
// -sub program yg dapat dipanggil di program lainnya
// -struktur dsar pembentuk javascript
// -untuk membuat sebuah tugas tertentu
// -caranya buat function lalu dipanggil
// -termasuk dalam first class object
// -kepana harus dibuat function?
//      untuk supaya tidak menulis program yg sama berulan - ulang
//      abstraksi
//      modularitas
// -ada 2 kategori function
//  built in function = yg sudah dibuatkan oleh suatu b.pemograman
//  user difined function = yg dibuat sendiri
//
// -funtion declaration
//      function jmlbil(a, b) {
//        var total;
//        total = a + b;
//        return total;
//      }
//
//      console.log(jmlbil(5, 4));
//
// -function ekspresion = ditampung ke variabel
//      var jumbil = function (a, b) {
//        var total;
//        total = a + b;
//
//        return total;
//      };

//      console.log(jumbil(5, 5));
// -struktur function = keywod(function), namaFunction(bebas), parameter() ,bodynya{}, return nilai(opsional)
// -parameter / argument = bahan baku dari sebuah function
//  definisi = variabel yg ditulis dikurung saat dibuat dan digunakan u menampung nilai
//  yg dikirim saat function dipanggil
// -argument = adalah nilai yg dikirim ke parameter tadi saat fungsi dipanggil
// -jadi parameter saat function dibuat & argument saat function dipanggil
//
// note : jika parameter lebih sedikit dari argument, maka argument kelebihannya akan diabaikan(for javascript)
// note : jika parameter lebih banyak dari argument, maka parameter kelebihannya akan diisi dgn nilai undefined
// note : arguments adl array yg berisi nilai yg dikirim saat fungsi dipanggil, manfaatnya dibawah
// contoh: nilai argument yg kelebihan sebenarnya ditampung dalam sebuah array yg namanya arguments
//          function tambah() {
//            return arguments;
//          }
//          var cobaArgu = tambah(5, 10, 20, "hi", false);
//          console.log(cobaArgu);
//
// contoh lain nya: dalam pemanfaatan array arguments pada function
//          function tambah() {
//            var hasil = 0;
//            for (var i = 0; i < arguments.length; i++) {
//              hasil += arguments[i];
//            }
//            return hasil;
//          }
//
//          //dgn manfaat arguments pada fungsi diatas kita bisa input nilai nya bebas untuk operasi penjumlahan
//          var coba = tambah(8, 1, 2, 3);
//          console.log(coba);
//
// ---------------------------------------------------------------------------------------------------------------
// note : dome u javascript supaya bisa berinteraksi dengan elemen html
