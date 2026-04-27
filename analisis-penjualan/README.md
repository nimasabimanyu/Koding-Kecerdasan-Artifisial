# Analisis Performa Penjualan E-Commerce

## Kelompok

1. Nimas
2. Bening

---

## Business Question

* Siapa pelanggan terbaik berdasarkan data transaksi?
* Apakah anggaran iklan (Ad_Budget) berpengaruh terhadap total penjualan (Total_Sales)?
* Kategori produk mana yang paling efektif dalam menghasilkan penjualan?
* Apakah terdapat produk dengan harga tinggi tetapi memiliki jumlah penjualan yang rendah?

---

## Data Wrangling

* Menghapus data dengan nilai *Price_Per_Unit* yang tidak valid (≤ 0)
* Mengubah kolom *Order_Date* menjadi format datetime
* Menghapus data yang memiliki nilai kosong (missing values) pada kolom penting seperti *Ad_Budget* dan *Total_Sales*

---

## Insights

* Terdapat produk dengan harga tinggi namun jumlah penjualan rendah, sehingga termasuk kategori *underperformer*.
* Hubungan antara anggaran iklan (*Ad_Budget*) dan total penjualan (*Total_Sales*) tidak terlalu kuat.
* Tidak semua kategori produk dengan anggaran iklan besar menghasilkan penjualan yang tinggi.
* Peningkatan anggaran iklan tidak selalu diikuti dengan peningkatan penjualan yang signifikan.
* Hasil regresi menunjukkan bahwa pengaruh iklan terhadap penjualan bersifat positif tetapi sangat kecil.

---

## Recommendation

* Perusahaan perlu mengevaluasi produk dengan harga tinggi namun kurang diminati.
* Penggunaan anggaran iklan perlu dioptimalkan agar lebih efektif.
* Fokus pada pelanggan loyal berdasarkan hasil RFM Analysis untuk meningkatkan penjualan.
* Perlu mempertimbangkan faktor lain seperti harga, kualitas produk, dan strategi promosi selain iklan.

---

## 1. Identifikasi Produk Underperformer

**Analisis:**
Berdasarkan scatter plot antara *Price_Per_Unit* dan *Quantity*, terdapat produk dengan harga tinggi tetapi jumlah penjualannya rendah.

**Insight:**
Harga yang terlalu mahal dapat menjadi salah satu penyebab rendahnya minat pembelian.

**Kesimpulan:**
Produk tersebut termasuk *underperformer* dan perlu dievaluasi dari segi harga atau strategi pemasaran.

---

## 2. Segmentasi Pelanggan (RFM Analysis)

**Analisis:**
Pelanggan dikelompokkan berdasarkan Recency, Frequency, dan Monetary.

**Insight:**
Terdapat pelanggan yang aktif (sering dan baru bertransaksi) serta pelanggan yang sudah lama tidak melakukan pembelian.

**Kesimpulan:**
Segmentasi ini dapat digunakan untuk menentukan strategi promosi seperti pemberian voucher kepada pelanggan loyal.

---

## 3. Analisis Kontribusi Kategori

**Analisis:**
Dilakukan perbandingan antara total penjualan dan anggaran iklan pada setiap kategori produk.

**Insight:**
Beberapa kategori memiliki anggaran iklan besar tetapi tidak menghasilkan penjualan yang sebanding.

**Kesimpulan:**
Kategori yang kurang efisien perlu dievaluasi agar penggunaan anggaran lebih optimal.

---

## 4. Uji Hipotesis Sederhana

**Analisis:**
Data dibagi menjadi dua kelompok berdasarkan median *Ad_Budget*, yaitu iklan tinggi dan iklan rendah.

**Insight:**
Hasil menunjukkan bahwa peningkatan anggaran iklan tidak selalu meningkatkan penjualan secara signifikan.

**Kesimpulan:**
Iklan bukan satu-satunya faktor yang mempengaruhi penjualan.

---

## 5. Pendalaman Teknik: RFM Analysis

**Analisis:**
Dilakukan pemberian skor RFM untuk setiap pelanggan berdasarkan Recency, Frequency, dan Monetary.

**Insight:**
Pelanggan dengan skor tinggi merupakan pelanggan terbaik karena aktif dan memiliki kontribusi besar terhadap penjualan.

**Kesimpulan:**
RFM Analysis efektif untuk menentukan strategi loyalitas pelanggan.

---

## 6. Pendalaman Teknik: Regresi Linear

**Hasil:**

* Koefisien Iklan: 0.184
* R2 Score: -0.19

**Insight:**
Anggaran iklan memiliki pengaruh positif terhadap penjualan, namun pengaruhnya sangat kecil dan hubungan keduanya tidak kuat.

**Kesimpulan:**
Penjualan dipengaruhi oleh banyak faktor, tidak hanya anggaran iklan.
