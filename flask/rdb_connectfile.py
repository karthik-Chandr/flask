from venv import create
import pymysql
conn = pymysql.connect(
    host = 'awsomescheduler-dbinstance.cozpto0jzcxq.us-east-1.rds.amazonaws.com',
    user = 'admin',
    password = 'password',
    db= 'awsschedulerdb',
)

def insert_meeting_details(date_from, date_to, skills, no_of_panelists):
    cur = conn.cursor()
    cur.execute("Insert into meetings(date_from, date_to, skills, no_of_panelists) values (%s,%s,%r,%s)", (date_from,date_to,tuple(skills),no_of_panelists))
    conn.commit()

def get_meeting_details():
    cur = conn.cursor()
    cur.execute("select * from meetings")
    details = cur.fetchall()
    return details

def insertPanelistDetails(selected_panelists):
    cur = conn.cursor()
    cur.execute("SELECT MAX( meeting_id ) FROM meetings;")
    x = cur.fetchall()
    print(x)
    print(str(x[0][0]))
    meeting_id = str(x[0][0])

    for i in selected_panelists:
        panelist_id = str(i[0])
        panelist_name = str(i[1])
        panelist_email = str(i[2])
        cur.execute("Insert into panelist_details(meeting_id, panelist_id, panelist_name, panelist_email) values (%s,%s,%s,%s)", (meeting_id, panelist_id, panelist_name, panelist_email))
        conn.commit()  

def get_emp_id(skills):
    inter_emp, emp_list = [], []
    print("skills 1:",skills)
    for i in range(len(skills)):
        cur = conn.cursor()
        print("each skill: ",skills[i])
        cur.execute("select e2.emp_id from employee e1 join emp_skills e2 on (e1.id = e2.emp_id) where e2.skills = (%s);", (skills[i]))
        details = cur.fetchall()
        inter_emp.extend(list(details))

    print("inter imp: ",inter_emp)
    for a in inter_emp:
        emp_list.append(a[0])

    print("emp_list: ",emp_list)

    return emp_list

def req_emp_details(no_of_panelists, emp_list_ascend):
    inter = ()
    if int(no_of_panelists)<len(emp_list_ascend):
        for i in range(int(no_of_panelists)):
            print(emp_list_ascend[i])

            cur = conn.cursor()
            cur.execute("select id, name, email_id from employee where id = (%s);", (emp_list_ascend[i]))
            details = cur.fetchall()
            # print(details)
            inter +=details
            # inter = (dict(details))
            # print(inter)
    else:
        for i in range(len(emp_list_ascend)):
            cur = conn.cursor()
            cur.execute("select id, name, email_id from employee where id = (%s);", (emp_list_ascend[i]))
            details = cur.fetchall()
            # print(details)
            inter +=details
    return inter

def get_meeting_id():
    cur = conn.cursor()
    cur.execute("SELECT MAX( meeting_id ) FROM meetings;")
    x = cur.fetchall()
    meeting_id = str(x[0][0])

    return meeting_id

def getRecordDetails():
    cur = conn.cursor()
    cur.execute("SELECT * FROM meeting_response")
    data = cur.fetchall()
    return data

def get_replaced_panelist(meeting_id):
    cur = conn.cursor()
    cur.execute('''SELECT employee.id, employee.name, employee.email_id
                FROM employee
                WHERE employee.id  NOT IN 
                    (SELECT panelist_details.panelist_id 
                    FROM panelist_details where panelist_details.meeting_id = (%s)
                    ORDER BY panelist_details.panelist_id); ''', (str(meeting_id)))
    data = cur.fetchall()
    return data

def replaceOldValues(meeting_id_old, panelist_name_old, replaced_data):
    cur = conn.cursor()
    cur.execute('''Update panelist_details SET panelist_id = (%s), panelist_name = (%s), panelist_email = (%s) 
                    WHERE meeting_id = (%s) and panelist_name = (%s)''', (str(replaced_data[0][0]), str(replaced_data[0][1]), str(replaced_data[0][2]), str(meeting_id_old), str(panelist_name_old)))
    cur.execute("DELETE from meeting_response WHERE meeting_id = (%s) and panelist_name = (%s)", (str(meeting_id_old), str(panelist_name_old)))
    conn.commit()
    cur.close()

def getDatesFromDB(meeting_id):
    cur = conn.cursor()
    cur.execute("select date_from, date_to from meetings where meeting_id = (%s);", (meeting_id))
    dates = cur.fetchall()
    return dates




