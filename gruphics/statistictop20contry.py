
# строим гистограмму топ стран по приезду в них
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
cursor.execute('select * from topactivitycontryto()')
a=cursor.fetchall()


for_colump=[i[1] for i in a]
for_name_colump=[i[0] for i in a]

s = [1, 2, 1, 5]
x = range(len(for_colump))
ax = plt.gca()
ax.bar(x, for_colump, align='edge') # align='edge' - выравнивание по границе, а не по центру
ax.set_xticks(x)
ax.set_xticklabels(for_name_colump)
plt.show()