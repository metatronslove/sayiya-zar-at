import random
import time
from colorama import Fore, Back, Style, init

# Renkleri başlat
init(autoreset=True)

def zar_at():
    return random.randint(1, 6)

def sansli_sayilari_bul():
    sansli_sayilar = set()
    tur = 0

    print(Fore.CYAN + "\n★☆★ Şanslı Sayı Simülatörü ★☆★" + Style.RESET_ALL)
    print(Fore.YELLOW + "Her sayı için 2 zar atılıyor. 6-6 gelirse şanslı kabul ediliyor...\n")

    while len(sansli_sayilar) < 7:
        tur += 1
        print(Fore.MAGENTA + f"\n⏳ Tur {tur}:" + Style.RESET_ALL)

        for sayi in range(1, 91):
            if sayi in sansli_sayilar:
                continue

            print(Fore.WHITE + f"Sayı {sayi}: Zar atılıyor...", end="\r")
            time.sleep(0.05)

            zar1, zar2 = zar_at(), zar_at()
            renk = Fore.GREEN if zar1 == 6 and zar2 == 6 else Fore.RED
            print(Fore.WHITE + f"Sayı {sayi}: " + renk + f"{zar1}-{zar2}" + " " * 10, end="\r")

            if zar1 == 6 and zar2 == 6:
                sansli_sayilar.add(sayi)
                print(Fore.GREEN + f"\n🎉 Şanslı sayı: {Back.BLUE}{sayi}{Style.RESET_ALL} (Zar: {zar1}-{zar2})")
                if len(sansli_sayilar) == 7:
                    break
            time.sleep(0.05)

    # Sonuçlar
    print(Fore.CYAN + "\n╔════════════════════════════╗")
    print("║     ŞANS LİSTESİ (6-6)     ║")
    print("╚════════════════════════════╝" + Style.RESET_ALL)

    for i, sayi in enumerate(sorted(sansli_sayilar), 1):
        print(Fore.YELLOW + f"{i}. {Back.RED}{Fore.WHITE}{sayi}{Style.RESET_ALL}")

    print(Fore.GREEN + f"\n✨ Toplam {tur} turda 7 şanslı sayı bulundu!")

if __name__ == "__main__":
    sansli_sayilari_bul()