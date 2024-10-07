# TUGAS NOMER DUA
nilai = int(input("masukkan nilai ujian anda (0-100): "))

if 100 >= nilai >= 90:
    print ("Feedback: sangat baik")
elif 89 >= nilai >= 80:
    print ("Feedback: baik")
elif 79 >= nilai >= 70:
    print ("Feedback: cukup")
elif 69 >= nilai >= 60:
    print ("Feedback: kurang")
else:
    print ("Feedback: sangat kurang")