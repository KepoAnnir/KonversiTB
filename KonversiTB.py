cm = 100
m = 1

while True:
    print("-- KONVERSI TINGGI BADAN --") 
    print("1. CM To M") 
    print("2. M To CM")
    print("0. Exit") 
    pilih = input("Pilih: ") 
    
    if pilih == "1":
        tbcm = int(input("\nCentimeter: "))
        print(f"Meter: {tbcm / cm}\n") 
        
    elif pilih == "2":
        tbm = float(input("\nM: "))
        print(f"Centimeter: {tbm * cm}\n")    
    
    else:
        print("\nMenu Tidak Ada!\n")  