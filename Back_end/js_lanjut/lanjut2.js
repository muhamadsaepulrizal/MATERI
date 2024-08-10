// 7. destructuring assignment
// -expression pada js yg membuat kita dpt membongkar nilai pada array / peoperti
//  dari object kedalam variabel yg terpisah.
// -contoh sederhana
//      // contoh dengan array
//      const coba = ["satu", "dua", "tiga"];
//      const [a, b, c] = coba;
//      console.log(a); //satu
//      console.log(b); //dua
//      console.log(c); //tiga
//
//      //contoh dengan object
//      const mhs = {
//        nama: "rizal",
//        umur: 20,
//        email: "2306142@gmail.com",
//      };
//      const { nama, umur, email } = mhs;
//      console.log(nama);
//      console.log(umur);
//      console.log(email);
// -contoh lebih detail cek file lan_9.js
//      // contoh dengan array
//      const coba = ["satu", "dua", "tiga"];
//      const [a, b, c] = coba;
//      console.log(a); //satu
//      console.log(b); //dua
//      console.log(c); //tiga
//      //contoh dengan object
//      const mhs = {
//        nama: "rizal",
//        umur: 20,
//        email: "2306142@gmail.com",
//      };
//      const { nama, umur, email } = mhs;
//      console.log(nama);
//      console.log(umur);
//      console.log(email);

//      // contoh lain array
//      const perkenalan = ["hallo", "nama", "saya", "rizal"];
//      // const [sapa, satu, dua, nama] = perkenalan;
//      // bisa di skip tapi komamya harus tetap ada
//      const [sapa, , , nama] = perkenalan;
//      console.log(sapa);

//      // dipakai untuk swap item
//      let a = 1;
//      let b = 2;
//      [a, b] = [b, a]; //bisa langsung ditukar dengan cara begini
//      console.log(a);

//      // bisa juga return value pada function
//      function coba() {
//        return [1, 2];
//      }
//      // const a = coba(); //tipe a jadi array
//      // console.log(a[1]);
//      // cara diatas bisa langsung dipecah tanpa tulis indexnya saat dipanggail
//      const [a, b] = coba(); //tipe a jadi array
//      console.log(a, b);

//      // rest parameter supaya mengatasi jika elemennya terus bertambah
//      const [a, ...args] = [1, 2, 3, 4, 5];
//      console.log(a);
//      console.log(args[0]); //tapi ini jadi berbentuk array lagi

//      // contoh lain object
//      const mhs = {
//        nama: "rizal",
//        umur: 20,
//      };
//      const { nama, umur } = mhs; //harus sama nama untuk nama, umur untuk umur
//      console.log(nama);

//      // assignment tanpa deklarasi object & const tapi tambah kurung diawal dan diakhir sebelum titik koma
//      ({ nama, umur } = {
//        nama: "rizal",
//        umur: 20,
//      });
//      console.log(nama);

//      // assign ke variabel baru
//      const mhs = {
//        nama: "rizal",
//        umur: 20,
//      };
//      const { nama: n, umur: u } = mhs; //bisa tidak harus sama caranya tambah (:) lalu nama atau singkatan baru
//      console.log(n);

//      // memberikan default value
//      const mhs = {
//        nama: "rizal",
//        umur: 20,
//        email: "2306142@gmail.com",
//      };
//      // bisa memberi default jika tidak ada seperi dibawah, jadi cek dulu ke object kalo gak ada baru default jalankan
//      const { nama, umur, email = "email@default" } = mhs;
//      console.log(email);

//      // memeberi default value + assign ke var baru
//      const mhs = {
//        nama: "rizal",
//        umur: 20,
//      };
//      const { nama: n, umur: u, email: e = "gak ada email bos" } = mhs;
//      console.log(e);

//      // bisa juga pakai rest parameter
//      const mhs = {
//        nama: "rizal",
//        umur: 20,
//        email: "2306142@itg.ac.id",
//      };
//      const { nama, umur, ...args } = mhs; //...args -nya dalam bentuk object
//      console.log(args);

