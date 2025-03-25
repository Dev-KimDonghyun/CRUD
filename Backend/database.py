import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import fastapi
from fastapi import FastAPI

app = FastAPI()

cred = credentials.Certificate('/Users/kimdonghyun/Documents/Develop/CRUD/Backend/security/SDK_Key.json')  
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.get('/')
async def main():
    return {'messgae': 'Hello World'}

@app.get('/dataget')
async def data():
    get_test_data_01 = db.collection('Test_Dummy')
    data_01 = get_test_data_01.get()
    res = []
    for result in data_01:
        res.append(result.to_dict())
    return res