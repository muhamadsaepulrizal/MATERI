// Pembahasan DOM (Document Object Model)
// DOM adl antarmuka pemograman u HTMl yg merepresentasikan halaman web,
// sehingga Dapat mengubah dan memanipulasi strukturnya.

//Antarmuka pemograman berbasis obejek yg merepresentasikan dokumen web
//Dom membuat seluruh komponen dari halaman web dapat diakses & dimanipulasi
//Kompenen nya apa saja?
// - elemen HTML, atribut, text, dll.
//Dom dpt dimanipulasi (dibuat, diubah, dihapus) menggunakan javascript.

// Materi DOM:
// 1. Dom selection
// 2. Dom manipulation
// 3. Dom traversal
// 4. Event handling
// 5. studi kasus

// DOM Tree
// -node pada Dome Tree memiliki banyak tipe:
//  Tipe element: <body>, <p> <h1>, dll
//  Tipe text: "paragraph 1" = yg ada didalam element.
//  Tipe attribute: href, dll
//  dan masih banyak lagi untuk type node-nya...

// istilah istilah: yg cara mengelolanya akan berbeda
// NodeList: kumpulan node dengan tipe yg berbeda bisa element, bisa text, bisa attribute. bersifat tidak live
// HTMLCollection: kumpulan node dengan tipe (element) saja. bersifat live
// 1. keduanya merupakan kumpulan node
// 2. struktur data-nya mirip array

// Struktur Hierarki Dom tree:
// 1. Root Node :
//  node yg menjadi sumbr dari semua node lain di dalam DOM
//  document
// 2. Parent Node:
//  node yg berada satu tingkat diatas node yg lain
// 3. Child Node:
//  node yg berada satu tingkat dibaah node yg lain

// 1. Dom selection method
// - document.getElementById() , hasil = element. menyeleksi lewat id, hanya 1

// - document.getElementsByTagName(), hasil = HTMLCollection. menyeleksi lewat nama tag-nya di console bentuknya array
// - document.getElementsByClasName(), hasil = HTMLCollection. menyeleksi lewat class kenapa, class bisa lebih dari 1 beda dng id
// untuk yg menghasilkan HTMLCollection hasilnya berupa array maka jika ingin manipulasi pakai index-nya.

// - querySelector(), hasil = element. hanya 1
// - querySelectorAll(), hasil = nodeList
// selector diatas adalah selector css yg dipakai untuk styling
// u yg All bentuk hasilnya berupa nodeList jadi u manipulasi jangan lupa tulis index-nya.
// querySelector digunakan jika tak ingin merubah atau menyentuh HTML-nya seperti menambah id & class
//
// ------------------------------------------------------------------
// Manipulation DOM
// 1. Manipulasi element
// method yg sering dipakai u manipulasi element:
// - element.innerHTML = u mengubah isi sebuah tag html, selain ubah isi juga bisa ditambah tag HTMl lagi
//    jadi intinya bisa menulis ulang tag html dengan isinya di js, tanpa sentuh HTML

// - element.style.<property css> = u ubah style nya seperti css, tapi di js

// untuk mengelola attribute, sesuatu yg menempel pada element pada HTML
// attribute seperti: class, id, href, dll
// -  element.getAttribute('attribute-nya') = mengetahui isi attribute, contoh attribute href bisa diliat isinya ke link mana
//    element.setAttribute('attribute','isi attribute') = menambah attribute baru, dan menimpa isi attribute jika sudah ada
//    element.removeAttribute('attribute-nya') = menghapus attribute

// - element.classList = untuk mengelola class
// element.classList.add()menambah / .remove()menghilangkan
// .toggle()menambah jika takAda, menghapus jika ada / .item(index dari 0)mengetahui class tertentu dlm element
// .contains()cek suatu class tertentu / .replace('awal','pengganti')mengganti class yg ada dengan yg baru

// 2. Manipulasi node
// method yg sering dipakai u manipulasi node
// - document.createElement()
// - document.createTextNode()
// - node.appendChild() = menyimpan diakhir
// - node.insertBefore(elBaru,elSetelahnya) = tangkap element parent, dan element setelahnya
// - parentNode.removeChild() = tangkap element parent & element yg ingin dihapus
// - parentNode.replaceChild(nodeBaru,nodeYgDiganti) = tangkap element parent & element yg ingin diganti,
//      lalu buat element baru dengan createElement() dan createTextNode() dan node.appendChild() lalu tinggal replace
//
// --------------------------------------------------------------------
// Materi DOM Events (kejadian yg terjadi dalam dom)
// -kejadian tersebut dilakukan oleh user (mouse event, keyboard event, dll)
// -ataupun dilakukan secara otomatis oleh API (animsi selesai dijalankan, halaman selesai di load, dll)
// cara 'mendengarkan'/menajalankan event:
// 1. Event Handler. cara lama
// - inline HTML attribute = didalam tag html, tidak disarankan karena menyentuh HTML
// - Element method contoh p2.onclick = ubahWarna;
//  on<event> contoh onclick
// 2. addEventListener(). cara baru bedanya ketika ada perubahan lebih dari 1 tidak saling menimpa perubahan sebelumnya
// contoh sederhana:
//  const p4 = document.querySelector('section#b p');
//  p4.addEventListener('click', function () {
//    alert('ok');
//  });
// ----------------------------------------------------------------------
//
// Materi Dom Traversal (penelusuran)
// kenapa diperlukan?
// -
// Method traversal
// -parentNode =, mengembalikan node
// -parentElement =, mengembalikan element
//  u parentElement jika ingin ambil kakek, maka gunakan 2 atau lebih seperti = e.target.parentElement.parentElement
// -nextSibling = saudara kandung dari sebuah element,enter html dihitung. mengembalikan node
// -nextElementSibling =, mengembalikan element, enter html tak dihitung
// -previousSibling =, mengembalikan node
// -previousElementSibling =, mengembalikan element
// ----------------------------------------------------------------------------
//
// prevent Default (menghilangkan kasi default dari suatu element)
// seperti element a yg punya default merepres
// caranya tingal tambah diakhir aksi event :
//      const close = document.querySelectorAll('.close');
//      close.forEach(function (el) {
//        el.addEventListener('click', function (e) {
//          e.target.parentElement.style.display = 'none';
//          e.preventDefault();
//        });
//      });
// --------------------------------------------------------------------------
//
// event bubbling
// sederhanya ketika child punya event, lalu parent punya event, saat kita click event pada child
// maka event di parent-nya juga akan kepanggil
// nah supaya event pada child saat dipanggil namun event parent-nya tidak ikut maka stop bubblingnya dengan:
// method = e.stopPropagation();, maka event pada setiap parent-nya tak akan jalan
