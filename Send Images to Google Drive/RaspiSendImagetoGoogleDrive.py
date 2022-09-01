from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = "client_secret_57119207473-lqv5vk0hpng28tb9f275qfp5v80v97os.apps.googleusercontent.com.json"
API_NAME = "drive"
API_VERSION = "V3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = "106B-H4gSU_LXbpiKiwHJp6Kot1jjOjMx"
file_names = ["foto.jpg"]
mime_types = ["image/jpeg"]

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        "name" : file_name,
        "parents" : [folder_id]
    }
    
    media = MediaFileUpload("/home/pi/Documents/TA/IEEE/RaspiSendImagetoGoogleDrive/FOTO/{0}".format(file_name), mimetype=mime_type)
    
    service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()