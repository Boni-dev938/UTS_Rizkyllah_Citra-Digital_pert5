import cv2
import numpy as np

# === Langkah 1: Baca gambar grayscale ===
gambar = cv2.imread('images.jpg', cv2.IMREAD_GRAYSCALE)
if gambar is None:
    print("Gambar tidak ditemukan! Pastikan file 'gambar_input.jpg' ada di folder yang sama.")
    exit()

# === Langkah 2: Terapkan Gaussian Blur untuk mengurangi noise ===
blur = cv2.GaussianBlur(gambar, (3, 3), 0)

# === Langkah 3: Hitung gradien arah X dan Y menggunakan Sobel ===
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)  # Deteksi tepi horizontal
sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)  # Deteksi tepi vertikal

# === Langkah 4: Hitung magnitudo gabungan (hasil akhir tepi) ===
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)

# Normalisasi hasil agar bisa ditampilkan dengan skala 0–255
sobel_magnitude = np.uint8(255 * sobel_magnitude / np.max(sobel_magnitude))

# === Langkah 5: Tampilkan hasil ===
cv2.imshow('Gambar Asli', gambar)
cv2.imshow('Sobel X (Horizontal)', cv2.convertScaleAbs(sobel_x))
cv2.imshow('Sobel Y (Vertikal)', cv2.convertScaleAbs(sobel_y))
cv2.imshow('Hasil Deteksi Tepi (Sobel)', sobel_magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()
