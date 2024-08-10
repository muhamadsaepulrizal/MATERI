// console.log("hallo \nkaka");
// jadi seperti ini:
// console.log(`hallo
// kaka`);

// multi line string (HTML fragments)
// const mhs = {
//   nama: "rizal",
//   umur: 20,
//   nim: "2306142",
// };
// seperti ini
// let el = ``;
// el += `<div class="mhs"`;
// el += `<h2>` + mhs.nama + `<h2>`;
// el += `<span clss="nim">` + mhs.nim + `<span>`;
// el += `</div>`;
// atau seperti ini lebih ringkas
// let el = `<div class="mhs">
// <h2>${mhs.nama}</h2>
// <span class="nim>${mhs.nim}</span>
// </div>`;
// console.log(el);
//
// const x = 11;
// console.log(`${x % 2 == 0 ? "genap" : "ganjil"}`);

// contoh lebih nyata HTML fragments yg nantinya disimpan di DOM
// const mhs = {
//   nama: "rizal",
//   umur: 20,
//   nim: "2306142",
//   email: "2306142@itg.ac.id",
// };
// const el = `<div class="mhs">
//  <h2>${mhs.nama}</h2>
//  <span class="nim">${mhs.nim}</span>
// </div>`;

// 2. looping
// const mhs = [
//   {
//     nama: "rizal",
//     email: "2306142@utg.ac.id",
//   },
//   {
//     nama: "kaka",
//     email: "2306143@utg.ac.id",
//   },
//   {
//     nama: "erik",
//     email: "2306144@utg.ac.id",
//   },
// ];
// const el = `<div class="mhs">
//     ${mhs
//       .map(
//         (m) => `<ul>
//             <li>${m.nama}</li>
//             <li>${m.email}</li>
//         </ul>`
//       )
//       .join("")}
// </div>`;

// 3. pengkondisian
// ternary
// const lagu = {
//   judul: "konservatif",
//   penyanyi: "the adams",
//    //feat: "koko",
// };
// const el = `<div class="lagu">
// <ul>
// <li>${lagu.penyanyi}</li>
// <li>${lagu.judul} ${lagu.feat ? `(feat. ${lagu.feat})` : ""}</li>
// </ul>
// </div>`;

// 4. HTML fragments bersarang atau nested
const mhs = {
  nama: "koko",
  sms: 5,
  matkul: ["rpl", "ai", "multimadia", "b.Indo"],
};
function cetakMatkul(matkul) {
  return `
    <ol>
        ${matkul.map((mk) => `<li>${mk}</li>`).join("")}
    </ol>`;
}
const el = `<div class="mhs">
    <h2>Nama: ${mhs.nama}</h2>
    <span class="sms">Semester ${mhs.sms}</span>
    <h4>Mata Kuliah</h4>${cetakMatkul(mhs.matkul)}
  </div>`;
document.body.innerHTML = el;
