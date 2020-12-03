import pymysql.cursors


def run_sql(sql):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 db='travel_agency')
    try:
        connection.commit()
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()


    finally:
        connection.close()


def show_results(sql):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 db='travel_agency')
    try:
        connection.commit()
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            desc = cursor.description

            for d in desc:
                print(f'{d[0]:<35}', end='')
            print()

            for row in rows:
                for i in range(0, len(row)):
                    print(f'{row[i]:<35}', end='')
                print()
    finally:
        connection.close()


def show_offers():
    sql = "SELECT o.id, o.name,  l.city_name AS city, c.name AS country," \
          " h.name as hotel, h.stars, o.trip_price FROM offer o " \
          "INNER JOIN location l ON o.location_id = l.id INNER JOIN country c" \
          " ON l.country_id = c.id INNER JOIN hotel h ON o.hotel_id = h.id "
    show_results(sql)
    choice = input("Czy chcesz zawęzić wyniki wyszukiwania?\n"
                   "1. Tak\n"
                   "2. Nie\n")
    if choice == "1":
        narrow_offer_search(sql)


def narrow_offer_search(sql):
    price = input("Jaki przedział cenowy wybierasz?\n"
                  "1. Poniżej 2000\n"
                  "2. Powyżej 2000\n"
                  "3. Obojętnie\n")
    standard = input("Jaki standard hotelu wybierasz?\n"
                     "1. Hostel\n"
                     "2. Hotele 3-, 4- i 5-gwiazdkowe\n"
                     "3. Obojętnie\n")
    price_sql = ""
    standard_sql = ""

    if price == "1":
        price_sql = "WHERE o.trip_price < 2000 "
    elif price == "2":
        price_sql = "WHERE o.trip_price > 2000 "

    sql += price_sql

    if price == "3" and (standard == "1" or standard == "2"):
        sql += "WHERE "
    elif price != "3" and (standard == "1" or standard == "2"):
        sql += "AND "
    if standard == "1":
        standard_sql += "h.stars = 0"
    elif standard == "2":
        standard_sql += "h.stars IN (\"3\",\"4\",\"5\")"

    sql += standard_sql

    show_results(sql)

def delete_offer():
    id_ = input("Podaj id wycieczki: ")
    sql = f"DELETE FROM offer WHERE id = '{id_}'"
    run_sql(sql)
    show_offers()


def show_client_info():
    sql = "SELECT * FROM `client`"
    show_results(sql)


def show_your_info(id_):
    sql = f"SELECT * FROM `client` WHERE id = \"{id_}\""
    show_results(sql)


def add_client():
    id_ = input("Podaj id nowego klienta: ")
    full_name = input("Podaj imię i nazwisko: ")
    phone_number = input("Podaj numer telefonu: ")
    sql = f"INSERT INTO client (id, full_name, phone_number) " \
          f"VALUES ('{id_}', '{full_name}', '{phone_number}')"
    run_sql(sql)
    show_client_info()


def delete_client():
    id_ = input("Podaj id klienta: ")
    sql = f"DELETE FROM client WHERE id = '{id_}'"
    run_sql(sql)
    show_client_info()