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
        
            def hitung_nilai_akhir(self):

        index = self.jumlah - 1
        tugas = self.data[index]['Tugas'] * 0.3
        uts = self.data[index]['UTS'] * 0.3
        uas = self.data[index]['UAS'] * 0.4
        nil_akhir = tugas + uts + uas

        self.data[index]['Nilai Akhir'] = nil_akhir

    def cari_predikat(self):

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
        df = pd.DataFrame(self.data)
        
        print("="*50)
        print("Data Nilai Akhir Mahasiswa".center(50,' '))
        print("="*50)
        print(df)
        print("="*50)
        print()

    def hapus_data(self, index):
        del self.data[index]

    def ekspor_data(self):
        df = pd.DataFrame(self.data)

        df.to_csv('data_mahasiswa.csv', mode='a', index=False, encoding="utf-8")
        print("Data telah diekspor ke dalam file CSV!")

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
