Tugas Analisis 1
Jika nilai hero1.hp diubah menjadi 500 setelah objek dibuat, lalu dilakukan print(hero1.hp), maka nilai yang ditampilkan adalah 500.
Hal ini terjadi karena atribut hp bersifat public, sehingga dapat diakses dan diubah langsung dari luar class. Python tidak membatasi perubahan atribut public, sehingga nilai HP hero dapat dimodifikasi secara bebas setelah proses instansiasi.

Tugas Analisis 2
Parameter lawan pada method serang menerima sebuah objek, bukan hanya data berupa string nama.
Hal ini penting karena dengan menerima objek secara utuh, program dapat:
> Mengakses atribut milik lawan seperti HP
> Memanggil method lain milik lawan seperti diserang()
> Mengubah kondisi objek lawan secara langsung
Dengan demikian, interaksi antar hero dalam game benar-benar terjadi secara nyata di dalam program, bukan hanya berupa tampilan teks.

Tugas Analisis 3
a. Error yang Muncul
Jika baris super().__init__(name, hp, attack_power) dihapus, maka akan muncul error:
AttributeError: 'Mage' object has no attribute 'name'
b. Penyebab Error
Error tersebut muncul karena constructor milik class induk (Hero) tidak dijalankan. Akibatnya, atribut dasar seperti name, hp, dan attack_power tidak pernah dibuat pada objek Mage, meskipun nilai tersebut sudah dikirim saat pembuatan objek.
c. Peran Fungsi 
super()
Fungsi super() berfungsi untuk memanggil constructor milik class induk agar seluruh atribut dasar tetap terbentuk. Dengan adanya super(), class anak dapat mewarisi dan menggunakan data dari class induk dengan benar.

Tugas Analisis 4
1. Percobaan Akses Paksa Data
saat baris kode :
print(hero1._Hero__hp)
dijalankan, nilai HP tetap dapat ditampilkan.
Hal ini disebabkan oleh mekanisme Name Mangling pada Python, di mana atribut private diubah secara internal agar tetap bisa dibedakan antar class. Meskipun memungkinkan, akses ini tidak disarankan karena melanggar prinsip enkapsulasi dan praktik pemrograman yang baik.
2. Uji Validasi Setter
Jika logika validasi pada method set_hp() dihapus dan hanya menyisakan:
self.__hp = nilai_baru
kemudian dilakukan hero1.set_hp(-100), maka nilai HP hero menjadi -100.
Kondisi ini menunjukkan bahwa tanpa validasi, data menjadi tidak terkontrol. Oleh karena itu, method setter sangat penting untuk menjaga integritas data dan mencegah nilai yang tidak logis dalam sistem game.

Tugas Analisis 5
1. Pelanggaran Kontrak Interface
Jika method serang() pada class Hero dihapus, program akan menampilkan error:
Can't instantiate abstract class Hero with abstract method serang
Error ini berarti class Hero tidak memenuhi kontrak yang telah ditetapkan oleh interface. Konsekuensinya, objek dari class tersebut tidak dapat dibuat sebelum seluruh method abstrak diimplementasikan.
2. Alasan Abstract Class Tidak Bisa Diinstansiasi
Class GameUnit tidak dapat dibuat menjadi objek karena berfungsi sebagai kerangka dasar. Class ini digunakan untuk menetapkan standar method bagi class turunannya, bukan sebagai objek yang digunakan langsung dalam program.

Tugas Analisis 6
1. Penambahan Class Baru
Setelah menambahkan class Healer(Hero) dan memasukkannya ke dalam list pasukan, program tetap berjalan tanpa mengubah kode looping.
Hal ini menunjukkan bahwa konsep polymorphism memudahkan penambahan fitur baru tanpa harus mengubah struktur program yang sudah ada.

2. Konsistensi Penamaan Method
Jika nama method serang pada class Archer diubah menjadi tembak_panah, maka program akan mengalami error saat looping dijalankan.
Hal ini terjadi karena pada konsep polymorphism, semua class turunan harus memiliki nama method yang sama agar dapat dipanggil secara seragam oleh program.

Kesimpulan
Penerapan konsep Object-Oriented Programming (OOP) membuat program lebih terstruktur, aman, dan mudah dikembangkan. Setiap pilar OOP memiliki peran penting dalam menjaga kualitas dan kestabilan program, terutama dalam pengembangan aplikasi dan game berskala besar.
