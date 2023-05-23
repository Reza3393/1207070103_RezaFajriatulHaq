import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari library matplotlib untuk membuat visualisasi plot.
from skimage import data  # Mengimpor modul data dari library skimage untuk mengakses dataset citra bawaan.
from skimage.io import imread  # Mengimpor modul imread dari library skimage.io untuk membaca citra dari file.
from skimage.color import rgb2gray  # Mengimpor modul rgb2gray dari library skimage.color untuk mengkonversi citra RGB menjadi grayscale.
import numpy as np  # Mengimpor modul numpy untuk operasi array dan manipulasi data numerik.

citra1 = imread(fname="Image/mobil.tif")  # Membaca citra 1 dari file "mobil.tif".
citra2 = imread(fname="Image/boneka2.tif")  # Membaca citra 2 dari file "boneka2.tif".

print('Shape citra 1 : ', citra1.shape)  # Menampilkan shape citra 1.
print('Shape citra 1 : ', citra2.shape)  # Menampilkan shape citra 2.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))  # Membuat subplot dengan 1 baris dan 2 kolom.
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra 1 pada subplot pertama.
ax[0].set_title("Citra 1")  # Mengatur judul untuk subplot pertama.

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra 2 pada subplot kedua.
ax[1].set_title("Citra 2")  # Mengatur judul untuk subplot kedua.

#for baris=2 : tinggi-1
#    for kolom=2 : lebar-1
#        minPiksel = min([F(baris-1, kolom-1) F(baris-1, kolom) F(baris, kolom+1) ...
#            F(baris, kolom-1) F(baris, kolom+1) F(baris+1, kolom-1)  ...
#            F(baris+1, kolom) F(baris+1, kolom+1)]);
#        
#        maksPiksel = max([F(baris-1, kolom-1) F(baris-1, kolom) F(baris, kolom+1)    ...
#            F(baris, kolom-1) F(baris, kolom+1) F(baris+1, kolom-1)  ...
#            F(baris+1, kolom) F(baris+1, kolom+1)]);    
#            
#        if F(baris, kolom) < minPiksel
#           G(baris, kolom) = minPiksel;
#        else
#            if F(baris, kolom) > maksPiksel
#                G(baris, kolom) = maksPiksel;
#            else
#                G(baris, kolom) = F(baris, kolom);
#            end
#        end    
#    end
#end

copyCitra1 = citra1.copy()  # Membuat salinan citra 1.
copyCitra2 = citra2.copy()  # Membuat salinan citra 2.

m1, n1 = copyCitra1.shape  # Mendapatkan dimensi baris (m1) dan kolom (n1) citra 1.
output1 = np.empty([m1, n1])  # Membuat matriks kosong dengan dimensi yang sama seperti citra 1 untuk menyimpan output.

m2, n2 = copyCitra2.shape  # Mendapatkan dimensi baris (m2) dan kolom (n2) citra 2.
output2 = np.empty([m2, n2])  # Membuat matriks kosong dengan dimensi yang sama seperti citra 2 untuk menyimpan output.

print('Shape copy citra 1 : ', copyCitra1.shape)  # Menampilkan shape dari salinan citra 1.
print('Shape output citra 1 : ', output1.shape)  # Menampilkan shape dari output citra 1.

print('m1 : ', m1)  # Menampilkan nilai m1 (jumlah baris) citra 1.
print('n1 : ', n1)  # Menampilkan nilai n1 (jumlah kolom) citra 1.
print()

print('Shape copy citra 2 : ', copyCitra2.shape)  # Menampilkan shape dari salinan citra 2.
print('Shape output citra 3 : ', output2.shape)  # Menampilkan shape dari output citra 2.

print('m2 : ', m2)  # Menampilkan nilai m2 (jumlah baris) citra 2.
print('n2 : ', n2)  # Menampilkan nilai n2 (jumlah kolom) citra 2.
print()