#    *************************      EXECUTED SQL QUERIES     **********************************


# cursor.execute("select version()")
# data = cursor.fetchone()
# print(data)


#Create a database
# sql = '''create database awsomebuilderdb'''
# cursor.execute(sql)
# cursor.connect.commit()

#Create table
# create_table = '''create table employee(
#     id int not null auto_increment,
#     name text,
#     email_id text,
#     primary key (id))
#     '''
# cursor.execute(create_table)

# create_skill_table = '''create table emp_skills(
#     skill_id int NOT NULL auto_increment,
#     skills text,
#     emp_id int,
#     PRIMARY KEY (skill_id),
#     FOREIGN KEY (emp_id) REFERENCES employee(id))
#     '''
# cursor.execute(create_skill_table)

# create_avail_table = '''create table availability(
#     avail_id int NOT NULL auto_increment,
#     dates_not_available date,
#     emp_id int,
#     PRIMARY KEY (avail_id),
#     FOREIGN KEY (emp_id) REFERENCES employee(id))
#     '''
# cursor.execute(create_avail_table)

# create_meetings_table = '''create table meetings(
#     meeting_id int NOT NULL auto_increment,
#     date_from date NOT NULL,
#     date_to date NOT NULL,
#     no_of_panelists int NOT NULL,
#     emp_id int,
#     PRIMARY KEY (meeting_id),
#     FOREIGN KEY (emp_id) REFERENCES employee(id))
#     '''
# cursor.execute(create_meetings_table)

# create_response_table = '''create table meeting_response(
#     response_id int NOT NULL auto_increment,
#     meeting_id int,
#     emp_id int,
#     accept boolean,
#     PRIMARY KEY (response_id),
#     FOREIGN KEY (meeting_id) REFERENCES meetings(meeting_id),
#     FOREIGN KEY (emp_id) REFERENCES employee(id))
#     '''
# cursor.execute(create_response_table)




# Insert data
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Kelly Smith', 'rambledminddj@gmail.com')
# cursor.execute(sql)
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Jennifer Warren', 'donajain9@gmail.com')
# cursor.execute(sql)
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Sam Kent', 'rambledmind8@yahoo.com')
# cursor.execute(sql)
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Robin Williams', 'donajain@yahoo.com')
# cursor.execute(sql)
# conn.commit()


# sql = '''insert into emp_skills(skills, emp_id) values('%s', '%s') ''' % ('DevOps,AppDev', '2')
# cursor.execute(sql)

# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'DevOps,AppDev', 2 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'CIA (Cloud Infrastructure Architect),AppDev,Database', 1 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'DevOps,AppDev,Security,Database,CIA (Cloud Infrastructure Architect)', 3 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'DevOps,Security,AppDev', 4 );

# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'DevOps', 2 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'AppDev', 2 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'AppDev', 1 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'Database', 1 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'CIA (Cloud Infrastructure Architect)', 1 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'Database', 3 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'AppDev', 3 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'DevOps', 3 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'CIA (Cloud Infrastructure Architect)', 3 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'DevOps', 4 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'Security', 4 );
# INSERT INTO emp_skills (skills, emp_id) VALUES ( 'AppDev', 4 );

# alter table availability MODIFY avail_id INT AUTO_INCREMENT;
# INSERT INTO availability (dates_not_available, emp_id) VALUES ( '2022/07/15', 4 );
# INSERT INTO availability (dates_not_available, emp_id) VALUES ( '2022/07/22', 4 );
# INSERT INTO availability (dates_not_available, emp_id) VALUES ( '2022/07/27', 1 );
# INSERT INTO availability (dates_not_available, emp_id) VALUES ( '2022/07/13', 2 );
# INSERT INTO availability (dates_not_available, emp_id) VALUES ( '2022/07/19', 4 );
# INSERT INTO availability (dates_not_available, emp_id) VALUES ( '2022/07/25', 3 );
# INSERT INTO availability (dates_not_available, emp_id) VALUES ( '2022/07/26', 3 );
# INSERT INTO availability (dates_not_available, emp_id) VALUES ( '2022/07/27', 3 );



#Insert data
# sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Kelly Smith', 'kellysmith34552@gmail.com')
# cursor.execute(sql)
# db.commit()

#display
# sql = '''select * from employee'''
# cursor.execute(sql)
# cursor.fetchall()