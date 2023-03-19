from fuzzywuzzy import fuzz
import pandas as pd
import sys

df = pd.read_csv('room_type.csv')
df.head(10)



x='y'
while True:
    
    print("\nSilakan pilih salah satu dari opsi di bawah ini:")
    print("1. Ratio")
    print("2. Partial Ratio")
    print("3. Token Set Ratio")
    print("4. Token Sort Ratio")
    print("5. Lihat data yang serupa")
    print("6. Lihat data yang sama")
    print("7. Keluar")
    
    choice = input("Masukkan nomor pilihan Anda: ")
    
    if choice == "1":
        str1 = input("Masukkan string pertama: ")
        str2 = input("Masukkan string kedua: ")
        
        ratio = fuzz.ratio(str1, str2)
        if ratio >= 90:
          kategori = 'Tinggi'
        elif ratio >= 50:
          kategori = 'Cukup'
        else:
          kategori = 'Rendah'
    
        print(f'Ratio dari :"{str1}" dan "{str2}" adalah {ratio}%')
        print( 'Kategori   :', kategori)
        x = input("Apakah ingin mengulang?y/n ")
        print("\n")
        
    elif choice == "2":
        str1 = input("Masukkan string pertama: ")
        str2 = input("Masukkan string kedua: ")
        
        ratio = fuzz.partial_ratio(str1, str2)
        if ratio >= 80:
          kategori = 'Tinggi'
        elif ratio >= 50:
          kategori = 'Cukup'
        else:
          kategori = 'Rendah'

      # Menampilkan hasil
        print(f'Partial ratio dari :"{str1}" dan "{str2}" adalah {ratio}%')
        print( 'Kategori           :', kategori)
        x = input("Apakah ingin mengulang?y/n ")
        print("\n")

    elif choice == "3":
        str1 = input("Masukkan string pertama: ")
        str2 = input("Masukkan string kedua: ")
        
        ratio = fuzz.token_set_ratio(str1, str2)
        if ratio >= 80:
            kategori = 'Tinggi'
        elif ratio >= 50:
            kategori = 'Cukup'
        else:
            kategori = 'Rendah'

        # Menampilkan hasil
        print(f'Token Set ratio dari :"{str1}" dan "{str2}" adalah {ratio}%')
        print( 'Kategori             :', kategori)
        x = input("Apakah ingin mengulang?y/n ")
        print("\n")
        
    elif choice == "4":
        str1 = input("Masukkan string pertama: ")
        str2 = input("Masukkan string kedua: ")
       
        ratio = fuzz.token_sort_ratio(str1, str2)
        if ratio >= 80:
            kategori = 'Tinggi'
        elif ratio >= 50:
            kategori = 'Cukup'
        else:
            kategori = 'Rendah'

        # Menampilkan hasil
        print(f'Token Sort ratio dari :"{str1}" dan "{str2}" adalah {ratio}%')
        print( 'Kategori              :', kategori)
        x = input("Apakah ingin mengulang?y/n ")
        print("\n")
        
    elif choice == "5":
       print("=============Lihat Data yang sama=============")
       def get_ratio(row):
        name1 = row ['Expedia']
        name2 = row ['Booking.com']

        return fuzz.token_set_ratio(name1, name2)

       df['set_token'] = df.apply(get_ratio, axis=1)

       x = len(df[df.apply(get_ratio, axis=1) > 85])/len(df)

       new_df = df.loc[df['set_token'] > 85, ['Expedia', 'Booking.com']] 

       print(new_df)
       print("\n") 
        
    elif choice == "6":
       def get_ratio(row):
        name1 = row ['Expedia']
        name2 = row ['Booking.com']

        return fuzz.ratio(name1, name2)

      # membuat kolom baru untuk menyimpan set token antara 'Expedia' dan 'Booking.com'
       df['set_token'] = df.apply(get_ratio, axis=1)

       x = len(df[df.apply(get_ratio, axis=1) > 99])/len(df)

       new_df = df.loc[df['set_token'] > 99, ['Expedia', 'Booking.com']]
       print("==========Data yang sama==========")
       print("==================================")
       print(x) 
       print(new_df) 

       x = input("Apakah ingin mengulang?y/n ")
       print("\n")
        
    elif choice == "7":
        print("Terima kasih telah menggunakan program ini.")
        sys.exit()
        
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
