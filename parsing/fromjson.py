import psycopg2
import json
# из этого файла будет добавленa страна для рейсов

from psycopg2 import sql

connection = psycopg2.connect(user = "test_user",
                                  password = "qwertyqwerty",
                                  host = "localhost",
                                  port = "5432",
                                  database = "bdzdum")
connection.autocommit = True

cursor = connection.cursor()


def parseJSON(jsonFile):

# этот файл нам ничего не дал так как не номера паспорта не номера карты тут нет
        with open(jsonFile, "r") as read_file:
            data = json.load(read_file)
            data=data['Forum Profiles']

            values = []

            for Profile in data:
                #эта проверка дала нам невозможность заявить о новых пассажирах
                # passport_num=Profile['Travel Documents'][0]['Passports']
                # if not passport_num:
                #     continue
                # print(8)
                for i in Profile['Registered Flights']:
                    insert_contry_airoportfrom=i['Arrival']['Country']
                    insert_contry_airoportto=i['Departure']['Country']
                    insert_code_airoportfrom = i['Arrival']['Airport']
                    insert_code_airoportto = i['Departure']['Airport']

                    values.append((insert_contry_airoportto,insert_code_airoportto,))
                    values.append((insert_contry_airoportfrom,insert_code_airoportfrom,))
                    if len(values) > 1000:
                        cursor.executemany('UPDATE Airport SET  country=%s  where  code=%s', values)
                        values = []

                    # cursor.execute('UPDATE Airport SET  country=%s  where  code=%s ', (insert_contry_airoportto,insert_code_airoportto ))
                    # cursor.execute('UPDATE Airport SET  country=%s  where  code=%s ', (insert_contry_airoportfrom,insert_code_airoportfrom ))
            if len(values) > 0:
                cursor.executemany('UPDATE Airport SET  country=%s  where  code=%s', values)

if __name__ == "__main__":

    parseJSON("/home/fuckinggirl/Рабочий стол/labs_ds/бдз/FrequentFlyerForum-Profiles.json")