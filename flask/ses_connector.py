import boto3
import rdb_connectfile as db

ses = boto3.client('ses')

def sentMailToRecepients(selected_panelists, date_from, date_to):
    meeting_id = db.get_meeting_id()

    for i in selected_panelists:
        ses.send_templated_email(
            Source='rambledminddj@gmail.com',
            Destination={
                'ToAddresses': [
                str(i[2]),
                ]
            },
            Template='AWSomeSESPanelRequestTemplate',
            TemplateData='{"name": "'+str(i[1])+'", "date_from":  "'+str(date_from)+'", "date_to":  "'+str(date_to)+'", "meeting_id": "'+meeting_id+'", "email_id": "'+str(i[2])+'"}'
            )


def sentMailToReplacedRecepients(replaced_data, date_from, date_to, meeting_id):
    ses.send_templated_email(
            Source='rambledminddj@gmail.com',
            Destination={
                'ToAddresses': [
                str(replaced_data[0][2]),
                ]
            },
            Template='AWSomeSESPanelRequestTemplate',
            TemplateData='{"name": "'+str(replaced_data[0][1])+'", "date_from":  "'+str(date_from)+'", "date_to":  "'+str(date_to)+'", "meeting_id": "'+str(meeting_id)+'", "email_id": "'+str(replaced_data[0][2])+'"}'
            )

