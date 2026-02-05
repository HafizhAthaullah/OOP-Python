Analisis 1
Hp nya hero pertama berubah menjadi 500


Analisis 2
Karena di dalam method serang, kita tidak hanya butuh nama lawan, tapi juga perilaku dan data milik lawan.


Analisis 3
Python tidak otomatis menyimpan name, hp, dan attack_power
karena constructor (__init__) milik Hero tidak pernah dijalankan

Fungsi super() berperan sebagai jembatan penghubung antara class Anak (child) dan class Induk (parent), khususnya untuk mewarisi dan menginisialisasi data milik class Induk.


Analisis 4
Percobaan Hacking
Nilai HP muncul dan tidak terjadi error. Python menggunakan mekanisme Name Mangling. Sehingga atribut __hp di dalam class Hero sebenarnya tersimpan sebagai _Hero__hp. Hal ini membuat atribut tersebut masih bisa diakses secara paksa dari luar class jika mengetahui nama internalnya.

Uji Validasi
Nilai HP menjadi -100. Tanpa validasi pada setter, nilai HP dapat diubah menjadi nilai yang tidak logis, seperti angka negatif. Hal ini dapat merusak aturan permainan dan menyebabkan ketidaksesuaian logika dalam game.


Analisis 5
Melanggar Kontrak
Program akan menampilkan error “Can’t instantiate abstract class Hero with abstract method serang” dan objek Hero tidak dapat dibuat.

Mencetak Cetakan
Saat baris unit = GameUnit() diaktifkan, program akan menghasilkan error karena class GameUnit tidak dapat dibuat menjadi objek.
Class GameUnit tidak dapat dijadikan objek karena merupakan abstract class yang berfungsi sebagai cetakan atau kontrak. Kegunaan class ini adalah untuk menentukan aturan dan struktur method yang wajib dimiliki oleh class turunannya, sehingga program menjadi konsisten, terstruktur, dan mudah dikembangkan meskipun class tersebut tidak pernah dibuat menjadi objek nyata.


Analisis 6
Uji Skalabilitas
Program tetap berjalan dengan lancar setelah menambahkan class Healer ke dalam list pasukan, tanpa mengubah satu baris pun pada kode looping.
Hal ini menunjukkan bahwa konsep Polymorphism memungkinkan objek dengan class yang berbeda untuk diperlakukan sama selama memiliki method dengan nama yang sama, yaitu serang(). Keuntungan polymorphism bagi programmer adalah memudahkan pengembangan dan penambahan fitur di masa depan tanpa harus mengubah kode yang sudah ada, sehingga program menjadi fleksibel, efisien, dan mudah dirawat.

Konsistensi Penamaan
Saat nama method serang() pada class Archer diubah menjadi tembak_panah(), program mengalami error karena method serang() tidak ditemukan pada objek Archer. Dalam konsep polymorphism, nama method antara parent class dan child class harus persis sama agar pemanggilan method dapat dilakukan secara seragam. Jika nama method berbeda, Python tidak dapat mengenali method tersebut saat dipanggil melalui parent class, sehingga menyebabkan error dan polymorphism tidak dapat berjalan dengan baik.