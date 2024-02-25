try:
    input_user = input("Masukkan suhu tubuh: ")
    suhu = int(input_user)
    if suhu >= 38 and suhu < 40:
        print("Demam ringan")
    elif suhu >= 40:
        print("Segera konsultasikan dengan dokter, suhu tubuh tinggi")
    else:
        print("Suhu tubuh normal")
except ValueError:
    print("Masukkan suhu tubuh dalam bentuk angka")