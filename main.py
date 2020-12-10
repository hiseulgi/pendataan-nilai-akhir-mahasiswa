import pandas as pd

class Mahasiswa():

    def __init__(self):
        self.data = []
        self.jumlah = 0

    def tambah_data(self, nama, nim, nil_tugas, nil_uts, nil_uas):
        
        self.data.append({'Nama':nama,
                    'NIM':nim,
                    'Tugas':nil_tugas,
                    'UTS':nil_uts,
                    'UAS':nil_uas,
                    'Nilai Akhir':'',
                    'Predikat':''})
        
        self.jumlah += 1

# function
def get_option():
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
