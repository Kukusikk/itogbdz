
# мы решили продолжить расследование и благодаря 2м преждним гистограммам заметели странности в положении дел на украине
import re

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

cursor.execute('select activitycountry(%s)',('Ukraine',))
a=cursor.fetchall()

res=re.split(r',', a[0][0])
for_colump=[int(res[0][1:]), int(res[1][:len(res[1])-1])]



x = range(len(for_colump))
ax = plt.gca()
ax.bar(x, for_colump, align='edge') # align='edge' - выравнивание по границе, а не по центру
ax.set_xticks(x)
ax.set_xticklabels(('приехало','уехало'))
plt.show()