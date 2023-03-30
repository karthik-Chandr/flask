from operator import itemgetter
import pymysql
from collections import Counter

conn = pymysql.connect(
    host = 'awsomescheduler-dbinstance.cozpto0jzcxq.us-east-1.rds.amazonaws.com',
    port = 3306,
    user = 'admin',
    password = 'password',
    db= 'awsschedulerdb',
)


# skills = ['DevOps','Security','AppDev']
# no_of_panelists = 3
# panelists = ''
# inter = ()
# final_panelist= []
# xyz = []
# g = []

# for i in range(len(skills)):

#     cur = conn.cursor()
#     cur.execute("select e2.emp_id from employee e1 join emp_skills e2 on (e1.id = e2.emp_id) where e2.skills = (%s);", (skills[i]))
#     details = cur.fetchall()
#     print(list(details))
#     xyz.extend(list(details))

# print(xyz)
# for a in xyz:
#     g.append(a[0])

# print(g)

# count = Counter(g)
# dic_count = dict(count)
# print(dic_count)

# print(list(dic_count.keys()))
# emp_list_ascend = list(dic_count.keys())

# if no_of_panelists<len(emp_list_ascend):
#     for i in range(no_of_panelists):
#         print(emp_list_ascend[i])

#         cur = conn.cursor()
#         cur.execute("select name, email_id from employee where id = (%s);", (emp_list_ascend[i]))
#         details = cur.fetchall()
#         print(details)
#         inter +=details
#         # inter = (dict(details))
#         print(inter)

# for x in inter:
#     print(x[0])
#     print(x[1])

# print(emp_list_ascend)
# print(len(emp_list_ascend))

# # DevOps
# # Security
# # CIA (Cloud Infrastructure Architect)
# # AppDev
# # Database



# abc = (343,)
# print(abc)
# print(abc[0])


# cur = conn.cursor()
# cur.execute("SELECT MAX( meeting_id ) FROM meetings;")
# x = cur.fetchall()
# print(x)
# print(str(x[0][0]))

# listsd = [2,3]
# inter = ()
# abc =2
# for i in range(len(listsd)):
#     cur.execute("select id, name, email_id from employee where id = (%s);", (listsd[i]))
#     details = cur.fetchall()
#     inter +=details

# print(inter)
# for i in inter:
#     print(i[1])
# print(inter[0][1])
# print(inter[1][1])



abcd = ((1, 'Robin Williams', 'donajain@yahoo.com'),)
print(abcd[0][1])


# cur = conn.cursor()
# cur.execute('''Update panelist_details SET panelist_id = (%s), panelist_name = (%s), panelist_email = (%s) 
#                 WHERE meeting_id = (%s) and panelist_name = (%s)''', (str(abcd[0][0]), str(abcd[0][1]), str(abcd[0][2]), "90", "Kelly Smith"))
# cur.execute("DELETE from meeting_response WHERE meeting_id = (%s) and panelist_name = (%s)", ("94", "Jennifer Warren"))

# conn.commit()
# cur.close()

# meeting_id = "91"
# cur = conn.cursor()
# cur.execute("select date_from, date_to from meetings where meeting_id = (%s);", (meeting_id))
# dates = cur.fetchall()
# print(dates)
# print(dates[0][0])
# print(dates[0][1])

# cursor = conn.cursor()
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Cooper Smith', 'rambledminddj@gmail.com')
# cursor.execute(sql)
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Steve Warren', 'donajain9@gmail.com')
# cursor.execute(sql)
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Stephen Johnson', 'rambledmind8@yahoo.com')
# cursor.execute(sql)
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Carla Robert', 'donajain@yahoo.com')
# cursor.execute(sql)
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Robert Cooper', 'rambledmind8@yahoo.com')
# cursor.execute(sql)
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Selena Martin', 'donajain@yahoo.com')
# cursor.execute(sql)



# conn.commit()


        