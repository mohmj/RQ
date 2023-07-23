from django.shortcuts import render
from configs import firebase as firebase_config
import datetime, pytz
# Create your views here.
def HomeGet(request): #open home page of the site .
    return render(request,"Customer/home_page.html")

def HomePost(request): #Create new contact order .
    company=request.POST.get("company")
    contactPerson=request.POST.get("contactPerson")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    service=request.POST.get("service")
    type=request.POST.get("type")
    # start_date=request.POST.get("start-date")
    # number_of_days=request.POST.get("number-of-days")
    # goal=request.POST.get("goal")
    order_time=firebase_config.firestore.SERVER_TIMESTAMP
    id=str(company)+" - "+str(datetime.datetime.now(pytz.timezone('Asia/Riyadh')).strftime("%m-%d-%y-%H:%M"))
    firebase_config.firestore_client.collection("orders").document(id).set({
        "id":id,
        "company":company,
        "contactPerson":contactPerson,
        "email":email,
        "phone":phone,
        "service":service,
        "type":type,
        # "start_date":start_date,
        # "numberOfDays":number_of_days,
        # "goal":goal,
        "order_time":order_time
    })
    return render(request, "Customer/order_approve.html" ,{
        'id':id,
    })