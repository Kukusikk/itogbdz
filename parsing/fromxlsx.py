import xlrd

import psycopg2
from psycopg2 import sql
import re
import os

connection = psycopg2.connect(user="test_user",
                              password="qwertyqwerty",
                              host="52.15.42.133",
                              port="5432",
                              database="bdzdum")






# connection.autocommit = True
cursor = connection.cursor()

path = '/home/fuckinggirl/arhiv/'  # your directory for data from Sanich's disk is here
# path += os.path.sep
print(path)
files = os.listdir(path)

values_sel1 = []
values_upt1 = []
values_upt2 = []
values_upt3 = []

for f in files:
    print("file: ", f)
    wb = xlrd.open_workbook(path + f, on_demand=True)  # open excel file

    for sh in wb.sheets():  # work with each sheet
        # queryvars=["", "", "", sh.cell(2,0).value, sh.cell(4,0).value, sh.cell(6,3).value, sh.cell(6,7).value, sh.cell(8,0).value, sh.cell(8,2).value, sh.cell(4,3).value, sh.cell(4,7).value, sh.cell(2,7).value, sh.cell(0,7).value, sh.cell(12,4).value, sh.cell(12,1).value, sh.cell(2,5).value] #all values except null, unnecessary/not interesting; three first cells are for names
        passanger = ["", "", "", sh.cell(12, 1).value, sh.cell(2, 0).value]  # FN, LN, MN, Code, Sex
        Airport_from = [sh.cell(6, 3).value, sh.cell(4, 3).value, ""]  # Code, city, country
        Airport_to = [sh.cell(6, 7).value, sh.cell(4, 7).value, ""]  # Code, city, country
        Flight = [sh.cell(4, 0).value, sh.cell(6, 3).value, sh.cell(6, 7).value, sh.cell(8, 2).value,
                  sh.cell(8, 0).value, ""]  # Flight_code, Airport_from, airport_to, time, date, bounes = null
        Passanger_on_flight = ["", "", sh.cell(12, 4).value, sh.cell(2, 7).value, sh.cell(2, 5).value, sh.cell(0,
                                                                                                               7).value]  # GET FLIGHT CODE (ID) AFTER INERT, GET PASSENGERS CODE (ID) AFTER INERT, eticket, class, strange_code, seq

        tmpname = sh.cell(2,
                          1).value  # we wirk with name 'cause it is really, really bad in the original. Don't ever do it like this
        tmp = re.split(' ', tmpname)  # two/three words
        if len(tmp) == 3:
            if len(tmp[0]) == 1:
                passanger[2] = tmp[0]
                passanger[0] = tmp[1]
                passanger[1] = tmp[2]
            if len(tmp[1]) == 1:
                passanger[2] = tmp[1]
                passanger[0] = tmp[0]
                passanger[1] = tmp[2]
            if len(tmp[2]) == 1:
                passanger[2] = tmp[2]
                passanger[0] = tmp[0]
                passanger[1] = tmp[1]

        if len(tmp) == 2:
            passanger[0] = tmp[0]
            passanger[1] = tmp[1]

        # insert into DB
        # insert passanger
        # cursor.execute(insert_passenger)


        insert = 'select id from Passanger where  last_name=%s and first_name=%s'
        cursor.execute(insert, (passanger[1], passanger[0]))

        wtf=[]
        for row in cursor:
            id=row[0]
            wtf.append(row)
            if len(wtf)==2:
                break


        if len(wtf)==1:
            values_upt1.append((passanger[3], passanger[4], passanger[1], passanger[0]))
            insert = 'UPDATE Passanger SET  middle_name=%s, sex=%s where  first_name=%s and last_name=%s'
            if len(values_upt1)>100:
                cursor.executemany(insert, values_upt1)
                values_upt1=[]


        # -----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # insert flight   , sql.Literal(Airport_to[2], sql.Literal(Airport_to[3], sql.Literal(Airport_to[4])

            values_upt2.append(( Flight[3], Flight[0]))

        # проверим есть ли у нас строки с таким кодом

        insert = 'UPDATE Fligth SET  time=%s where  flight_code=%s  '
        if len(values_upt2)>100:
            cursor.execute(insert, values_upt2)
            values_upt2=[]


        Passanger_on_flight[0] = sh.cell(4, 0).value
        # # -----------------------------------------------------------------------------------------------------------------------------------------------------------------
        # # insert pidor
        #
        if len(wtf) == 1:
            values_upt3.append(
                ( Passanger_on_flight[2], Passanger_on_flight[3],
                 Passanger_on_flight[4], Passanger_on_flight[5],
                  Passanger_on_flight[0], id,)
            )
            insert = 'UPDATE Passanger_on_flight SET eticket=%s, class=%s, strange_code=%s, sequence=%s where  flight_code=%s and  pasanger_code=%s '
            if len(values_upt3) > 100:
               cursor.execute(insert, values_upt3)
               values_upt3=[]

insert = 'UPDATE Passanger SET  middle_name=%s, sex=%s where  code=%s'
if len(values_upt1) > 0:
    cursor.executemany(insert, values_upt1)

insert = 'UPDATE Fligth SET  time=%s where  flight_code=%s  '
if len(values_upt2) > 0:
    cursor.execute(insert, values_upt2)

insert = 'UPDATE Passanger_on_flight SET eticket={}, class={}, strange_code={}, sequence={} where  flight_code={} and  pasanger_code={} '
if len(values_upt3) > 0:
    cursor.execute(insert, values_upt3)
