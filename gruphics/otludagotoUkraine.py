#посмотрим из каких стран едут на украину

import psycopg2
from psycopg2 import sql
connection = psycopg2.connect(user = "test_user",
                                  password = "qwertyqwerty",
                                  host = "52.15.42.133",
                                  port = "5432",
                                  database = "bdzdum")


import matplotlib.pyplot as plt
connection.autocommit = True
cursor = connection.cursor()

insert = sql.SQL('select * from otkudaincountry({})').format(
    sql.SQL(',').join(map(sql.Literal, ['Ukraine']))
)
cursor.execute(insert)


a=cursor.fetchall()


for_colump=[i[1] for i in a]
for_name_colump=[i[0] for i in a]


x = range(len(for_colump))
ax = plt.gca()
ax.bar(x, for_colump, align='edge') # align='edge' - выравнивание по границе, а не по центру
ax.set_xticks(x)
ax.set_xticklabels(for_name_colump)
plt.show()