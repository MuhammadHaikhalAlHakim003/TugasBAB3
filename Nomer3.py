# TUGAS NOMER TIGA
usia = int(input("masukkan usia anda: "))
darah = int(input("masukkan tekanan darah anda: "))

if usia >= 60 and darah > 140:
    print("status kesehatan: Tinggi")
elif usia >= 60 and darah <= 140:
    print("status kesehatan: Normal")
elif usia < 60 and darah > 130:
    print("status kesehatan: Tinggi")
elif usia < 60 and darah <= 130:
    print("status kesehatan: Normal")