import pymysql
import boto3

conn = pymysql.connect(
    host = 'awsomescheduler-dbinstance.cozpto0jzcxq.us-east-1.rds.amazonaws.com',
    user = 'admin',
    password = 'password',
    db= 'awsschedulerdb',
)

def lambda_handler(event, context):
    ses = boto3.client('ses')
    
    body = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Homepage</title>
    </head>
    <body>
        <main role="main" class="container">
            <div class="row">
              <div style="width: 100%;">
                <br>
                <h4 style="text-align:center">Thank you for your response.</h4>
    </body>
    </html>'''
    
    
    meeting_id = event['queryStringParameters']['meeting_id']
    name = event['queryStringParameters']['name']
    email = event['queryStringParameters']['email']
    date_from = event['queryStringParameters']['date_from']
    date_to = event['queryStringParameters']['date_to']
    mailResponse = event['queryStringParameters']['mailResponse']
    
    insert_response_details(meeting_id, name, email, date_from, date_to)
    
    def insert_response_details(meeting_id, name, email, date_from, date_to):
        cur = conn.cursor()
        cur.execute("Insert into Details(meeting_id, panelist_name, panelist_email, date_from, date_to, response) values (%s,%s,%r,%s)", (meeting_id, name, email, date_from, date_to, mailResponse))
        conn.commit()
      
    
    ses.send_templated_email(
            Source='donajain@amazon.com',
            Destination={
                'ToAddresses': [
                'donajain@amazon.com',
                ]
            },
            Template='AWSomeSESFinalACKtemplate',
            TemplateData='{"meeting_id": "'+meeting_id+'", "name": "'+name+'", "email": "'+email+'", "mailResponse": "'+mailResponse+'"}'
    
    )
    
    response = {
        'statusCode': 200,
        'headers': {"Content-Type": "text/html",},
        'body': body
    }
    return response