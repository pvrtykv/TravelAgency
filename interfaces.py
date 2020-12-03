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
    elif choice == "3":
        sys.exit()


def client_interface():
    choice = input("Wybierz:\n"
                   "1. Wyświetl dostępne wycieczki\n"
                   "2. Wyświetl moje dane\n"
                   "3. Powrót do menu głównego\n"
                   )
    if choice == "1":
        utils.show_offers()
    elif choice == "2":
        id_ = input("Podaj swój numer identyfikacyjny:\n")
        utils.show_your_info(id_)
    elif choice == "3":
        main_menu()
    print()
    client_interface()


def employee_interface():
    choice = input("Wybierz:\n"
                   "1. Zarządzaj wycieczkami \n"
                   "2. Zarządzaj danymi klientów \n"
                   "3. Powrót do menu głównego\n")

    if choice == "1":
        manage_offers()
    elif choice == "2":
        manage_client_info()
    elif choice == "3":
        main_menu()
    employee_interface()


def manage_offers():
    choice = input("Wybierz: \n"
                   "1. Wyświetl dostępne oferty \n"
                   "2. Usuń ofertę\n")
    if choice == "1":
        utils.show_offers()
    elif choice == "2":
        utils.delete_offer()


def manage_client_info():
    choice = input("Wybierz:\n"
                   "1. Wyświetl dane klientów\n"
                   "2. Dodaj nowego klienta\n"
                   "3. Usuń klienta \n")
    if choice == "1":
        utils.show_client_info()
    elif choice == "2":
        utils.add_client()
    elif choice == "3":
        utils.delete_client()


