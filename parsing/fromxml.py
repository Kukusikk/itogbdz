import psycopg2


from lxml import etree
from copy import deepcopy

from psycopg2 import sql

connection = psycopg2.connect(user = "test_user",
                                  password = "qwertyqwerty",
                                  host = "52.15.42.133",
                                  port = "5432",
                                  database = "bdzdum")
connection.autocommit = True

cursor = connection.cursor()







def parseXML(xmlFile):
 """
 Парсинг XML
 """
 with open(xmlFile) as fobj:
     xml = fobj.read()
     root = etree.fromstring(xml)

     id_passagers=0
     for user in root.getchildren():

         fl=1
         insert_user={}
         id_passagers+=1
         insert_user['id']=id_passagers
         for userabout in user.getchildren():
             if(fl):
                 insert_user['firstname']=userabout.attrib['first']
                 insert_user['lastname'] = userabout.attrib['last']
                 #вставка пассажира
                 values = [
                     (insert_user['id'], insert_user['firstname'], insert_user['lastname'])
                 ]
                 insert = sql.SQL('INSERT INTO Passanger (id, first_name, last_name) VALUES {}').format(
                     sql.SQL(',').join(map(sql.Literal, values))
                 )

                 s=cursor.execute(insert)
                 fl=0
             else:
                 #все о карте
                 insert_documents={}
                 for card in userabout.getchildren():
                     insert_documents['numbercart'] = card.attrib['number']
                     insert_documents['id'] = insert_user['id'];
                     # вставка документов
                     values = [
                         (insert_documents['id'], insert_documents['numbercart'])
                     ]
                     insert = sql.SQL('INSERT INTO Passangers_document (id, Number_card) VALUES {}').format(
                         sql.SQL(',').join(map(sql.Literal, values))
                     )

                     cursor.execute(insert)
                     fl=1
                     for cardabout in card:
                         if(fl):
                             insert_fligth={}
                             insert_fligth['bonusprogramm'] = cardabout.text
                             fl=0
                         else:
                             for activity in cardabout.getchildren():

                                 # namefields=['Code', 'Date','Departure','Arrival','Fare']
                                 insert_airoport_from={}
                                 insert_airoport_to = {}
                                 insert_airoport_from['code'] = activity.getchildren()[3].text
                                 insert_airoport_to['code']=activity.getchildren()[2].text
                                 # вставка аэропорта прибытия

                                 values = [
                                     (insert_airoport_to['code'],'')
                                 ]
                                 insert = sql.SQL('INSERT INTO Airport (code,city) VALUES {}').format(
                                     sql.SQL(',').join(map(sql.Literal, values))
                                 )
                                 try:
                                     cursor.execute(insert)
                                 except:
                                     pass

                                 # вставка аэропорта улета
                                 values = [
                                     (insert_airoport_from['code'],'')
                                 ]
                                 insert = sql.SQL('INSERT INTO Airport (code,city) VALUES {}').format(
                                     sql.SQL(',').join(map(sql.Literal, values))
                                 )

                                 try:
                                     cursor.execute(insert)
                                 except:
                                     pass

                                 insert_fligth['Code']=activity.getchildren()[0].text
                                 insert_fligth['date'] = activity.getchildren()[1].text
                                 insert_fligth['airport_to'] = activity.getchildren()[2].text
                                 insert_fligth['airport_from'] = activity.getchildren()[3].text
                                 # вставка в таблицу fligth
                                 values = [
                                     (insert_fligth['bonusprogramm'], insert_fligth['Code'],insert_fligth['date'],insert_fligth['airport_to'],insert_fligth['airport_from'])
                                 ]
                                 insert = sql.SQL('INSERT INTO Fligth (bonus_program, flight_code, date, airport_to,airport_from) VALUES {}').format(
                                     sql.SQL(',').join(map(sql.Literal, values))
                                 )
                                 cursor.execute(insert)
                                 insert_passger_on_flight={}

                                 insert_passger_on_flight['flight_code']=insert_fligth['Code']
                                 insert_passger_on_flight['passage_code']=insert_user['id']
                                 # вставка в таблицу passger_on_flight
                                 values = [
                                     (insert_passger_on_flight['flight_code'], insert_passger_on_flight['passage_code'])
                                 ]
                                 insert = sql.SQL('INSERT INTO Passanger_on_flight (flight_code, pasanger_code) VALUES {}').format(
                                     sql.SQL(',').join(map(sql.Literal, values))
                                 )
                                 cursor.execute(insert)


















if __name__ == "__main__":
    parseXML("/home/fuckinggirl/Рабочий стол/labs_ds/бдз/PointzAggregator-AirlinesData.xml")
    cursor.close()
    connection.close()