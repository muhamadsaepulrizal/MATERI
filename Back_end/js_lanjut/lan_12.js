// spread operator
// memecah iterables jadi single elements

// // case 1 pada gabungkan array
// // buat array mhs
// const mhs = ["kaka", "ucup", "baba"];
// console.log(...mhs[0]); //maka akan memecah kaka = k a k a
// // buat satu lagi array dosen
// const dosen = ["jaja", "ajum", "agus"];
// // lalu gabungkan aray mhs & dosen ditampung ke array lagi u menampung hasilnya
// // lalu saktinya pakai spread operator ditengah2 kita bisa menambahkan elemen array baru
// const mhsDosen = [...mhs, "nana", ...dosen];
// console.table(mhsDosen);

// // bisa juga pakai cara lain prototype array yaitu concat u menggabungkan 2 array
// const orang = mhs.concat(dosen);
// console.log(orang);

// // case 2 meng copy array
// const mhs = ["kaka", "ucup", "baba"];
// // // dengan cara ini array asal juga berubah jadi bukan men copy, lalu hasil copy bisa dirubah
// // // karena kita ingin merubah-rubah array copyan-nya
// // const mhs1 = mhs;
// // mhs1[0] = "akak";
// // console.log(mhs1);
// // console.log(mhs); //ikut berubah

// // caranya seperti ini yg benar
// // maka mhs1 benar2 copyan dan bisa di edit tanpa ganggu array asalnya
// const mhs1 = [...mhs];
// mhs1[0] = "akak";
// console.log(mhs1);
// console.log(mhs); //tak ikut berubah

// mengambil elemen html jadi array
// const liMhs = document.querySelectorAll("li");
// //pakai loop for
// const mhs = [];
// for (var i = 0; i < liMhs.length; i++) {
//   mhs.push(liMhs[i].textContent);
// }
// console.log(mhs);
// //pakai map lebih simple
// //map hanya untuk array u ubah ke array pakai spread (...)
// const mhs = [...liMhs].map((m) => m.textContent);
// console.log(mhs);

// // mengubah perilaku elemen html
// // melakukan animasi gerak setiap huruf pada nama
// const nama = document.querySelector(".nama");
// const hurufNama = [...nama.textContent]
//   //membungkus huruf dengan span
//   .map((hN) => `<span>${hN}</span>`)
//   //marubah array jadi string biasa
//   .join("");
// //timpa hurufNama ke nama sehinggah h1 tiap huruf dibungkus span
// nama.innerHTML = hurufNama;