//      // mengambil field pada object, beres dikirim sbg parameter oleh function
//      const mhs = {
//        id: 123,
//        nama: "rizal",
//        umur: 20,
//        email: "2306142@itg.ac.id",
//      };
//      // dibongkar lalu yg diambil hanya id nya, dengan cara di ()parameter masukkan kurungKurawa{properti}
//      function getIdMhs({ id }) {
//        return id;
//      }
//      console.log(getIdMhs(mhs));
// ------------------------------------------------------------------------------------------
//
// 8. Destructuring Function cek file lan_10.js
// -contoh sederhana
//      function tambahKali(a, b) {
//        return [a + b, a * b];
//      }
//      // ini agak ribet karena harus tuliskan indexnya
//      const jumlah = tambahKali(2, 3);
//      console.log(jumlah[0]);
//      console.log(jumlah[1]);

//      // case 1
//      // kita pecah aja / destructuring
//      const [tambah, kali] = tambahKali(2, 3);
//      console.log(kali);

// -note = u array urutan berpengaruh jika ingin output sesuai & object tak perlu berurutan
// -berikut contoh sederhananya
//      function opMath(a, b) {
//        return {
//          tambah: a + b,
//          kurang: a - b,
//          kali: a * b,
//          bagi: a / b,
//        };
//      }
//      const { kali, kurang, bagi, tambah } = opMath(5, 5); //disini tidak berurutan tapi terpacu pada nama
//      console.log(bagi);
// // 1. destructur return value
//      function tambahKali(a, b) {
//        return [a + b, a * b];
//      }
//      // ini agak ribet karena harus tuliskan indexnya
//      const jumlah = tambahKali(2, 3);
//      console.log(jumlah[0]);
//      console.log(jumlah[1]);

//      // case 1
//      // kita pecah aja / destructuring
//      const [tambah, kali] = tambahKali(2, 3);
//      console.log(kali);

//      // case 2
//      function opMath(a, b) {
//        return {
//          tambah: a + b,
//          kurang: a - b,
//          kali: a * b,
//          bagi: a / b,
//        };
//      }
//      const { kali, kurang, bagi, tambah } = opMath(5, 5);
//      console.log(bagi);

// // 2. destructur arguments
//      // case 3
//      const mhs1 = {
//        nama: "rizal",
//        umur: "20",
//        email: "2306142@itg.ac.id",
//        nilai: {
//          tugas: 80,
//          uts: 85,
//          uas: 75,
//        },
//      };
//      // destructur dipecah object mhs1 disini hanya nama,umur pakai kurungKurawa
//      // lalu kita bisa lakukan destructur bersarang seperti dibawah pemecahan dilakukan pakai tanda (:)
//      function cetakMhs({ nama, umur, nilai: { uas } }) {
//        return `Hallo nama saya ${nama}, umur saya ${umur} tahun, dan nilai uas saya adalah ${uas}`;
//      }
//      console.log(cetakMhs(mhs1)); //object masuk kesini
// -------------------------------------------------------------------------------------
//
// 9. Looping baru = for..of & for..in
// - for..of
// mengulang atau menelusuri object2 yg iterable
// seperti = string, array, arguments/NodeList, typeArray, map, set, user-defined itelables
//      // case 1 penggunaan for..of ke array, karena array itu iterables
//      // const mhs = ["rizal", "koko", "agus"];
//      // for biasa
//      for (let i = 0; i < mhs.length; i++) {
//        console.log(mhs[i]);
//      }

//      //forEach, khusu untuk array
//      //forEach juga bisa punya 2 parameter satunya lagi untuk index, jadi bisa seperti dibawah
//      mhs.forEach((m, i) => {
//        console.log(`${m} adalah mahasiswa ke-${i + 1}`);
//      });

