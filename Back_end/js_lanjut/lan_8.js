// tagged tampalte
// const nama = "rizal";
// const umur = 20;

// // (...args) adalah sebuah parameter dimana akan menampung semua argument
// // tanpa kita tahu ada berapa jumlah argument nya / otomatis
// // jadi string buat ambil strings biasa, ...args buat ambil semua expressionnya
// function coba(strings, ...args) {
//   //   let result_str = "";
//   ////kenapa pakai forEach karena jika pakai map akan terbentuk array baru
//   //   strings.forEach((str, i) => {
//   ////||(or) string kosong("") karena jml string dan expressionnya kurang 1 setelah tahun
//   ////jadi dikasih or, supaya jika expression gak ada diberi string kosong tidak undifined
//   // result_str += `${str}${args[i] || ""}`;
//   //   });
//   //   return result_str;

//   //cara diatas bisa diringkas pakai reduce
//   //string kosong diakhir sebagai nilai awal karena ini string jadi diberi("") kalo angka(0)
//   //parameter ada 3= result_str(yg menggabungkan hasil), str(el yg akan digabungkan), i(u loop expressionya)
//   //lebih ringkas boss
//   return strings.reduce(
//     (result_str, str, i) => `${result_str}${str}${args[i] || ""}`,
//     ""
//   );
// }

// const str = coba`hallo saya ${nama}, umur saya ${umur} tahun`;
// console.log(str);

// kenapa diatas diperlukan?

// contoh Highlights
const nama = "rizal";
const umur = 20;
const email = "2306142@itg.ac.id";

// (...args) adalah sebuah parameter dimana akan menampung semua argument
// tanpa kita tahu ada berapa jumlah argument nya / otomatis
// jadi string buat ambil strings biasa, ...args buat ambil semua expressionnya
function highligh(strings, ...args) {
  //cara diatas bisa diringkas pakai reduce
  //string kosong diakhir sebagai nilai awal karena ini string jadi diberi("") kalo angka(0)
  //parameter ada 3= result_str(yg menggabungkan hasil), str(el yg akan digabungkan), i(u loop expressionya)
  //lebih ringkas boss
  return strings.reduce(
    (result_str, str, i) =>
      `${result_str}${str}<span class="hl">${args[i] || ""}</span>`,
    ""
  );
}

const str = highligh`hallo saya ${nama}, umur saya ${umur} tahun dan email saya : ${email}`;
console.log(str);

document.body.innerHTML = str;
