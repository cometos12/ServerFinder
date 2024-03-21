import os
from dotenv import load_dotenv

def wyswietl_menu():
    print("Witaj w ServerFinder!")
    print("1. Uruchom Program ip.py")
    print("2. Wyjście")

def sprawdz_licencje(licencja):
    load_dotenv()  
    prawidlowa_licencja = os.getenv("LICENCJA")
    return licencja == prawidlowa_licencja

def uruchom_ip_program():
    try:
        os.system("python ip.py")
    except Exception as e:
        print("Wystąpił błąd podczas uruchamiania programu ip.py:", e)

def main():
    licencja = input("Podaj licencję: ")
    if not sprawdz_licencje(licencja):
        print("Nieprawidłowa licencja. Program zostanie zakończony.")
        return

    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            if not os.path.exists("ip.py"):
                print("Plik ip.py nie istnieje w obecnym folderze.")
                continue
            uruchom_ip_program()
        elif wybor == '2':
            print("Wyłączyłeś Program!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
