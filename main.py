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
