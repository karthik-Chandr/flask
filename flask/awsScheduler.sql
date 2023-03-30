-- This document contains all the initial scripts required to run this application --

--- Queries to create the tables ---

create table employee(
	id int not null auto_increment,
	name text, email_id text,
	primary key (id));
    
create table emp_skills(
    skill_id int NOT NULL auto_increment,
    skills text,
    emp_id int,
    PRIMARY KEY (skill_id),
    FOREIGN KEY (emp_id) REFERENCES employee(id));
    
create table availability(
    avail_id int NOT NULL auto_increment,
    dates_not_available date,
    emp_id int,
    PRIMARY KEY (avail_id),
    FOREIGN KEY (emp_id) REFERENCES employee(id));	
    

create table meetings(
    meeting_id int NOT NULL auto_increment,
    date_from date NOT NULL,
    date_to date NOT NULL,
    skills varchar(300),
    no_of_panelists int NOT NULL,
    PRIMARY KEY (meeting_id));
    
create table panelist_details(
	id int NOT NULL auto_increment,
    meeting_id int,
    panelist_id int,
    panelist_name text,
    panelist_email varchar(300),
    PRIMARY KEY (id),
    FOREIGN KEY (meeting_id) REFERENCES meetings(meeting_id),
    FOREIGN KEY (panelist_id) REFERENCES employee(id));
    
create table meeting_response(
	response_id int NOT NULL auto_increment,
    meeting_id int,
    panelist_name text,
    panelist_email varchar(200),
	date_from date,
    date_to date,
    response text,
    PRIMARY KEY (response_id),
    FOREIGN KEY (meeting_id) REFERENCES meetings(meeting_id));


--- Script to add dummy data ---

-- cursor = conn.cursor()
-- sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Kelly Smith', 'rambledminddj@gmail.com')
-- cursor.execute(sql)
-- sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Jennifer Warren', 'donajain9@gmail.com')
-- cursor.execute(sql)
-- sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Sam Kent', 'rambledmind8@yahoo.com')
-- cursor.execute(sql)
-- sql = '''insert into employee(name, email_id) values('%s', '%s') ''' % ('Robin Williams', 'donajain@yahoo.com')
-- cursor.execute(sql)



-- sql = '''insert into emp_skills(skills, emp_id) values('%s', '%s') ''' % ('DevOps,AppDev', '2')
-- cursor.execute(sql)
    