for baris in range(0, m1-1):  # Looping untuk setiap baris citra.
    for kolom in range(0, n1-1):  # Looping untuk setiap kolom citra.

        a1 = baris  # Mengatur variabel 'a1' menjadi indeks baris saat ini.
        b1 = kolom  # Mengatur variabel 'b1' menjadi indeks kolom saat ini.

        arr = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1, b1+1], \
            copyCitra1[a1, b1-1], copyCitra1[a1, b1+1], copyCitra1[a1+1, b1-1],  \
            copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])  # Membuat array 'arr' yang berisi piksel-piksel tetangga sekitar dari citra 'copyCitra1' pada posisi (a1, b1).

        minPiksel = np.amin(arr)  # Menentukan piksel dengan nilai minimum dari array 'arr'.
        maksPiksel = np.amax(arr)  # Menentukan piksel dengan nilai maksimum dari array 'arr'.

        if copyCitra1[baris, kolom] < minPiksel:  # Jika piksel di citra 'copyCitra1' pada posisi (baris, kolom) kurang dari piksel dengan nilai minimum,
            output1[baris, kolom] = minPiksel  # Setel piksel di citra hasil (output1) pada posisi (baris, kolom) menjadi piksel dengan nilai minimum.
        else:
            if copyCitra1[baris, kolom] > maksPiksel:  # Jika piksel di citra 'copyCitra1' pada posisi (baris, kolom) lebih dari piksel dengan nilai maksimum,
                output1[baris, kolom] = maksPiksel  # Setel piksel di citra hasil (output1) pada posisi (baris, kolom) menjadi piksel dengan nilai maksimum.
            else:
                output1[baris, kolom] = copyCitra1[baris, kolom]  # Jika tidak, setel piksel di citra hasil (output1) pada posisi (baris, kolom) menjadi piksel asli dari citra 'copyCitra1'.

for baris1 in range(0, m2-1):  # Looping untuk setiap baris citra.
    for kolom1 in range(0, n2-1):  # Looping untuk setiap kolom citra.

        a1 = baris1  # Mengatur variabel 'a1' menjadi indeks baris saat ini.
        b1 = kolom1  # Mengatur variabel 'b1' menjadi indeks kolom saat ini.

        arr = np.array([copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1, b1+1], \
            copyCitra2[a1, b1-1], copyCitra2[a1, b1+1], copyCitra2[a1+1, b1-1],  \
            copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]])  # Membuat array 'arr' yang berisi piksel-piksel tetangga sekitar dari citra 'copyCitra2' pada posisi (a1, b1).

        minPiksel = np.amin(arr)  # Menentukan piksel dengan nilai minimum dari array 'arr'.
        maksPiksel = np.amax(arr)  # Menentukan piksel dengan nilai maksimum dari array 'arr'.

        if copyCitra2[baris1, kolom1] < minPiksel:  # Jika piksel di citra 'copyCitra2' pada posisi (baris1, kolom1) kurang dari piksel dengan nilai minimum,
            output2[baris1, kolom1] = minPiksel  # Setel piksel di citra hasil (output2) pada posisi (baris1, kolom1) menjadi piksel dengan nilai minimum.
        else:
            if copyCitra2[baris1, kolom1] > maksPiksel:  # Jika piksel di citra 'copyCitra2' pada posisi (baris1, kolom1) lebih dari piksel dengan nilai maksimum,
                output2[baris1, kolom1] = maksPiksel  # Setel piksel di citra hasil (output2) pada posisi (baris1, kolom1) menjadi piksel dengan nilai maksimum.
            else:
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1]  # Jika tidak, setel piksel di citra hasil (output2) pada posisi (baris1, kolom1) menjadi piksel asli dari citra 'copyCitra2'.
fig, axes = plt.subplots(2, 2, figsize=(10, 10))  # Membuat objek subplot dengan ukuran 2x2 dan ukuran gambar 10x10.
ax = axes.ravel()  # Melakukan ravel pada objek axes untuk mendapatkan array dari semua sumbu subplot.

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra 1 pada sumbu indeks 0.
ax[0].set_title("Input Citra 1")  # Menetapkan judul untuk sumbu indeks 0.

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra 2 pada sumbu indeks 1.
ax[1].set_title("Input Citra 2")  # Menetapkan judul untuk sumbu indeks 1.

ax[2].imshow(output1, cmap='gray')  # Menampilkan output citra 1 pada sumbu indeks 2.
ax[2].set_title("Output Citra 1")  # Menetapkan judul untuk sumbu indeks 2.

ax[3].imshow(output2, cmap='gray')  # Menampilkan output citra 2 pada sumbu indeks 3.
ax[3].set_title("Output Citra 2")  # Menetapkan judul untuk sumbu indeks 3.

plt.show()