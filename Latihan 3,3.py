try:
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan < 1 or bulan > 12:
        print("Bulan yang dimasukkan tidak valid.")
    else:
        if bulan == 2:
            jumlah_hari = 29  
        elif bulan in [1, 3, 5, 7, 8, 10, 12]:
            jumlah_hari = 31
        else:
            jumlah_hari = 30
        print(f"Jumlah hari pada bulan {bulan} adalah {jumlah_hari}.")
except ValueError:
    print("Masukkan harus berupa angka.")