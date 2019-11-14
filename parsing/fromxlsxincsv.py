import xlrd

import psycopg2
from psycopg2 import sql
import re
import os
import csv


path = '/home/fuckinggirl/arhiv/'  # your directory for data from Sanich's disk is here
print(path)
files = os.listdir(path)

passengers_values = []
flight_values = []
pof_values = []
data=[]
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




    data.append((passanger[0], passanger[1], passanger[3],passanger[4],Passanger_on_flight[2], Passanger_on_flight[3], Passanger_on_flight[4], Passanger_on_flight[5], Passanger_on_flight[0] ))

###########################################################################################################################################
#запишем все в свн
#имя фамилия отчество пол  номербилета класс кодхз хз кодполета
# Write CSV file

with open('test.csv', 'w') as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerow(["first_name", "last_name", "middle_name", "sex","eticket","class","strange_code", "sequence", "flight_code"])  # write header
    writer.writerows(data)