
# Program Penjualan Toko Apel Online Store

Portofolio Capstone Project Modul 1 Purwadhika Job Connector Data Science On Campus Batch 26 (JCDS-2604-002) - Kevin Matthew Aditya

## Deskripsi Data
Berikut ini data produk yang dipakai dalam program penjualan toko  :
| ID | Product             | Category   | Warranty   | Price     | Stock |
|----|---------------------|------------|------------|-----------|-------|
| 1  | Macbook Air         | Laptop     | 2 Year     | 22,000,000 | 15    |
| 2  | Macbook Pro         | Laptop     | 2 Year     | 32,000,000 | 15    |
| 3  | iMac                | Desktop    | 2 Years    | 30,000,000 | 10    |
| 4  | iPad Pro            | Tablet     | 1 Year     | 21,000,000 | 20    |
| 5  | iPad Air            | Tablet     | 1 Year     | 12,000,000 | 20    |
| 6  | iPad Mini           | Tablet     | 1 Year     | 10,000,000 | 20    |
| 7  | iPhone 15 Pro       | Smartphone | 1 Year     | 25,000,000 | 30    |
| 8  | iPhone 15           | Smartphone | 1 Year     | 20,000,000 | 30    |
| 9  | iPhone 14 Pro       | Smartphone | 1 Year     | 15,000,000 | 25    |
| 10 | iPhone 14           | Smartphone | 1 Year     | 11,000,000 | 25    |
| 11 | iPhone 13           | Smartphone | 1 Year     | 10,000,000 | 20    |
| 12 | iPhone 12           | Smartphone | 1 Year     | 8,000,000  | 15    |
| 13 | Apple Watch Ultra   | Wearable   | 6 Months   | 15,000,000 | 20    |
| 14 | Apple Watch SE      | Wearable   | 6 Months   | 6,000,000  | 15    |
| 15 | AirPods Pro         | Accessory  | 6 Months   | 4,500,000  | 30    |
| 16 | AirPods Max         | Accessory  | 6 Months   | 8,000,000  | 30    |



# Apel Online Store
Selamat datang di Apel Online Store! 🎉

Ini adalah aplikasi Python yang dirancang khusus untuk membantu kamu mengelola toko dengan cara yang mudah dan efisien. Dengan aplikasi ini, kamu bisa melakukan banyak hal untuk mengatur produk, membuat pesananan, dan memantau stok barang.

## Sub Menu 1 : View Product List
Sub-menu ini menampilkan daftar produk yang dijual di toko ini. Untuk menutup tampilan daftar produk, user cukup dengan menekan tombol "Enter".

## Sub Menu 2 : Add Product (Admin)
Sub-menu ini akan menambahkan produk beserta dengan detailnya kedalam daftar produk. User diminta untuk memasukan produk baru yang belum ada di daftar produk. Selanjutnya user diminta untuk konfirmasi penambahan produk. Untuk menu ini hanya dapat diakses oleh manajer toko yang memiliki password admin.

## Sub Menu 3 : Remove Product (Admin)
Sub-menu ini akan menghapus produk pada daftar produk. User memilih produk yang akan dihapus dengan memasukan id produk. Kemudian user diminta melakukan konfirmasi penghapusan produk. Untuk menu ini hanya dapat diakses oleh manajer toko yang memiliki password admin.

## Sub Menu 4 : Update Product (Admin)
Sub-menu ini akan mengubah harga dan stok produk yang ada di daftar produk. User memilih menu untuk melakukan perubahan pada harga, stok, atau harga dan stok. Selanjutnya user diminta untuk mengkonfirmasi perubahan produk. Untuk menu ini hanya dapat diakses oleh manajer toko yang memiliki password admin.

## Sub Menu 5 : Create Order
Sub-menu ini digunakan oleh karyawan toko  untuk memasukan pesanan pelanggan. Tambahan fitur yang ada di sub-menu ini adalah kode promo. Setelah memasukan pesanan, user diminta untuk memasukan kode promo jika ada. Apabila kode promo yang dimasukan sesuai, maka pelanggan akan mendapatkan potongan harga. Harga normal diberlakukan apabila tidak mempunyai kode promo yang sesuai.

## Sub Menu 6 : Sales Report
Sub-menu ini menunjukan laporan penjualan dalam bentuk tabel. Pada kesimpulan terdapat informasi mengenai total penjualan dan total potongan harga. Menu ini dapat digunakan oleh menejer maupun karyawan toko untuk keperluan laporan keuangan toko.

## Sub Menu 7 : Monitoring Stock
Sub-menu ini sangat berguna untuk program penjualan toko yaitu melakukan sortir pada stok barang di daftar produk. Stok barang dapat disortir dari volume terbesar atau dari volume terkecil tergantung kebutuhan user.

## Sub Menu 8 : Exit
Sub-menu ini akan membuat user keluar dari program.
