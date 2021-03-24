print ("=============================================")
print ("Soal 4 Tugas 4")
print ("=============================================")

x = int(input("Berapa usia kamu :"))
y = input("Apakah sudah lulus ujian kualifikasi (Y/T):").upper()

if x >= 21 and y == "Y":
    print("Anda dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")