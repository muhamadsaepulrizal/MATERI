const container = document.querySelector('.container');
const jumbo = document.querySelector('.jumbo');
const thumbs = document.querySelectorAll('.thumb');

container.addEventListener('click', function (e) {
  // cek apakah yg diclik adl thumb, jika ya ganti src jumbo dengan src yg diclick
  if (e.target.className == 'thumb') {
    jumbo.src = e.target.src;
    jumbo.classList.add('fade');
    //setTimeout supaya animasi fade hanya bertahan 0.5 detik, lalu hilangkan
    //saat di click lagi bakal muncul fade-nya, lalu hilang lagi setelah 0.5 s
    setTimeout(function () {
      jumbo.classList.remove('fade');
    }, 500);

    thumbs.forEach(function (thumb) {
      //   if (thumb.classList.contains('active')) {
      //     thumb.classList.remove('active');
      //   }
      thumb.className = 'thumb';
    });
    e.target.classList.add('active');
  }
});