//      // for..of = kalau for..of secara default gk punya index
//      // tapi tetep bisa diakalin caranya pakai .entries() setelah array-nya.
//      // didepan deklarasikan indexnya dulu, baru var untuk menampung isi array-nya contoh = [i,m]
//      for (const [i, m] of mhs.entries()) {
//        console.log(`${m} adalah mhs ke-${i + 1}`);
//      }

//      // case 2 penggunaan pada string, karna string iterables
//      // tapi string gak bisa pake forEach, karna forEach khusus untuk array
//      // const nama = "rizal";
//      // for..of. akan me loop tiap-tiap karakter dalam string-nya
//      for (const n of nama) {
//        console.log(n);
//      }

//      // case 3 penggunaan pada NodeList, melakukan QRY pada DOM
//      // const liNama = document.querySelectorAll(".nama");
//      // pakai forEach
//      liNama.forEach((n) => console.log(n.textContent));

//      // pakai for..of
//      for (let n of liNama) {
//        console.log(n.textContent);
//      }

//      // loop arguments disini kita bisa tak pakai parameter tapi memanfaatkan for..of
//      function jmlAngka() {
//        let jml = 0;
//        for (a of arguments) {
//          jml += a;
//        }
//        return jml;
//      }
//      console.log(jmlAngka(1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5));
// - for.. in = perhatikan kata in artinya didalam
// hanya untuk properti pada object
//      const mhs = {
//        nama: "rizal",
//        umur: 20,
//        email: "2306142@itg.ac.id",
//      };
//      // jika ingin ambil valuenya kita tinggal jadikan mhs sebagai index, m untuk menangkap valeunya
//      for (m in mhs) {
//        console.log(mhs[m]);
//      }
// --------------------------------------------------------------------------------------
//
// 10. spread operator
// -cek file = lan_12.js & index_12.html
// -notasi sama seperti rest parameter yaitu pakai (...)
// -spread operator
//  memecah (expand / unpack) iterables menjadi single element, yg banyak isinya dipecah jadi satu.
//  ietables object = string, array, arguments/NodeList, TypedArray, map, set, User-defined iterables.
//  untuk apa spread operator?
//  1. menggabungkan 2 array
//      // case 1 pada gabungkan array
//      // buat array mhs
//      const mhs = ["kaka", "ucup", "baba"];
//      console.log(...mhs[0]); //maka akan memecah kaka = k a k a
//      // buat satu lagi array dosen
//      const dosen = ["jaja", "ajum", "agus"];
//      // lalu gabungkan aray mhs & dosen ditampung ke array lagi u menampung hasilnya
//      // lalu saktinya pakai spread operator ditengah2 kita bisa menambahkan elemen array baru
//      const mhsDosen = [...mhs, "nana", ...dosen];
//      console.table(mhsDosen);

//      // bisa juga pakai cara lain prototype array yaitu concat u menggabungkan 2 array
//      const orang = mhs.concat(dosen);
//      console.log(orang);

//  2. men copy array
//      // case 2 meng copy array
//      const mhs = ["kaka", "ucup", "baba"];
//      // // dengan cara ini array asal juga berubah jadi bukan men copy, lalu hasil copy bisa dirubah
//      // // karena kita ingin merubah-rubah array copyan-nya
//      // const mhs1 = mhs;
//      // mhs1[0] = "akak";
//      // console.log(mhs1);
//      // console.log(mhs); //ikut berubah

//      // caranya seperti ini yg benar
//      // maka mhs1 benar2 copyan dan bisa di edit tanpa ganggu array asalnya
//      const mhs1 = [...mhs];
//      mhs1[0] = "akak";
//      console.log(mhs1);
//      console.log(mhs); //tak ikut berubah

//  3. mengambil elemen html jadi array
//      //mengambil elemen html jadi array
//      const liMhs = document.querySelectorAll("li");
//      //pakai loop for
//      const mhs = [];
//      for (var i = 0; i < liMhs.length; i++) {
//        mhs.push(liMhs[i].textContent);
//      }
//      console.log(mhs);
//      //pakai map lebih simple
//      //map hanya untuk array u ubah ke array pakai spread (...)
//      const mhs = [...liMhs].map((m) => m.textContent);
//      console.log(mhs);

