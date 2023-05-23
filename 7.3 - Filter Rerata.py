import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari library matplotlib untuk membuat visualisasi plot.
from skimage import data  # Mengimpor modul data dari library skimage untuk mengakses dataset citra bawaan.
from skimage.io import imread  # Mengimpor modul imread dari library skimage.io untuk membaca citra dari file.
from skimage.color import rgb2gray  # Mengimpor modul rgb2gray dari library skimage.color untuk mengkonversi citra RGB menjadi grayscale.
import numpy as np  # Mengimpor modul numpy untuk operasi array dan manipulasi data numerik.

citra1 = imread(fname="Image/gedung.tif")  # Membaca citra dari file "mobil.tif" dan menyimpannya dalam variabel citra1.
citra2 = imread(fname="Image/goldhill.tif")  # Membaca citra dari file "boneka2.tif" dan menyimpannya dalam variabel citra2.

print('Shape citra 1 : ', citra1.shape)  # Menampilkan dimensi citra 1 dengan menggunakan atribut shape.
print('Shape citra 2 : ', citra2.shape)  # Menampilkan dimensi citra 2 dengan menggunakan atribut shape.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))  # Membuat subplot dengan 1 baris dan 2 kolom, serta mengatur ukuran figur menjadi 10x10.
ax = axes.ravel()  # Membuat array 1 dimensi dari axes.

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra 1 dalam axes pertama menggunakan cmap gray.
ax[0].set_title("Citra 1")  # Mengatur judul untuk axes pertama.
ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra 2 dalam axes kedua menggunakan cmap gray.
ax[1].set_title("Citra 2")  # Mengatur judul untuk axes kedua.

#proses filter rerata untuk citra mobil
#F2 = double(inputMobil);
#for baris=2 : tinggiA-1
#    for kolom=2 : lebarA-1
#        jum = F2(baris-1, kolom-1)+ F2(baris-1, kolom) + F2(baris-1, kolom-1) + ...
#              F2(baris, kolom-1) + F2(baris, kolom) + F2(baris, kolom+1) + ...
#              F2(baris+1, kolom-1) + F2(baris+1, kolom) + F2(baris+1, kolom+1);         
#         outputMobil(baris, kolom) = uint8(1/9 * jum);
#    end
#end

copyCitra1 = citra1.copy().astype(float)  # Membuat salinan citra1 dan mengonversinya ke tipe data float.
copyCitra2 = citra2.copy().astype(float)  # Membuat salinan citra2 dan mengonversinya ke tipe data float.

m1,n1 = copyCitra1.shape  # Mendapatkan dimensi citra1 dan menyimpannya dalam variabel m1 dan n1.
output1 = np.empty([m1, n1])  # Membuat array kosong dengan ukuran m1 x n1 untuk menyimpan output1.

m2,n2 = copyCitra2.shape  # Mendapatkan dimensi citra2 dan menyimpannya dalam variabel m2 dan n2.
output2 = np.empty([m2, n2])  # Membuat array kosong dengan ukuran m2 x n2 untuk menyimpan output2.

print('Shape copy citra 1 : ', copyCitra1.shape)  # Menampilkan dimensi copyCitra1 dengan menggunakan atribut shape.
print('Shape output citra 1 : ', output1.shape)  # Menampilkan dimensi output1 dengan menggunakan atribut shape.
print('m1 : ',m1)  # Menampilkan nilai m1.
print('n1 : ',n1)  # Menampilkan nilai n1.
print()

print('Shape copy citra 2 : ', copyCitra2.shape)  # Menampilkan dimensi copyCitra2 dengan menggunakan atribut shape.
print('Shape output citra 3 : ', output2.shape)  # Menampilkan dimensi output2 dengan menggunakan atribut shape.
print('m2 : ',m2)  # Menampilkan nilai m2.
print('n2 : ',n2)  # Menampilkan nilai n2.
print()

for baris in range(0, m1-1):  # Melakukan perulangan untuk setiap baris dari 0 hingga m1-2.
    for kolom in range(0, n1-1):  # Melakukan perulangan untuk setiap kolom dari 0 hingga n1-2.
        a1 = baris  # Menyimpan nilai baris dalam variabel a1.
        b1 = kolom  # Menyimpan nilai kolom dalam variabel b1.
        jumlah = copyCitra1[a1-1, b1-1] + copyCitra1[a1-1, b1] + copyCitra1[a1-1, b1-1] + \
                 copyCitra1[a1, b1-1] + copyCitra1[a1, b1] + copyCitra1[a1, b1+1] + \
                 copyCitra1[a1+1, b1-1] + copyCitra1[a1+1, b1] + copyCitra1[a1+1, b1+1];  # Menghitung jumlah dari 9 tetangga piksel.
        output1[a1, b1] = (1/9 * jumlah)  # Menyimpan hasil rata-rata dari tetangga piksel dalam output1[a1, b1].

for baris1 in range(0, m2-1):  # Melakukan perulangan untuk setiap baris dari 0 hingga m2-2.
    for kolom1 in range(0, n2-1):  # Melakukan perulangan untuk setiap kolom dari 0 hingga n2-2.
        a1 = baris1  # Menyimpan nilai baris dalam variabel a1.
        b1 = kolom1  # Menyimpan nilai kolom dalam variabel b1.
        jumlah = copyCitra2[a1-1, b1-1] + copyCitra2[a1-1, b1] + copyCitra2[a1-1, b1-1] + \
                 copyCitra2[a1, b1-1] + copyCitra2[a1, b1] + copyCitra2[a1, b1+1] + \
                 copyCitra2[a1+1, b1-1] + copyCitra2[a1+1, b1] + copyCitra2[a1+1, b1+1];  # Menghitung jumlah dari 9 tetangga piksel.
        output2[a1, b1] = (1/9 * jumlah)  # Menyimpan hasil rata-rata dari tetangga piksel dalam output2[a1, b1].

fig, axes = plt.subplots(2, 2, figsize=(10, 10))  # Membuat subplots dengan 2 baris dan 2 kolom, dengan ukuran gambar 10x10.
ax = axes.ravel()  # Meratakan array axes menjadi satu dimensi.

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra1 pada axis 0 dengan colormap 'gray'.
ax[0].set_title("Input Citra 1")  # Memberikan judul "Input Citra 1" pada axis 0.

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra2 pada axis 1 dengan colormap 'gray'.
ax[1].set_title("Input Citra 1")  # Memberikan judul "Input Citra 2" pada axis 1.

ax[2].imshow(output1, cmap='gray')  # Menampilkan output1 pada axis 2 dengan colormap 'gray'.
ax[2].set_title("Output Citra 1")  # Memberikan judul "Output Citra 1" pada axis 2.

ax[3].imshow(output2, cmap='gray')  # Menampilkan output2 pada axis 3 dengan colormap 'gray'.
ax[3].set_title("Output Citra 2")  # Memberikan judul "Output Citra 2" pada axis 3.

plt.show()

