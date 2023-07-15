import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred,{
    "databaseURL":"https://playground-fdda0-default-rtdb.firebaseio.com"
})

with open('db.json', 'w', encoding='utf-8') as f:
    json.dump(db.reference().get(), f, ensure_ascii=False, indent=4)
