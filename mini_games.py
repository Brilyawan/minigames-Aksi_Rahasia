import os

def clear_screen():
    """Membersihkan layar terminal."""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
        
def show_difficulty(difficulty_choice):
    """Menampilkan level kesulitan yang dipilih."""
    print(f"\nAnda memilih level kesulitan: {difficulty_levels.get(difficulty_choice, 'Tidak valid')}")

def show_story():
    """Menampilkan cerita permainan."""
    print(game_title)
    print("-" * 90)
    print(f"Perhatikan cerita di bawah ini:\n{story}")

def get_difficulty_choice():
    """Meminta dan mengembalikan pilihan level kesulitan dari pengguna."""
    while True:
        print("\nPilih level kesulitan:")
        for key, value in difficulty_levels.items():
            print(f"{key}. {value}")
        difficulty_choice = input("Masukkan nomor level kesulitan yang Anda pilih: ")
        if difficulty_choice in difficulty_levels:
            return difficulty_choice
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor 1, 2, atau 3.")
        
game_title = """
 ▄▄▄       ██ ▄█▀  ██████  ██▓    ██▀███   ▄▄▄       ██░ ██  ▄▄▄        ██████  ██▓ ▄▄▄      
▒████▄     ██▄█▒ ▒██    ▒ ▓██▒   ▓██ ▒ ██▒▒████▄    ▓██░ ██▒▒████▄    ▒██    ▒ ▓██▒▒████▄    
▒██  ▀█▄  ▓███▄░ ░ ▓██▄   ▒██▒   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▒▒██  ▀█▄  
░██▄▄▄▄██ ▓██ █▄   ▒   ██▒░██░   ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░██░░██▄▄▄▄██ 
 ▓█   ▓██▒▒██▒ █▄▒██████▒▒░██░   ░██▓ ▒██▒ ▓█   ▓██▒░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░██░ ▓█   ▓██▒
 ▒▒   ▓▒█░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░░▓     ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░
  ▒   ▒▒ ░░ ░▒ ▒░░ ░▒  ░ ░ ▒ ░     ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░
  ░   ▒   ░ ░░ ░ ░  ░  ░   ▒ ░     ░░   ░   ░   ▒    ░  ░░ ░  ░   ▒   ░  ░  ░   ▒ ░  ░   ▒   
      ░  ░░  ░         ░   ░        ░           ░  ░ ░  ░  ░      ░  ░      ░   ░        ░  ░
----------------------------------  by: Kristian Brilyawan  ----------------------------------
"""

story_intro = """
Selamat datang di 'Aksi Rahasia: Misi Membobol Rekening Bank'.
Suatu hari ada seseorang yang menghubungi Anda, dan bercerita 
bahwa dia sedang terperangkap dalam masalah keuangan besar.
Dia meminta bantuan Anda untuk membobol akun bank sesorang bernama 
Andre, untuk mengambil semua uang di dalam rekening tersebut.
Bantu klien Anda dengan membobol kata sandi akun bank Andre!
"""

story = """
Andre Sutejo adalah seorang direktur di salah satu perusahaan BUMN terbesar.
Andre sudah menikah dengan Tuti Jiyanti, dan mereka memiliki dua anak.
Anak pertama mereka adalah seorang laki-laki bernama Suparman, dan anak kedua mereka adalah seorang perempuan bernama Ida.
Mereka tinggal di desa terpencil bernama Konohagakure.
Di dekat kediaman mereka, terdapat sebuah warung makan yang sering mereka kunjungi bersama keluarga.

Andre dan Tuti sangat menyukai makanan pedas, sementara Suparman lebih suka makanan manis, dan Ida lebih menyukai makanan asin.
Makanan favorit Andre adalah kwetiaw pedas, sedangkan Tuti lebih menyukai mie rebus pedas.
Suparman sering memesan nasi goreng, sedangkan Ida lebih suka mie ayam.

Mereka adalah keluarga yang bahagia dan hidup dalam kemewahan.
"""

difficulty_levels = {
    "1": "Mudah",
    "2": "Sedang",
    "3": "Sulit"
}

clear_screen()
print(game_title)
print(story_intro)
print("-" * 70)
input("\nTekan enter untuk melanjutkan...\n")
clear_screen()
show_story()

input("\nTekan enter untuk memulai permainan...\n")
print(f"{'-' * 90}\n")

difficulty_choice = get_difficulty_choice()
clear_screen()

max_attempts = 0
if difficulty_choice == "1":
    max_attempts = 7
elif difficulty_choice == "2":
    max_attempts = 5
elif difficulty_choice == "3":
    max_attempts = 3
    
correct_password = "kecap"

attempts = 0
show_story()
show_difficulty(difficulty_choice)
print(f"{'='*78}\n{'='*12} Selamat datang di aplikasi m-banking 'Andre Sutejo' {'='*12}\n{'='*78}\n")
while attempts < max_attempts:
    guess = input("Masukkan kata sandi Anda: ")
    if guess.lower() == correct_password:
        print("\nSelamat! Anda berhasil membobol akun bank Andre Sutejo!")
        print("Anda berhasil membuka tabungan rahasia Andre dan membantunya keluar dari masalah keuangan.")
        break
    else:   
        print("Kata sandi salah. Coba lagi!")
        attempts += 1
        print(f"Anda memiliki {max_attempts - attempts} kesempatan tersisa.\n")
        
    if attempts == 2:
        print("Petunjuk: kata sandi terdiri dari '5' huruf\n\n")

    if attempts == 4:
        print("Petunjuk: berkaitan dengan anak pertama Andre\n\n")

    if attempts == 6:
        print("Petunjuk: berkaitan dengan bahan masakan\n\n")

if attempts == max_attempts:
    print("\nMaaf, Anda telah mencapai batas maksimum percobaan. Akun telah terblokir!")
    print("Anda gagal membantu klien Anda. Silakan coba lagi nanti.")

print("\nTerima kasih telah bermain 'Aksi Rahasia: Misi Membobol Rekening Bank'.")