import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate(
    "/work-record-manager/workrecordsmanager-fa5c8-firebase-adminsdk-aifxp-f060e8dee8.json")
firebase_admin.initialize_app(cred)


def sendPush(title, msg, registration_token,dataObject):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg,
        ),
    data = dataObject,
    tokens = registration_token
    )
    
    response = messaging.send.multicast(message)

    