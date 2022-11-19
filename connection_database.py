#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import storage
import pyrebase
import requests


config = {
    "apiKey": "AIzaSyDqu8MFLwT_8w8519gtrrUmkxTIIMVAYJQ",
    "authDomain": "codejam-bbc52.firebaseapp.com",
    "storageBucket": "codejam-bbc52.appspot.com",
    "databaseURL": "https://codejam-bbc52-default-rtdb.firebaseio.com/",
    "serviceAccount": "codejam-bbc52-firebase-adminsdk-uu7pl-a2ef151695.json"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()

def getUsers(company_name: str):
    all_users = db.child("companies").child(company_name).get()

    for user in all_users.each():
        print(user.key())
        print(user.val())
        downloadStorageImage(company_name, user.key())

    return all_users

    

def downloadStorageImage(company_name: str, user_id):
    file_name = f"{user_id}.jpg"
    path = f"{company_name}/{file_name}"
    url = storage.child(path).get_url(None)

    r = requests.get(url, allow_redirects=True)
    open(f"known/{file_name}", 'wb').write(r.content)

getUsers("company1")

"""
cred = credentials.Certificate("./codejam-bbc52-52bf4477aac5.json")
app = firebase_admin.initialize_app(cred, {'storageBucket': 'codejam-bbc52.appspot.com'}) # connecting to firebase
"""


"""
storage.Client(credentials=cred).bucket(firebase_admin.storage.bucket().name).blob('company1/sample_text_file.txt').download_to_filename('downloaded_file.txt')

all_files = storage.child("company1/whitelist").list_files() #Enter the name of the folder 

files = storage.Client(credentials=cred).list_blobs(firebase_admin.storage.bucket().name)
for file in files:
    try:
        print(file)
    except:
        print("Erreur lors du téléchargement.")
"""

"""
file_path = "IMG_5077_2.jpg"
bucket = storage.bucket() # storage bucket
blob = bucket.blob(file_path)
blob.upload_from_filename(file_path)
"""

"""
bucket = storage.bucket(app=app)


def getWhiteList(company_name):

    for file in bucket.list_blobs():
        print(str(file.name))
        destination_file_name = f'images/whitelist/{str(file.name)}.jpg'
        source_blob_name = str(file.name)
        blob = bucket.blob(f"{source_blob_name}")
        blob.download_to_filename(destination_file_name)

getWhiteList('company1')
"""