# Program untuk membuat objek mahasiswa dengan atribut nama dan umur
class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)

mahasiswa1 = Mahasiswa("John", 20)
mahasiswa2 = Mahasiswa("Jane", 22)

# Menapilkan output
mahasiswa1.tampilkan_data()
mahasiswa2.tampilkan_data()
