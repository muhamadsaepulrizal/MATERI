// pakai dom $$

// algoritma:
// 1. ambil semua elemen vidio
const videos = Array.from(document.querySelectorAll("[data-duration]")); //document.querySelectorAll = ambil semua elemen dengan data-duration

// 2. pilih hanya yg javascript lanjutan
let jsLanjut = videos
  .filter((video) => video.textContent.includes("JAVASCRIPT LANJUTAN")) // textContent.includes('yg diambil adalah tulisan content di tag html)
  // 3. ambil durasi masing masing video ()
  .map((item) => item.dataset.duration)
  // 4. ubah durasi jadi float, ubah menit jadi detik, split juga waktu 10:30 jadi array [10.30]
  .map((waktu) => {
    // 10:30 -> [10.30] = split
    // setelah itu ubah string [10.30] jadi float(angka)
    const parts = waktu.split(":").map((part) => parseFloat(part));
    return parts[0] * 60 + parts[1];
  })
  // 5. jumlahkan semua detiknya
  .reduce((total, detik) => total + detik);
// 6. ubah lagi formatnya ke jam, menit, detik
const jam = Math.floor(jsLanjut / 3600); //ambil pembulatan kebawah pakai floor
jsLanjut = jsLanjut - jam * 3600; // timpa jsLanjut untuk menemukan sisa dari jam diatas dalam bentuk detik
const menit = Math.floor(jsLanjut / 60); //60 disini untuk menit
const detik = jsLanjut - menit * 60; //60 disini untuk detik

// 7. simpan di dom
const pDurasi = document.querySelector(".total-durasi"); //mencari elemen dengan di selector dengan class .total-durasi
pDurasi.textContent = `${jam} jam, ${menit} menit, ${detik} detik`; //masukkan ke content di htmlnya

//ambil elemen yg sudah di filter (videos) lalu kita length
const jmlVideo = videos.filter((video) =>
  video.textContent.includes("JAVASCRIPT LANJUTAN")
).length;

const pJmlVideo = document.querySelector(".jumlah-video");
pJmlVideo.textContent = `${jmlVideo} Video`;

console.log(jmlVideo);