//      // mengubah perilaku elemen html
//      // melakukan animasi gerak setiap huruf pada nama
//      const nama = document.querySelector(".nama");
//      const hurufNama = [...nama.textContent]
//        //membungkus huruf dengan span
//        .map((hN) => `<span>${hN}</span>`)
//        //marubah array jadi string biasa
//        .join("");
//      //timpa hurufNama ke nama sehinggah h1 tiap huruf dibungkus span
//      nama.innerHTML = hurufNama;
// -------------------------------------------------------------------------
//
// 11. rest parameter cek file = lan_13.js
// -notasi sama pakai (...)
// -merepresentasikan (menangkap) argument pada function dengan jml yg tidak terbatas menjadi sebuah array
// rest parameter = untuk mengambil sisa parameter jadi di taruh diakhir
// contoh sederhana
// function myFunc(...args) {
//   //ini jika hanya ada beberapa parameter, sisanya ditangkap (...args)
//   return `a = ${a}, b = ${b}, sisanya dalam(args) = ${args}`;

//   //bisa juga langsung tangkap semua pakai (...args) jadi tak perlu khawatir berapa memasukan argument dibawah
//   //bentuk (...args) adalah array
//   return args.join(" ");

//   //bisa juga pakai arguments, karena arguments itu menangkap semua argument dibawah
//   //caranya laangsung return, bentuk (arguments) adalah object
//   //bisa juga pakai Array.from(), untuk jadi array
//   return arguments;

//   //atau bisa juga pakai spread operatot si arguments dimasukkan ke spread operator
//   return [...arguments];
// }
// console.log(myFunc(1, 2, 3, 4, 5));

// contoh 2 menjumlahkan
// // pakai args & for..of & reduce
// function jumlahkan(...args) {
//   let total = 0;
//   // pakai for..of
//   for (const a of args) {
//     total += a;
//   }
//   return total;
//   // pakai reduce
//   return args.reduce((hasil, a) => hasil + a);
// }
// console.log(jumlahkan(1, 2, 3, 4, 5));

// // array destructuring dengan rest parameter
// // rulenya nama pertama ketua, kedua waketua, sisa anggota
// const kel1 = ["kaka", "ajat", "baba", "dodo", "joko"];
// const [ketua, wakil, ...anggota] = kel1;
// console.log(anggota)

// // object desctructuring dengan rest parameter
// // pisahkan pm dan sisa kelompoknya
// const team1 = {
//   pm: "rizal",
//   fe1: "dody",
//   fe2: "jaja",
//   be: "kaka",
//   ux: "hendra",
//   devOps: "rere",
// };
// const { pm, ...args } = team1;
// console.log(args);

// // filtering parameter yg dikirim
// // mencari string saja, angka saja, dll apapunnya saja wkwk
// function filterBy(type, ...args) {
//   return args.filter((v) => typeof v === type);
// }
// // number dibawah masuk ke type jadi elemen selanjutnya akan dibandingkan dengan sisanya
// console.log(filterBy("boolean", 1, 2, "rizal", false, 10, true, "dody"));
// -----------------------------------------------------------------------------
//
// 12. Asynchronous programming
// -teknik teknik asynchronous = callback, promise, ajax, async & await
// -javascript = single thread menunggu proses sebelum proses sebelumnya dijalankan (singkatnya seperti lag)
// -cara atasinya ada Asynchronous (  setTimeout(()=> {},5000); )
// kenapa dipelajari?
// - supaya kita bisa bikin sebuah web yg nyaman digunakan user
// kesimpulan:
// - single vs multi tread = lingkungan eksekusi 'task'
// - blocking vs non-blocking = teknik 'ngoding' (Input/Output related)
// - synchronous vs Asynchronous = teknik 'ngoding' (HTTP request related)
// - concurrent vs parallel = linkungan kesekusi 'task'
