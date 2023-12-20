from django.shortcuts import render
from django.http import HttpResponse 
import firebase_admin
from firebase_admin import credentials, db
from django.shortcuts import render, redirect
from django.contrib import messages
if not firebase_admin._apps:
    cred = credentials.Certificate("GDsteel/credentials.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://gd-steel-s-inventory-default-rtdb.firebaseio.com'
    })

app = firebase_admin.get_app()
ref = db.reference(app=app)

def home(request):
    messages.success(request, 'This is a popup message.')
    return render(request, 'gds/update_sp.html')    
  
def Add(request):
    if request.method =='POST':
        data = request.POST
        new_entry = {
            'Item_name': data.get('Item_name'),
            'quantity': data.get('quantity'),
            'Date': data.get('entry_date'),
            'StockPile': data.get('stock_pile')
        }
        ref.push(new_entry)
        
        
    d =ref.get()
    context={'d' :d}
    return render(request, 'gds/home.html',context)



def Edit(request, key):
    if request.method == 'POST':
        data = request.POST
        ref = db.reference(key)  #object return kregaaa
        
        entry = ref.get()  # Retrieve the current entry
        
        updated_entry = {}
        
        # Check each field for updates and populate the updated_entry dictionary
        if data.get('Item_name'):
            updated_entry['Item_name'] = data.get('Item_name')
        else:
            updated_entry['Item_name'] = entry.get('Item_name')
        
        if data.get('quantity'):
            updated_entry['quantity'] = data.get('quantity')
        else:
            updated_entry['quantity'] = entry.get('quantity')
        
        if data.get('entry_date'):
            updated_entry['Date'] = data.get('entry_date')
        else:
            updated_entry['Date'] = entry.get('Date')
        
        if data.get('stock_pile'):
            updated_entry['StockPile'] = data.get('stock_pile')
        else:
            updated_entry['StockPile'] = entry.get('StockPile')
        
        ref.update(updated_entry)  # Update the entry at the specified key
        return redirect('/')  # Redirect to some URL after the update
        
    return render(request, 'gds/edit.html')


def Delete(request,key):
    ref = db.reference(key)
    ref.delete() 
    return redirect('/')

def Update_stock(request,key):
    if request.method == 'POST':
        data = request.POST
        a=data.get('quantity')

        current_stockpile = db.reference(key).child('StockPile').get()
        if current_stockpile is not None:
    # Convert 'a' and current stockpile to integers, add them, and convert back to string
            updated_stockpile = str(int(current_stockpile) + int(a))

    # Update the 'StockPile' attribute with the new value
        db.reference(key).child('StockPile').set(updated_stockpile)
        
        return redirect('/')  
        
    return render(request, 'gds/update_sp.html')
    


    












# Create your views here.
# config = {
#   "apiKey": "AIzaSyCZoAhpB0VOxU-LarBVpC1xY4onURns4bw",
#   "authDomain": "gd-steel-s-inventory.firebaseapp.com",
#   "databaseURL": "https://gd-steel-s-inventory-default-rtdb.firebaseio.com",
#   "projectId": "gd-steel-s-inventory",
#   "storageBucket": "gd-steel-s-inventory.appspot.com",
#   "messagingSenderId": "778792335168",
#   "appId": "1:778792335168:web:e0565cd487dd9e08b92ca5",
#   "measurementId": "G-NCGYMS92M0"
# };


#here we are doing firebase authentication
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()