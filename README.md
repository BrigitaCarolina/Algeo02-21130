# Algeo02-21130
Tugas Besar 2 Aljabar Linier dan Geometri Kelompok "Tatata"
1. Althaaf Kasyi Atisomya - 13521130 
2. Cetta Reswara Parahita - 13521133
3. Brigita Tri Carolina - 13521156

# Gambaran Program 
Program ini dibuat dengan menggunakan bahasa pemrograman python dengan library-library yang ada di dalamnya, yaitu:
* OpenCV 
* Numpy 
* Tkinter 
* Pillow 

Program face recognition ini menggunakan metode eigenface dalam proses mengenali sekumpulan citra wajah yang kemudian di-extract dan direpresentasikan dalam bentuk matriks eigenface. Citra wajah yang akan di-extract oleh program di antaranya adalah citra wajah pada dataset dan citra wajah dari data masukan user (dalam program ini bisa juga menerima input data citra wajah dari webcam). Kemudian setelah dataset dan test image direpresentasikan dalam bentuk matriks eigenface, dicari euclidian distance paling kecil antara image-image pada dataset dengan test image, yang selanjutnya image yang memiliki euclidian distance paling kecil tersebut adalah image yang dianggap program paling menyerupai test image.

# Langkah Menggunakan Program
1. Jalankan file gui.py pada terminal yang sudah terinstall python versi 3 atau langsung klik dua kali pada file Face Recognition App.exe 
2. Tekan tombol choose folder untuk memilih folder dataset 
3. Tekan tombol choose file untuk memilih file input 
4. Tekan tombol calculate untuk menjalankan program
5. Result akan muncul pada closest result dalam bentuk gambar
6. Setelah proses result yang diinginkan tampil, user dapat menggunakan program kembali dengan menekan tombol clear result

# Fitur Tambahan 
1. Terdapat tombol use webcam jika user ingin menggunakan webcam untuk data masukan test image langsung dari webcam 
2. Setelah menekan tombol, program akan men-capture foto sekali untuk dimasukkan ke dataset
3. Kemudian program akan menjalankan webcam, menunggu 10 detik dan men-capture foto live dari webcam setiap 10 detik sekali 
4. Webcam kemudian akan berhenti 
5. User dapat memasukkan kembali dataset dan data input yang tadi sudah berupa capture foto live dari webcam 
6. Tekan tombol calculate dan program akan berjalan seperti biasanya
7. User dapat melihat result yang bertuliskan couldn't find matching image ketika tidak ada image yang cocok di dataset berdasarkan threshold tertentu 
8. User dapat melihat result matching image is found ketika terdapat image yang dikenali program paling mirip di dataset 
