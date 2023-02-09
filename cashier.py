class Transaction:
    def __init__(self):
        '''
        berfungsi untuk menginisialisasi class Transaction
        data_trans = dict untuk menyimpan data transaksi 
        '''
        self.data_trans = {}

  
    def add_item(self, nama_barang, jumlah_barang, harga_barang):
        '''
        Fungsi untuk menambahkan nama_item, jumlah dan harga barang ke dalam atributt
        class Transaction
        
        parameters:
        nama_barang   = str     barang yang dibeli (as key)
        jumlah_barang = int     jumlah barang yang dibeli (value)
        harga_barang  = int     harga barang yang dibeli (value)
          '''
        #input data ke dalam dictionary
        nama_barang = input('Masukkan nama barang: ')
        
        #input jumlah barang dengan checking validitas input user
        while True:
          jumlah_barang = input('Masukkan jumlah barang: ')
          if jumlah_barang.isnumeric():
            jumlah_barang = int(jumlah_barang)
            break
          else:
            print('Jumlah barang harus berupa angka.')
    
        #input harga barang dengan checking validitas input user
        while True:
          harga_barang = input('Masukkan harga barang: ')
          if harga_barang.isnumeric():
            harga_barang = int(harga_barang)
            break
          else:
            print('Harga barang harus berupa angka.')
      
        new_item = {nama_barang: [jumlah_barang, harga_barang]}
        self.data_trans.update(new_item)
        print(f'{nama_barang} dengan harga Rp. {harga_barang} sejumlah {jumlah_barang} buah berhasil dimasukkan keranjang belanja Anda.')


    def update_nama_barang(self, nama_barang, nama_baru):
        '''
        Berfungsi untuk mengoreksi/mengubah nama barang yang telah diinput 
        {nama_barang_baru} akan menggantikan key {nama_barang} sebelumnya
        
        parameters:
        nama_barang = nama barang semula
        nama_baru   = nama barang yang telah diperbarui 
        '''
        temp = self.data_trans[nama_barang]
        self.data_trans.pop(nama_barang)
        self.data_trans.update({nama_baru: temp})


    def update_jumlah_barang(self, nama_barang, jumlah_baru):
        '''
        fungsi untuk memperbarui jumlah barang yang telah terinput
        
        parameters:
        nama_barang   = nama barang 
        jumlah_baru   = jumlah barang yang telah diperbarui 
        
        '''
        self.data_trans[nama_barang][0] = jumlah_baru


    def update_harga_barang(self, nama_barang, harga_baru):
        '''
        fungsi untuk memperbarui jumlah barang yang telah terinput
       
        parameters:
        nama_barang   = nama barang 
        harga_baru    = harga barang yang telah diperbarui 
        
        '''
        self.data_trans[nama_barang][1] = harga_baru

   
    def delete_item(self):
        '''
        Berfungsi untuk menghapus item (nama barang, jumlah dan harga) 
        yang diinginkan dari dict data transaksi
        '''
        try:
          delete_barang = input('Masukkan nama barang yang akan dihapus: ')
          self.data_trans.pop(delete_barang)

          print(f'{delete_barang} telah dihapus dari keranjang belanja.')
          self.check_order()

        except KeyError:
          print(f'{nama_barang} tidak terdapat dalam keranjang belanja Anda.')

    
    def reset_transaction(self):
        '''
        Fungsi untuk mereset semua data yang ada di data transaksi
        '''
        self.data_trans.clear()

   
    def check_order(self):
        '''
        fungsi untuk mengecek data terbaru yang terecord dalam dictionary
        
        '''
        if(len(self.data_trans) == 0):
          print('Tidak ada barang di keranjang belanja Anda.')
        else:
          #print(self.data_trans)
          data = pd.DataFrame(self.data_trans).T
          data.columns = ['Jumlah Barang', 'Harga Barang']
          print(data.to_markdown())


    def total_price(self):
        '''
        Fungsi untuk menghitung total harga yang harus dibayarkan customer.
        ''' 

        #menjumlahkan total seluruh transaksi
        total_price = 0
        for value in self.data_trans.values():
            self.jumlah_barang = value[0]
            self.harga_barang = value[1]
            total_price += (self.jumlah_barang * self.harga_barang)


        #menghitung diskon
        if total_price > 200_000:
          diskon = int(total_price*0.05)
          total_price = int(total_price-diskon)
          print(f'Anda mendapatkan diskon sebesar 5%. Total belanja yang harus Anda bayarkan adalah Rp. {total_price}.')
          print('Terimakasih Atas Kunjungan Anda.')

        elif total_price > 300_000:
          diskon = int(total_price*0.08)
          total_price = int(total_price-diskon)
          print(f'Anda mendapatkan diskon sebesar 8%. Total belanja yang harus Anda bayarkan adalah Rp. {total_price}.')
          print('Terimakasih Atas Kunjungan Anda.')

        elif total_price > 500_000:
          diskon = int(total_price*0.1)
          total_price = int(total_price-diskon)
          print(f'Anda mendapatkan diskon sebesar 10%. Total belanja yang harus Anda bayarkan adalah Rp. {total_price}.')
          print('Terimakasih Atas Kunjungan Anda.')

        else:
          print(f'Total belanja Anda adalah {total_price}.')
          print('Terimakasih Atas Kunjungan Anda.')








