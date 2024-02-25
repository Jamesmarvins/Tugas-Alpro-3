try:
    bilangan_str = input("Masukkan suatu bilangan: ")
    bilangan = int(bilangan_str)
    if bilangan == 0:
        print("Bilangan nol")
    elif bilangan > 0:
        print("Bilangan positif")
    else:
        print("Bilangan negatif")
except ValueError:
    print("Masukkan harus berupa bilangan bulat")