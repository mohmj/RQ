from django.shortcuts import render
from configs import firebase as firebase_config
import datetime, pytz, pandas as pd, io
from django.http import HttpResponse

# Create your views here.

# Get orders data from firebase
def get_data_from_firebse():
    ordersList=[]
    docs = firebase_config.firestore_client.collection('orders').order_by("order_time",direction=firebase_config.firestore.Query.DESCENDING).stream()
    for doc in docs:
        orderDict=doc.to_dict()
        orderDict['order_time']=datetime.datetime.fromtimestamp(orderDict['order_time'].timestamp(),pytz.timezone('Asia/Riyadh')).strftime("%m-%d-%y %H:%M")
        ordersList.append(orderDict) 

    return ordersList

def HomeGet(request): #open home page of orders app .
    ordersList=get_data_from_firebse()
    return render(request,"Orders/index.html",{"ordersList":ordersList})


def ordersDownload(request):
    
    ordersList=get_data_from_firebse()
    df=pd.DataFrame(ordersList)
    
    buffer=io.StringIO()
    df.to_csv(buffer,index=False)
    
    response = HttpResponse(buffer.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=orders.csv'

    return response