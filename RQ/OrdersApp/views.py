from django.shortcuts import render
from configs import firebase as firebase_config
import datetime, pytz
# Create your views here.
def HomeGet(request): #open home page of orders app .
    ordersList=[]
    docs = firebase_config.firestore_client.collection('orders').order_by("order_time",direction=firebase_config.firestore.Query.DESCENDING).stream()
    for doc in docs:
        orderDict=doc.to_dict()
        orderDict['order_time']=datetime.datetime.fromtimestamp(orderDict['order_time'].timestamp(),pytz.timezone('Asia/Riyadh')).strftime("%m-%d-%y %H:%M")
        ordersList.append(orderDict)
    return render(request,"Orders/index.html",{"ordersList":ordersList})
