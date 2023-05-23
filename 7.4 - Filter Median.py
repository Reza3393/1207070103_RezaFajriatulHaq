import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari library matplotlib untuk membuat visualisasi plot.
from skimage import data  # Mengimpor modul data dari library skimage untuk mengakses dataset citra bawaan.
from skimage.io import imread  # Mengimpor modul imread dari library skimage.io untuk membaca citra dari file.
from skimage.color import rgb2gray  # Mengimpor modul rgb2gray dari library skimage.color untuk mengkonversi citra RGB menjadi grayscale.
import numpy as np  # Mengimpor modul numpy untuk operasi array dan manipulasi data numerik.

citra1 = imread(fname="Image/boneka2.tif")  # Membaca citra "mobil.tif" menggunakan fungsi imread dan menyimpannya ke dalam variabel citra1.
citra2 = imread(fname="Image/mobil.tif")  # Membaca citra "boneka2.tif" menggunakan fungsi imread dan menyimpannya ke dalam variabel citra2.

print('Shape citra 1 : ', citra1.shape)  # Menampilkan bentuk (shape) dari citra1.
print('Shape citra 1 : ', citra2.shape)  # Menampilkan bentuk (shape) dari citra2.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))  # Membuat subplots dengan 1 baris dan 2 kolom, dengan ukuran gambar 10x10.
ax = axes.ravel()  # Meratakan array axes menjadi satu dimensi.

ax[0].imshow(citra1, cmap='gray')  # Menampilkan citra1 pada axis 0 dengan colormap 'gray'.
ax[0].set_title("Citra 1")  # Memberikan judul "Citra 1" pada axis 0.

ax[1].imshow(citra2, cmap='gray')  # Menampilkan citra2 pada axis 1 dengan colormap 'gray'.
ax[1].set_title("Citra 2")  # Memberikan judul "Citra 2" pada axis 1.

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

copyCitra1 = citra1.copy()  # Melakukan salinan (copy) dari citra1 ke variabel copyCitra1.
copyCitra2 = citra2.copy()  # Melakukan salinan (copy) dari citra2 ke variabel copyCitra2.

m1, n1 = copyCitra1.shape  # Mendapatkan ukuran baris (m1) dan kolom (n1) dari copyCitra1.
output1 = np.empty([m1, n1])  # Membuat array kosong dengan ukuran yang sama dengan copyCitra1.

m2, n2 = copyCitra2.shape  # Mendapatkan ukuran baris (m2) dan kolom (n2) dari copyCitra2.
output2 = np.empty([m2, n2])  # Membuat array kosong dengan ukuran yang sama dengan copyCitra2.

print('Shape copy citra 1 : ', copyCitra1.shape)  # Menampilkan bentuk (shape) dari copyCitra1.
print('Shape output citra 1 : ', output1.shape)  # Menampilkan bentuk (shape) dari output1.

print('m1 : ', m1)  # Menampilkan nilai m1.
print('n1 : ', n1)  # Menampilkan nilai n1.
print()

print('Shape copy citra 2 : ', copyCitra2.shape)  # Menampilkan bentuk (shape) dari copyCitra2.
print('Shape output citra 3 : ', output2.shape)  # Menampilkan bentuk (shape) dari output2.
print('m2 : ', m2)  # Menampilkan nilai m2.
print('n2 : ', n2)  # Menampilkan nilai n2.
print()

for baris in range(0, m1-1):  # Melakukan iterasi untuk setiap baris dalam citra.
    for kolom in range(0, n1-1):  # Melakukan iterasi untuk setiap kolom dalam citra.
        a1 = baris
        b1 = kolom
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1], \
              copyCitra1[a1, b1-1], copyCitra1[a1, b1], copyCitra1[a1, b1+1], \
              copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]]  # Mengumpulkan data dari sekitar piksel dalam list dataA.
        
        # Urutkan
        for i in range(1, 8):  # Melakukan iterasi dari indeks 1 hingga 7.
            for j in range(i, 9):  # Melakukan iterasi dari indeks i hingga 8.
                if dataA[i] > dataA[j]:  # Jika nilai dataA[i] lebih besar dari dataA[j], maka lakukan pertukaran.
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA
        
        output1[a1, b1] = dataA[5]  # Menetapkan nilai output1 pada baris a1 dan kolom b1 dengan nilai dataA indeks 5.


for baris in range(0, m2-1):  # Melakukan iterasi untuk setiap baris dalam citra.
    for kolom in range(0, n2-1):  # Melakukan iterasi untuk setiap kolom dalam citra.
        a1 = baris
        b1 = kolom
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1], \
              copyCitra2[a1, b1-1], copyCitra2[a1, b1], copyCitra2[a1, b1+1], \
              copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]]  # Mengumpulkan data dari sekitar piksel dalam list dataA.
        
        # Urutkan
        for i in range(1, 8):  # Melakukan iterasi dari indeks 1 hingga 7.
            for j in range(i, 9):  # Melakukan iterasi dari indeks i hingga 8.
                if dataA[i] > dataA[j]:  # Jika nilai dataA[i] lebih besar dari dataA[j], maka lakukan pertukaran.
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA
        
        output2[a1, b1] = dataA[5]  # Menetapkan nilai output2 pada baris a1 dan kolom b1 dengan nilai dataA indeks 5.


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

