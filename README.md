# SuperCashier-Project
SuperCashier merupakan program yang digunakan sebagai sistem transaksi kasir self-service, yang bertujuan agar customer dapat melakukan proses pembayaran secara mandiri. Program ini dibuat dengan menggunakan bahasa pemrograman Python dengan menerapkan beberapa method atau objek serta menerapkan prinsip clean code (PEP8).

# Objectives
Customer supermarket dapat bertindak sebagai kasir dengan menginput items belanjaan dan melakukan pembayaran sesuai nominal yang ditampilkan secara mandiri. 

# Flowchart
![Untitled Diagram](https://user-images.githubusercontent.com/119783447/217859030-8fb509ee-c1c6-487b-969b-b5b690e2b226.jpg)

1. Membuat ID Transaksi
2. Memasukkan item yang akan dibeli dengan menginput parameter berikut:<br />
   a. nama item <br />
   b. jumlah item <br />
   c. harga barang
3. Jika terdapat kesalahan input (baik nama, jumlah ataupun harga barang), maka customer dapat melakukan update item sebagai berikut: <br />
   a. update nama item <br />
   b. update jumlah item <br />
   c. update harga item
4. Jika batal membeli item tertentu, customer dapat melakukan: <br />
   a. menghapus salah satu item <br />
   b. menghapus keseluruhan transaksi (reset transaksi)  
5. Untuk final checking, customer dapat memeriksa apakah item yang diinput sudah sesuai menggunakan “check order” dengan output : <br />
   a. Mengeluarkan seluruh rincian transaksi (nama item, jumlah item, harga dan total harga) 
6. Menghitung total belanja menggunakan “total price” dengan memperhitungkan perolehan diskon sesuai ketentuan berikut: <br />
   a. Transaksi lebih dari Rp 200.000 mendapat diskon 5%<br />
   b. Transaksi lebih dari Rp 300.000 mendapat diskon 8%<br />
   c. Transaksi lebih dari Rp 500.000 mendapat diskon 10%
   
# Program Description
## 1. __init__ ()
  Berfungsi untuk menginisialisasi class Transaction.<br />
> data_trans = dict untuk menyimpan seluruh data transaksi.
## 2. add_item (nama_barang, jumlah_barang, harga_barang)
  Berfungsi untuk menambahkan nama_item, jumlah dan harga barang ke dalam atribut class Transaction.<br />
 > Parameter yang digunakan: <br />
 nama_barang   = str, barang yang dibeli (as key) <br />
 jumlah_barang = int, jumlah barang yang dibeli (value) <br />
 harga_barang  = int, harga barang yang dibeli (value)
## 3. update_nama_barang (nama_barang, nama_baru)
  Berfungsi untuk mengoreksi/mengubah nama barang yang telah diinput.<br />
  {nama_barang_baru} akan menggantikan key {nama_barang} sebelumnya.
 > Parameter yang digunakan: <br />
 nama_barang = nama barang semula  <br />
 nama_baru   = nama barang yang telah diperbarui 
## 4. update_jumlah_barang (nama_barang, jumlah_baru)
  Berfungsi untuk mengoreksi/mengubah jumlah barang yang telah diinput. <br />
  {jumlah_baru} akan menggantikan {jumlah_barang} sebelumnya.
  > Parameter yang digunakan: <br />
  nama_barang = nama barang   <br />
  jumlah_baru = jumlah barang yang telah diperbarui 
## 5. update_harga_barang (nama_barang, harga_baru)
  Berfungsi untuk mengoreksi/mengubah harga barang yang telah diinput. <br />
  {harga_baru} akan menggantikan {harga_barang} sebelumnya.
  > Parameter yang digunakan: <br />
  nama_barang = nama barang   <br />
  jumlah_baru = jumlah barang yang telah diperbarui 
## 6. delete_item()
  Berfungsi untuk menghapus item (nama, jumlah dan harga barang) yang diinginkan dari dict data transaksi.
  > delete_barang = str, untuk memasukkan nama barang yang akan dihapus menggunakan user input.
## 7. reset_transaction()
  Berfungsi untuk mereset semua data yang ada di data transaksi.
## 8. check_order()  
  Berfungsi untuk mengecek data terbaru yang terecord dalam dictionary.
  >data.columns = ['Jumlah Barang', 'Harga Barang'] <br />
  att data.columns ditampilkan dalam bentuk tabulasi menggunakan library pandas dataFrame.
## 9. total_price()
  Berfungsi untuk menghitung total harga yang harus dibayarkan customer. <br />
### menghitung diskon:<br />
  diskon = int(total_price*0.05)<br />
  total_price = int(total_price-diskon)<br />
  >jika total_price > 200000, maka diskon 5%<br />
  jika total_price > 300000, maka diskon 8%<br />
  jika total_price > 500000, maka diskon 10%
  
# Test-Case Report
## 1. Add Item
Penambahan data baru dengan menggunakan input user.
<img width="638" alt="Screen Shot 2023-02-09 at 23 36 18" src="https://user-images.githubusercontent.com/119783447/217878438-04fb6cc1-18de-478a-a1bf-ed51b67abf16.png">
   
Program akan memberikan warning jika tipe data yang diinput tidak sesuai, dan akan melakukan proses looping hingga user menginput data yang benar.

<img width="628" alt="Screen Shot 2023-02-09 at 23 41 43" src="https://user-images.githubusercontent.com/119783447/217880170-943bb354-b0a3-49bd-a1cd-dc0a1df0d251.png">

Setelah data terinput dengan benar, program akan memberi notifikasi "succesfull."
<img width="1003" alt="Screen Shot 2023-02-09 at 23 44 35" src="https://user-images.githubusercontent.com/119783447/217880862-e7f4a566-9293-417f-a961-8e937844950b.png">

## 2. Delete Item
Menghapus item (nama, jumlah dan harga barang) yang diinginkan dari dict data transaksi menggunakan input user.
<img width="569" alt="Screen Shot 2023-02-09 at 23 48 45" src="https://user-images.githubusercontent.com/119783447/217882921-4b3c0b53-ef71-402d-b92c-bfc4d747c978.png">

Setelah menginput item yang ingin dihapus, program akan mengeluarkan output berupa konfirmasi barang yang berhasil dihapus dan menampilkan data yang tersisa dalam dictionary.

<img width="606" alt="Screen Shot 2023-02-09 at 23 49 20" src="https://user-images.githubusercontent.com/119783447/217882613-963cc4b2-a0cd-4719-a529-8d2bc15f3cc5.png">

## 3. Update Item
### Update Nama Barang
Mengubah nama barang "Ayam Goreng" menjadi "Fried Chicken" menampilkan output sebagai berikut:
<img width="605" alt="Screen Shot 2023-02-09 at 23 56 19" src="https://user-images.githubusercontent.com/119783447/217884161-ceb6d5fe-76b7-4f05-ae38-ca2c087af466.png">

### Update Jumlah Barang
Mengubah jumlah barang "Pasta Gigi", dengan jumlah awal 3 buah menjadi 10 buah.
<img width="611" alt="Screen Shot 2023-02-09 at 23 59 37" src="https://user-images.githubusercontent.com/119783447/217884683-d4880e67-d696-40d0-9465-597ad21421cb.png">

### Update Harga Barang
Mengubah harga barang "Pasta Gigi", dengan harga awal 15000 menjadi 29000.
<img width="604" alt="Screen Shot 2023-02-10 at 00 00 50" src="https://user-images.githubusercontent.com/119783447/217884959-face9cf2-b653-4a5e-922d-9352185ee208.png">

## 4. Reset Item
Menghapus seluruh data yang tersimpan dalam dictionary. Program akan memberikan output bahwa seluruh item telah berhasil dihapus.
<img width="603" alt="Screen Shot 2023-02-10 at 00 04 15" src="https://user-images.githubusercontent.com/119783447/217885927-952fad65-d159-481a-bf6a-aa3063d92177.png">

## 5. Count Total Price
Menghitung total harga yang harus dibayarkan customer, dengan atau tanpa kondisi mendapatkan diskon.<br />
Output untuk total pembayaran dengan total belanja >200.000 dan diskon 5%:
<img width="1006" alt="Screen Shot 2023-02-10 at 00 05 35" src="https://user-images.githubusercontent.com/119783447/217886639-9b7d907a-863a-4376-84e4-a07ca35a5774.png">

## 6. Check Order
Menampilkan data yang merupakan daftar belanja yang tersimpan dalam dictionary.
<img width="508" alt="Screen Shot 2023-02-10 at 00 09 02" src="https://user-images.githubusercontent.com/119783447/217886920-91aec7e0-2721-4abf-a431-eb1b132fe123.png">

# Conclusion
SuperCashier sudah dapat digunakan sebagai sistem transaksi self-service cashier yang layak dan easy to use. 


  
   





