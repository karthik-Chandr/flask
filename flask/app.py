from pipes import Template
from flask import Flask, render_template, redirect, session, request, url_for
from forms import InfoForm
import rdb_connectfile as db
from flask import Response,send_file
from collections import Counter
import boto3
import ses_connector

app = Flask(__name__)
app.config['SECRET_KEY'] = '324a4f656976bdf81685d98c2b0c2bee'
ses = boto3.client('ses')
email_from = 'donajain@amazon.com'

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/insert',methods=['POST'])
def insert():
    if request.method == 'POST':
        date_from = request.form['startdate']
        print(date_from)
        date_to = request.form['enddate']
        print(date_to)
        skills = request.form.getlist('skills')
        print(skills)
        no_of_panelists = request.form['no_of_panelists']
        print(no_of_panelists)
        db.insert_meeting_details(date_from, date_to, skills, no_of_panelists)
        meeting_details = db.get_meeting_details()
        selected_panelists = get_panelists_details(skills, no_of_panelists)
        db.insertPanelistDetails(selected_panelists)
        session['selected_panelists'] = selected_panelists
        session['startdate'] = date_from
        session['enddate'] = date_to
        return render_template('insert.html',selected_panelists=selected_panelists)

def get_panelists_details(skills, no_of_panelists):
    emp_id_list = db.get_emp_id(skills)
    count = Counter(emp_id_list)
    dic_count = dict(count)
    print(dic_count)
    print(list(dic_count.keys()))
    emp_list_ascend = list(dic_count.keys())
    required_emp_detail = db.req_emp_details(no_of_panelists, emp_list_ascend)
    return required_emp_detail

@app.route('/sent',methods=['POST'])
def sent():
    if request.method == 'POST':
        selected_panelists = session['selected_panelists']
        print("selected_panelists val in sent tag: ",selected_panelists)         #Remove after testing
        date_from = session['startdate']
        print("date_from: ",date_from)                                      #Remove after testing
        date_to = session['enddate']
        print("date_to1",date_to)                                    #Remove after testing
        ses_connector.sentMailToRecepients(selected_panelists, date_from, date_to)
        session.pop('selected_panelists', None)
        return redirect(url_for('index'))

@app.route('/modify',methods=['GET', 'POST'])
def modify():
    data = db.getRecordDetails()
    print(data)
    if request.method == 'POST':
        response_id = request.form['response_id']
        meeting_id = request.form['meeting_id']
        panelist_name = request.form['panelist_name']
        panelist_email = request.form['panelist_email']
        print(response_id)
        print(meeting_id)
        print(panelist_name)
        print(panelist_email)
        replaced_data = db.get_replaced_panelist(meeting_id)
        print("data: ", replaced_data)
        session['replaced_data'] = replaced_data
        return render_template('replace.html', replaced_data=replaced_data)
    return render_template('modify.html', data=data)

@app.route('/update',methods=['POST','GET'])
def update():
        response_id = request.form['response_id']
        meeting_id = request.form['meeting_id']
        panelist_name = request.form['panelist_name']
        panelist_email = request.form['panelist_email']
        print(response_id)
        print(meeting_id)
        print(panelist_name)
        print(panelist_email)
        # code to get a single panelist other than the one who is been selected before
        replaced_data = db.get_replaced_panelist(meeting_id)
        print("data: ", replaced_data)
        session['replaced_data'] = replaced_data
        session['meeting_id_old'] = meeting_id
        session['panelist_name_old'] = panelist_name
        session['panelist_email_old'] = panelist_email
        return render_template('replace.html', replaced_data=replaced_data)

@app.route('/sentreplacedemail',methods=['POST'])
def sentreplacedemail():
    if request.method == 'POST':
        replaced_data = session['replaced_data']
        meeting_id = session['meeting_id_old']
        panelist_name = session['panelist_name_old']
        panelist_email = session['panelist_email_old']
        print("replaced_data val in sent tag: ",replaced_data)         #Remove after testing
        # remove old value from panelist_details & meeting_response
        db.replaceOldValues(meeting_id, panelist_name, replaced_data)
        dates = db.getDatesFromDB(meeting_id)
        ses_connector.sentMailToReplacedRecepients(replaced_data, dates[0][0], dates[0][1], meeting_id)
        # session.pop('selected_panelists', None)
        return redirect(url_for('index'))

@app.route('/about',methods=['GET', 'POST'])
def about():    
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080)
