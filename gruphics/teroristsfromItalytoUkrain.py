#мы выяснили что надо искать людей, которые летели из италии на украину
# оружее они бы в багаже не повезли а самого багажа у них почти нет
# им больше 18 и они приемущественно мужчины
# они не платят банковской картой




# у нас есть 4 вида класса полета   - они летают самым дешевым - y
# select class from from_xlsx group by class;
#    class
# ------------
#  P
#  J
#  class
#  A
#  Y
# (5 строк)






import psycopg2


# топ 10 стран по приезду в них
from psycopg2 import sql

connection = psycopg2.connect(user = "test_user",
                                  password = "qwertyqwerty",
                                  host = "52.15.42.133",
                                  port = "5432",
                                  database = "bdzdum")

import matplotlib.pyplot as plt
connection.autocommit = True
cursor = connection.cursor()

insert = sql.SQL('select * from toppuplefromto({})').format(
    sql.SQL(',').join(map(sql.Literal, ['Italy','Ukraine']))
)
cursor.execute(insert)

people=cursor.fetchall()

for i in people:
# проверка на банковскую карту
    print(i[0],i[1])
#     insert = sql.SQL('select * from passangers_document where id={}').format(
#         sql.SQL(',').join(map(sql.Literal, [i[2]]))
#     )
#     cursor.execute(insert)
#     documents=cursor.fetchall()
#
#     if documents[0][2]:
#         print(documents[0][2])


    #проверка по классу





# проверка на возраст


# проверка на багаж






