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

// filtering parameter yg dikirim
// mencari string saja, angka saja, dll apapunnya saja wkwk
// function filterBy(type, ...args) {
//   return args.filter((v) => typeof v === type);
// }
// // number dibawah masuk ke type jadi elemen selanjutnya akan dibandingkan dengan sisanya
// console.log(filterBy("boolean", 1, 2, "rizal", false, 10, true, "dody"));
