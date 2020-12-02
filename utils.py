import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             db='travel_agency')


def show_offers():
    try:
        connection.commit()

        with connection.cursor() as cursor:
            sql = "SELECT o.name, o.departure_date, l.city_name AS city, c.name AS country," \
                  " h.name as hotel, o.departure_date, o.return_date, o.trip_price FROM offer o " \
                  "INNER JOIN location l ON o.location_id = l.id INNER JOIN country c" \
                  " ON l.country_id = c.id INNER JOIN hotel h ON o.hotel_id = h.id"
            cursor.execute(sql)
            rows = cursor.fetchall()
            desc = cursor.description

            for d in desc:
                print(f'{d[0]:6}', end=' ')
            print()

            for row in rows:
                for i in range(0, len(row)):
                    print(row[i], end="\t")
                print()
    finally:
        connection.close()


def show_client_info():
    try:
        connection.commit()

        with connection.cursor() as cursor:
            sql = "SELECT * FROM `client`"
            cursor.execute(sql)
            rows = cursor.fetchall()
            desc = cursor.description

            for d in desc:
                print(f'{d[0]:6}', end=' ')
            print()

            for row in rows:
                for i in range(0, len(row)):
                    print(row[i], end="\t")
                print()
    finally:
        connection.close()


def show_your_info(id_):
    try:
        connection.commit()

        with connection.cursor() as cursor:
            sql = f"SELECT * FROM `client` WHERE id = \"{id_}\""
            cursor.execute(sql)
            rows = cursor.fetchall()
            desc = cursor.description

            for d in desc:
                print(f'{d[0]:6}', end=' ')
            print()
            # print(f'{desc[0][0]:<8} {desc[1][0]:<8} {desc[2][0]:>5}')

            for row in rows:
                for i in range(0, len(row)):
                    print(row[i], end="\t")
                print()
    finally:
        connection.close()
