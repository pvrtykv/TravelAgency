import utils
import sys


def main_menu():
    choice = input("Witaj w systemie obsługi Biura Podróży!\n"
                   "Wpisz numer interesującej cię opcji:\n"
                   "1. Jestem klientem\n"
                   "2. Jestem pracownikiem\n"
                   "3. Wyjście z programu \n")

    if choice == "1":
        client_interface()
    elif choice == "2":
        employee_interface()
    elif choice == "3":m
        sys.exit()


def client_interface():
    choice = input("Wybierz:\n"
                   "1. Chcę wyświetlić dostępne wycieczki\n"
                   "2. Chcę wyświetlić swoje dane\n"
                   "3. Powrót do menu głównego\n"
                   )
    if choice == "1":
        utils.show_offers()
    elif choice == "2":
        id_ = input("Podaj swój numer identyfikacyjny:\n")
        utils.show_your_info(id_)
    elif choice == "3":
        main_menu()


def employee_interface():
    choice = input("Wybierz:\n"
                   "1. Chce wyświetlić dostępne wycieczki \n"
                   "2. Chcę wyświetlić dane o klientach \n"
                   "3. Powrót do menu głównego\n")

    if choice == "1":
        utils.show_offers()
    elif choice == "2":
        utils.show_client_info()
    elif choice == "3":
        main_menu()