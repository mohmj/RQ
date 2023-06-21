import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("configs/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
firestore_client = firestore.client()
from google.cloud.firestore_v1 import Increment