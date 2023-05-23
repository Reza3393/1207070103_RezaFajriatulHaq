import cv2  # Mengimpor modul cv2 untuk pengolahan citra menggunakan OpenCV.
import numpy as np  # Mengimpor modul numpy untuk operasi array dan manipulasi data numerik.
from skimage import data  # Mengimpor modul data dari skimage untuk mendapatkan contoh citra.
import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari matplotlib untuk visualisasi gambar.

img = cv2.imread("Image/ronaldo.jpeg")  # Mendapatkan contoh citra 'camera' dari modul data di skimage dan menyimpannya dalam variabel img.
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #untuk mengubah citra img dari format BGR menjadi grayscale. Hasil konversi disimpan kembali ke variabel img

row, column = img.shape  # Mendapatkan dimensi baris dan kolom citra menggunakan atribut shape dan menyimpannya dalam variabel row dan column.

img1 = np.zeros((row,column),dtype = 'uint8')  # Membuat array kosong dengan ukuran yang sama dengan citra (row x column) dan tipe data uint8, kemudian menyimpannya dalam variabel img1.

min_range = 10  # Mengatur nilai batas bawah (minimum) untuk rentang intensitas piksel.
max_range = 60  # Mengatur nilai batas atas (maksimum) untuk rentang intensitas piksel.

for i in range(row):  # Melakukan iterasi untuk setiap baris dalam citra.
    for j in range(column):  # Melakukan iterasi untuk setiap kolom dalam citra.
        if img[i,j]>min_range and img[i,j]<max_range:  # Memeriksa apakah intensitas piksel pada posisi (i, j) berada dalam rentang yang ditentukan.
            img1[i,j] = 255  # Jika iya, mengatur intensitas piksel pada posisi (i, j) dalam img1 menjadi 255 (putih).
        else:
            img1[i,j] = 0  # Jika tidak, mengatur intensitas piksel pada posisi (i, j) dalam img1 menjadi 0 (hitam).

fig, axes = plt.subplots(2, 2, figsize=(12, 12))  # Membuat subplot dengan 2 baris dan 2 kolom, dengan ukuran total 12x12 inch, dan menyimpannya dalam variabel fig dan axes.

ax = axes.ravel()  # Mengubah array 2D axes menjadi array 1D menggunakan ravel(), dan menyimpannya dalam variabel ax.

ax[0].imshow(img, cmap=plt.cm.gray)  # Menampilkan citra input dalam axes pertama (indeks 0) menggunakan imshow() dengan peta warna gray.
ax[0].set_title("Citra Input")  # Mengatur judul untuk axes pertama.

ax[1].hist(img.ravel(), bins=256)  # Menampilkan histogram citra input dalam axes kedua (indeks 1) menggunakan fungsi hist() dengan jumlah bin sebesar 256.
ax[1].set_title('Histogram Input')  # Mengatur judul untuk axes kedua.

ax[2].imshow(img1, cmap=plt.cm.gray)  # Menampilkan citra output dalam axes ketiga (indeks 2) menggunakan imshow() dengan peta warna gray.
ax[2].set_title("Citra Output")  # Mengatur judul untuk axes ketiga.

ax[3].hist(img1.ravel(), bins=256)  # Menampilkan histogram citra output dalam axes keempat (indeks 3) menggunakan fungsi hist() dengan jumlah bin sebesar 256.
ax[3].set_title('Histogram Output')  # Mengatur judul untuk axes keempat.

plt.show()



