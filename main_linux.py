import pandas as pd
from os import system
from time import sleep 

class Mahasiswa():

    def __init__(self):
        """
        inisialisasi class
        """
        self.data = []
        self.jumlah = 0

    def tambah_data(self, nama, nim, nil_tugas, nil_uts, nil_uas):
        """
        menambahkan data mahasiswa ke dalam list
        """
        self.data.append({'Nama':nama,
                    'NIM':nim,
                    'Tugas':nil_tugas,
                    'UTS':nil_uts,
                    'UAS':nil_uas,
                    'Nilai Akhir':'',
                    'Predikat':''})
        
        self.jumlah += 1
        
    def hitung_nilai_akhir(self):
        """
        menghitung nilai akhir berdasarkan rumus
        nil_akhir = nil_tugas * 0.3 + nil_uts * 0.3 + nil_uas * 0.4
        dan memasukkannya ke dalam list
        """
        index = self.jumlah - 1
        tugas = self.data[index]['Tugas'] * 0.3
        uts = self.data[index]['UTS'] * 0.3
        uas = self.data[index]['UAS'] * 0.4
        nil_akhir = tugas + uts + uas

        self.data[index]['Nilai Akhir'] = nil_akhir

    def cari_predikat(self):
        """
        menghitung predikat berdasarkan nilai akhir
        dan memasukkannya ke dalam list
        """
        index = self.jumlah - 1
        nil_akhir = self.data[index]['Nilai Akhir']

        if (nil_akhir >= 0 and nil_akhir < 20) :
            predikat = "E"
        elif (nil_akhir >= 20 and nil_akhir < 40) :
            predikat = "D"
        elif (nil_akhir >= 40 and nil_akhir < 60) :
            predikat = "C"
        elif (nil_akhir >= 60 and nil_akhir < 80) :
            predikat = "B"
        elif (nil_akhir >= 80 and nil_akhir < 100) :
            predikat = "A"

        self.data[index]['Predikat'] = predikat

    def tampilkan_data(self):
        """
        menampilkan data-data mahasiswa
        """
        df = pd.DataFrame(self.data)
        
        clear()
        print("="*50)
        print("Data Nilai Akhir Mahasiswa".center(50,' '))
        print("="*50)
        print(df)
        print("="*50)
        print()
        lanjut = input("Ketik apapun untuk lanjut! ")

    def hapus_data(self, index):
        """
        menghapus data mahasiswa
        """
        del self.data[index]
        self.jumlah -= 1

    def ekspor_data(self):
        """
        mengekspor file ke dalam file csv
        """
        df = pd.DataFrame(self.data)

        df.to_csv('data_mahasiswa.csv', mode='a', index=False, encoding="utf-8")
        print("Data telah diekspor ke dalam file CSV!")

# function
def clear():
    # fungsi membersihkan layar
    system('clear')
    
def get_option():
    # fungsi menampilkan menu utama
    clear()
    print("="*50)
    print("Program Pendataan Nilai Akhir Mahasiswa".center(50,' '))
    print("="*50)
    print("1. Tambahkan Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ekspor Data sebagai File CSV")
    print("5. Keluar")
    print("="*50)
    
    pilih = int(input("Masukkan pilihan : "))
    print()
    return pilih

def tambah():
    # fungsi menambah data mahasiswa
    print("1. Tambahkan Data")
    nama = input("Nama\t\t: ")
    nim = int(input("NIM\t\t: "))
    nil_tugas = int(input("Nilai Tugas\t: "))
    nil_uts = int(input("Nilai UTS\t: "))
    nil_uas = int(input("Nilai UAS\t: "))
    
    mahasiswa.tambah_data(nama, nim, nil_tugas, nil_uts, nil_uas)
    mahasiswa.hitung_nilai_akhir()
    mahasiswa.cari_predikat()
 
def hapus():
    # fungsi menghapus data mahasiswa
    print("3. Hapus Data")
    index = int(input("Masukkan Index Data \t: "))
    mahasiswa.hapus_data(index)
    print("Data pada index ke-", index, "telah terhapus!")
   
# main program
mahasiswa = Mahasiswa()
while (True):
    pilih = get_option()
 
    if (pilih == 1):
        tambah()
        sleep(0.5)
        
    elif (pilih == 2):
        mahasiswa.tampilkan_data()
        
    elif (pilih == 3):
        hapus()
        sleep(0.5)
        
    elif (pilih == 4):
        mahasiswa.ekspor_data()
        sleep(1)
        
    elif (pilih == 5):
        print("Keluar dari program!")
        break
        
    else:
        print("Tidak ada pilihan!")
        sleep(1)
