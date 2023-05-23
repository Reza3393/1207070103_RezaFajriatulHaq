import matplotlib.pyplot as plt  # Mengimpor modul matplotlib untuk visualisasi data.
from skimage import data  # Mengimpor fungsi data dari modul skimage untuk mengambil citra bawaan.
from skimage.io import imread  # Mengimpor fungsi imread dari modul skimage.io untuk membaca citra dari file.
from skimage.color import rgb2gray  # Mengimpor fungsi rgb2gray dari modul skimage.color untuk mengubah citra menjadi grayscale.
import numpy as np  # Mengimpor modul numpy untuk operasi array.
import cv2  # Mengimpor modul cv2 dari OpenCV untuk pengolahan citra.

citra1 = imread(fname="Image/gedung.tif")  # Membaca citra dengan nama file "gedung.tif" menggunakan fungsi imread.
print(citra1.shape)  # Menampilkan dimensi citra menggunakan atribut shape.

plt.imshow(citra1, cmap='gray')  # Menampilkan citra menggunakan imshow dengan cmap 'gray'.

kernel = np.array([[-1, 0, -1], 
                   [0, 4, 0], 
                   [-1, 0, -1]])  # Membuat kernel sebagai array 3x3 dengan nilai tertentu.

citraOutput = cv2.filter2D(citra1, -1, kernel)  # Melakukan filtering citra menggunakan kernel dengan filter2D.

fig, axes = plt.subplots(1, 2, figsize=(12, 12))  # Membuat objek subplot dengan ukuran 1x2 dan ukuran gambar 12x12.
ax = axes.ravel()  # Melakukan ravel pada objek axes untuk mendapatkan array dari semua sumbu subplot.

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra input pada sumbu indeks 0.
ax[0].set_title("Citra Input")  # Menetapkan judul untuk sumbu indeks 0.
ax[1].imshow(citraOutput, cmap='gray')  # Menampilkan citra output pada sumbu indeks 1.
ax[1].set_title("Citra Output")  # Menetapkan judul untuk sumbu indeks 1.

plt.show()


