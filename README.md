# UTS_Rizkyllah_Citra-Digital_pert5

 Tujuan Program

Program ini digunakan untuk mendeteksi tepi (edge) pada sebuah gambar dengan metode Sobel menggunakan library OpenCV dan NumPy.
Tepi adalah daerah pada gambar di mana terjadi perubahan intensitas piksel yang signifikan, misalnya batas antara objek dan latar belakang.

 Penjelasan Baris demi Baris
---
'''Import Library
import cv2
import numpy as np'''


cv2 → modul dari OpenCV, digunakan untuk membaca, memproses, dan menampilkan gambar.

numpy (np) → digunakan untuk perhitungan numerik seperti operasi matriks, normalisasi, dan manipulasi data citra.

🔹 Langkah 1: Membaca Gambar
gambar = cv2.imread('gambar_input.jpg', cv2.IMREAD_GRAYSCALE)
if gambar is None:
    print("Gambar tidak ditemukan! Pastikan file 'gambar_input.jpg' ada di folder yang sama.")
    exit()


cv2.imread() membaca gambar dari file.

cv2.IMREAD_GRAYSCALE → langsung mengubah gambar menjadi grayscale (abu-abu) agar mudah diproses, karena deteksi tepi hanya membutuhkan 1 kanal intensitas (bukan RGB).

if gambar is None: → memastikan file gambar ditemukan. Kalau tidak, program berhenti dengan pesan error.

🔹 Langkah 2: Menghaluskan Gambar (Noise Reduction)
blur = cv2.GaussianBlur(gambar, (3, 3), 0)


Gaussian Blur digunakan untuk mengurangi noise (bintik) pada gambar.

(3,3) → ukuran kernel (area filter), semakin besar nilainya, semakin halus gambarnya.

0 → nilai sigma (standar deviasi), menentukan seberapa kuat efek blur diterapkan.

 Tujuan: agar deteksi tepi tidak salah karena gangguan noise kecil.

🔹 Langkah 3: Hitung Gradien Arah X dan Y
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)


Operator Sobel adalah filter konvolusi yang mencari perubahan intensitas piksel.

cv2.CV_64F → tipe data float 64-bit agar nilai negatif tidak hilang.

(1, 0) berarti menghitung gradien arah X (horizontal).

(0, 1) berarti menghitung gradien arah Y (vertikal).

ksize=3 → ukuran kernel 3×3 yang umum digunakan.

Hasil dari sobel_x dan sobel_y adalah peta perubahan intensitas di tiap arah.

🔹 Langkah 4: Gabungkan Gradien (Magnitudo)
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)


Fungsi ini menghitung magnitudo gradien gabungan dari arah X dan Y.

Rumus matematisnya:

𝐺
=
(
𝐺
𝑥
2
+
𝐺
𝑦
2
)
G=
(G
x
2
	​

+G
y
2
	​

)
	​


di mana Gx = gradien horizontal dan Gy = gradien vertikal.

🔹 Normalisasi Hasil ke Skala 0–255
sobel_magnitude = np.uint8(255 * sobel_magnitude / np.max(sobel_magnitude))


Nilai gradien bisa sangat besar, jadi perlu dinormalisasi agar bisa ditampilkan sebagai gambar dengan intensitas 0–255 (standar citra 8-bit).

np.max(sobel_magnitude) mencari nilai maksimum lalu semua nilai dibagi dan dikalikan 255 untuk menyesuaikan skala.

np.uint8() mengubah tipe data menjadi 8-bit integer.

🔹 Langkah 5: Menampilkan Hasil
cv2.imshow('Gambar Asli', gambar)
cv2.imshow('Sobel X (Horizontal)', cv2.convertScaleAbs(sobel_x))
cv2.imshow('Sobel Y (Vertikal)', cv2.convertScaleAbs(sobel_y))
cv2.imshow('Hasil Deteksi Tepi (Sobel)', sobel_magnitude)


cv2.imshow() → Menampilkan jendela gambar.

cv2.convertScaleAbs() → Mengubah data float (bisa negatif) menjadi 8-bit positif agar bisa ditampilkan.

Menampilkan:

Gambar asli

Hasil deteksi tepi arah X

Hasil deteksi tepi arah Y

Gabungan hasil tepi (magnitudo total)

🔹 Akhiri Program
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.waitKey(0) → Menunggu sampai ada tombol ditekan.

cv2.destroyAllWindows() → Menutup semua jendela gambar yang terbuka.

 Hasil Akhir

Setelah dijalankan, kamu akan melihat 4 jendela:

Gambar Asli (grayscale)

Sobel X – garis vertikal terlihat jelas

Sobel Y – garis horizontal terlihat jelas

Gabungan Sobel (Magnitude) – semua tepi objek terlihat jelas

 Kesimpulan

Kode ini:

Melakukan deteksi tepi dengan operator Sobel.

Menghasilkan peta tepi dengan memanfaatkan gradien intensitas arah X dan Y.

Dapat digunakan untuk tahap awal segmentasi objek, deteksi bentuk, atau analisis struktur gambar.
