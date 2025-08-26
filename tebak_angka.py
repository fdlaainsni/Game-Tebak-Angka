import random

def main():
    print("=" * 40)
    print("    SELAMAT DATANG DI GAME TEBAK ANGKA!")
    print("=" * 40)
    print("Saya telah memikirkan sebuah angka antara 1 dan 100")
    print("Coba tebak angka tersebut!")
    print("Ketik 'quit' untuk keluar dari game")
    print()
    
    # Inisialisasi variabel
    angka_rahasia = random.randint(1, 100)
    percobaan = 0
    max_percobaan = 7
    
    print(f"Anda memiliki {max_percobaan} kesempatan untuk menebak!")
    print("-" * 40)
    
    while percobaan < max_percobaan:
        try:
            # Input dari pemain
            tebakan = input(f"Percobaan ke-{percobaan + 1}: Masukkan tebakan Anda: ")
            
            # Cek apakah pemain ingin keluar
            if tebakan.lower() == 'quit':
                print("Terima kasih telah bermain! Sampai jumpa!")
                break
            
            # Konversi input ke integer
            tebakan = int(tebakan)
            
            # Validasi input
            if tebakan < 1 or tebakan > 100:
                print("❌ Harap masukkan angka antara 1 dan 100!")
                continue
            
            percobaan += 1
            
            # Cek tebakan
            if tebakan == angka_rahasia:
                print(f"🎉 SELAMAT! Anda berhasil menebak angka {angka_rahasia}!")
                print(f"Anda menebak dengan benar dalam {percobaan} percobaan!")
                
                # Berikan rating berdasarkan jumlah percobaan
                if percobaan <= 3:
                    print("⭐⭐⭐ Rating: LUAR BIASA!")
                elif percobaan <= 5:
                    print("⭐⭐ Rating: BAGUS!")
                else:
                    print("⭐ Rating: TIDAK BURUK!")
                break
                
            elif tebakan < angka_rahasia:
                sisa_percobaan = max_percobaan - percobaan
                print(f"📈 Terlalu kecil! Coba angka yang lebih besar.")
                if sisa_percobaan > 0:
                    print(f"Sisa percobaan: {sisa_percobaan}")
                    
            else:  # tebakan > angka_rahasia
                sisa_percobaan = max_percobaan - percobaan
                print(f"📉 Terlalu besar! Coba angka yang lebih kecil.")
                if sisa_percobaan > 0:
                    print(f"Sisa percobaan: {sisa_percobaan}")
            
            print("-" * 40)
            
        except ValueError:
            print("❌ Input tidak valid! Harap masukkan angka atau 'quit'.")
    
    # Jika percobaan habis
    if percobaan >= max_percobaan:
        print(f"💔 Sayang sekali! Percobaan Anda habis.")
        print(f"Angka yang benar adalah: {angka_rahasia}")
    
    # Tanya apakah ingin main lagi
    print("\n" + "=" * 40)
    main_lagi = input("Apakah Anda ingin bermain lagi? (y/n): ").lower()
    if main_lagi in ['y', 'yes', 'ya']:
        print("\n")
        main()  # Panggil fungsi main() lagi untuk game baru
    else:
        print("Terima kasih telah bermain! Sampai jumpa! 👋")

# Jalankan game
if __name__ == "__main__":
    main()
