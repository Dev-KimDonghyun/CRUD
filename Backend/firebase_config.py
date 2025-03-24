import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/Users/kimdonghyun/Documents/Develop/CRUD/Backend/security/SDK_key.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

collection_name = 'Test_Dummy'
document_id = 'Test01'

# 추가할 데이터를 딕셔너리 형태로 작성합니다.
data = {
    'Name': '김동현',
    'Korean_Age': '20',
    'Age': '18',
    'Location': 'Daegu',
    'Job': 'Student',
}

# 데이터를 컬렉션에 추가합니다.
doc_ref = db.collection(collection_name).document(document_id)
doc_ref.set(data)

print('축하합니다. 데이터가 성공적으로 추가되었습니다.')