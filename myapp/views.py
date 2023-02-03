from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Customer, Models, Bookingdetails, Billing
import pymysql

con = pymysql.connect(host='localhost', user='root', password='Mysql@1234', database='cardealership')
cr = con.cursor()

# Create your views here.
def index(request): 
    return render(request, 'index.html', {})

def models(request): 
    return render(request, 'models.html', {})

def signup(request): 
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retypePassword = request.POST['retypePassword']
        if password == retypePassword: 
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Customer already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('signup')
        else:
            messages.info(request, "Passwords Don't match")
            return redirect('signup')
    else:       
        return render(request, 'signup.html', {})

def login(request): 
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: 
            auth.login(request, user)
            return redirect('index')
        else: 
            messages.info(request, 'Invalid Credentials')
            return redirect('signup')

def logout(request): 
    auth.logout(request)
    return redirect('index')

def myacc(request):
    return render(request, 'myacc.html', {})

# ----------------------------Views for handling adminpg and users table-----------------------------------

def adminpg(request):
    if request.method == 'POST':
        value = request.POST.get('search')
        userFields = ['Id','Username', 'Email', 'Password']
        if value == '':
            userFields = ['Id','Username', 'Email', 'Password']
            users = User.objects.all()
            return render(request, 'adminpg.html', {'userFields':userFields, 'users': users})
        if value.isdigit():
            value = int(value)
            searchResult = User.objects.filter(id=value)
        else:
            searchResult = User.objects.filter(username=value)
        
        if not searchResult:
            messages.info(request, 'No Valid Entry')
        return render(request, 'adminpg.html', {'userFields':userFields, 'users':searchResult})
    else:
        # userFields = User._meta.fields
        # userFields = [field.name.title() for field in User._meta.fields] 
        userFields = ['Id','Username', 'Email', 'Password']
        users = User.objects.all()
        return render(request, 'adminpg.html', {'userFields':userFields, 'users': users})

def addUser(request): 
    if request.method == 'POST': 
         username = request.POST.get('username')
         email = request.POST.get('email')
         password = request.POST.get('password')
         if User.objects.filter(email=email).exists() : 
            messages.info(request, 'Email Already Used')
         elif User.objects.filter(username=username).exists():
            messages.info(request, 'Customer already exists')
         else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
         return redirect('adminpg')
    else: 
        return redirect('adminpg')

def delUser(request): 
    if request.method == 'POST': 
        id = int(request.POST.get('id'))
        user = User.objects.filter(id=id)
        if user.exists(): 
            user.delete()
            messages.info(request, 'User Deleted')
        else:
            messages.info(request, 'Id not found')
    return redirect('adminpg')

# def uptUser(request): 
#     if request.method == 'POST':  
#         id = request.POST.get('id')
#         attr = request.POST.get('update_field')
#         value = request.POST.get('value')
#         if attr == 'Active': 
#             if value == 'True': 
#                 value = 1
#             else:
#                 value = 0 
#         if Customer.objects.filter(id=id).exists():
#             cr.execute(f'''UPDATE  auth_user SET {attr} = '{value}' WHERE id = '{id}' ''')
#             con.commit()
#         else:
#             messages.info(request, 'Customer not found')
#     return redirect('adminpg')


#------------Views for handling customer table in admin page--------------------------

def admincus(request):
    if request.method == 'POST':
        value = request.POST.get('search')
        if value == '':
            return redirect('admincus')

        searchResult = Customer.objects.raw(f'''CALL search_by_cust_id('{value}');''')
        if not searchResult: 
            searchResult = Customer.objects.raw(f'''CALL search_by_name('{value}');''')             
        
        if not searchResult:
            messages.info(request, 'No Valid Entry')
        attr = [f.name.title() for f in Customer._meta.fields]
        return render(request, 'admincus.html', {'cusAttr': attr, 'cusRows':searchResult})
     
    attr = [f.name.title() for f in Customer._meta.fields]
    rows = Customer.objects.raw('''SELECT * FROM customer''')
    return render(request, 'admincus.html', {'cusAttr': attr, 'cusRows': rows})


def addCus(request): 
    if request.method == 'POST':  
        cust_id = request.POST.get('cust_id')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        address = request.POST.get('address')
        occupation = request.POST.get('occupation')
        active = request.POST.get('active')
        if active == 'True' or active == 'Yes': 
            active = 1
        else:
            active = 0 
        if Customer.objects.filter(cust_id=cust_id).exists():
            messages.info(request, 'Customer Exists')
        else:
            cr.execute(f'''INSERT INTO customer VALUES('{cust_id}', 
                                                        '{name.title()}', 
                                                        '{gender}', 
                                                        '{dob}',
                                                        '{email}', 
                                                        '{address}',
                                                        '{occupation}',
                                                        {active} ) ''')
            con.commit()
    return redirect('admincus')

def delCus(request): 
    if request.method == 'POST':  
        cust_id = request.POST.get('cust_id')
        if Customer.objects.filter(cust_id=cust_id).exists():
            cr.execute(f'''DELETE FROM customer WHERE cust_id = '{cust_id}' ''')
            con.commit()
        else:
            messages.info(request, 'Customer not found')
    return redirect('admincus')

def uptCus(request): 
    if request.method == 'POST':  
        cust_id = request.POST.get('cust_id')
        attr = request.POST.get('update_field')
        value = request.POST.get('value')
        if attr == 'Active': 
            if value == 'True': 
                value = 1
            else:
                value = 0 
        if Customer.objects.filter(cust_id=cust_id).exists():
            cr.execute(f'''UPDATE customer SET {attr} = '{value}' WHERE cust_id = '{cust_id}' ''')
            con.commit()
        else:
            messages.info(request, 'Customer not found')
    return redirect('admincus')



#------------Views for handling Car Models in admin page-----------------------------------
def carmodels(request): 
    attr = [f.name.title() for f in Models._meta.fields]
    rows = Models.objects.raw('''SELECT * FROM models''')
    return render(request, 'carmodels.html', {'modelsAttr': attr, 'modelsRows': rows})

def addCarmodels(request): 
    if request.method == 'POST':  
        model = request.POST.get('model_name')
        available = request.POST.get('availability')
        if available == 'True': 
            available = 1; 
        else:
            available = 0; 
        if Models.objects.filter(model_name=model).exists():
            messages.info(request, 'Model Exists')
        else:
            cr.execute(f'''INSERT INTO models VALUES('{model}', {available}) ''')
            con.commit()
    return redirect('carmodels')

def delCarmodels(request): 
    if request.method == 'POST':  
        model = request.POST.get('model_name')
        if Models.objects.filter(model_name=model).exists():
            cr.execute(f'''DELETE FROM models WHERE model_name = '{model}' ''')
            con.commit()
        else:
            messages.info(request, 'Model not found')
    return redirect('carmodels')

def uptCarmodels(request): 
    if request.method == 'POST':  
        model = request.POST.get('model')
        attr = request.POST.get('update_field')
        value = request.POST.get('value')
        if value == 'True': 
            value = 1; 
        else:
            value = 0; 
        if Bookingdetails.objects.filter(model=model).exists():
            cr.execute(f'''UPDATE models SET {attr} = '{value}' WHERE model_name = '{model}' ''')
            con.commit()
        else:
            messages.info(request, 'Model not found')
    return redirect('carmodels')




#-------------Views for handling Booking Details in admin page--------------------------------------
def bookingDetails(request):
    attr = [f.name.title() for f in Bookingdetails._meta.fields]
    rows = Bookingdetails.objects.raw('''SELECT * FROM bookingdetails''')
    return render(request, 'bookingDet.html', {'attrs': attr, 'rows':rows})


def addBookingDet(request): 
    if request.method == 'POST': 
         cust_id = request.POST.get('cust_id')
         booking_id = request.POST.get('booking_id')
         booking_date = request.POST.get('booking_date')
         model = request.POST.get('model')
         reg_no = request.POST.get('reg_no')
         vehicle_id = request.POST.get('vehicle_id')
         vehicle_status = request.POST.get('vehicle_status')
         meter_reading = request.POST.get('meter_reading')
         if Bookingdetails.objects.filter(booking_id=booking_id).exists(): 
            messages.info(request, 'Booking details already updated')
         else:
            cr.execute(f'''INSERT INTO bookingdetails VALUES(
                                            '{cust_id}',
                                            '{booking_id}',
                                            '{booking_date}',
                                            '{model}',
                                            '{reg_no}',
                                            '{vehicle_id}',
                                            '{vehicle_status}',
                                            '{meter_reading}')''')
            con.commit()                                
         return redirect('bookingDetails')
    else: 
        return redirect('bookingDetails')

def delBookingDet(request): 
    if request.method == 'POST':  
        cust_id = request.POST.get('cust_id')
        booking_id = request.POST.get('booking_id')
        bookingDetails = Bookingdetails.objects.filter(cust_id=cust_id, booking_id=booking_id)
        if  bookingDetails.exists(): 
            bookingDetails.delete()
            messages.info(request, 'Booking details Deleted')
        else:
            messages.info(request, 'Details not found')
    return redirect('bookingDetails')

def uptBookingDet(request): 
    if request.method == 'POST':  
        cust_id = request.POST.get('cust_id')
        booking_id = request.POST.get('booking_id')
        attr = request.POST.get('update_field')
        value = request.POST.get('value')
        if Bookingdetails.objects.filter(cust_id=cust_id, booking_id=booking_id).exists():
            cr.execute(f'''UPDATE bookingdetails SET {attr} = '{value}' WHERE booking_id = '{booking_id}' ''')
            con.commit()
        else:
            messages.info(request, 'Booking Details not found')
    return redirect('bookingDetails')


#--------------------------Views for handling Billing Details in admin page---------------------
def billing(request): 
    attr = [f.name.title() for f in Billing._meta.fields]
    rows = Billing.objects.raw('''SELECT * FROM billing''')
    return render(request, 'billing.html', {'attrs': attr, 'rows':rows})

def addBill(request): 
    if request.method == 'POST': 
        bill_id = request.POST.get('bill_id')
        booking_id = request.POST.get('booking_id')
        billing_date = request.POST.get('billing_date')
        bill_type = request.POST.get('bill_type')
        bill_amount = request.POST.get('bill_amount')
        amt_paid = request.POST.get('amt_paid')
        if Billing.objects.filter(bill_id=bill_id).exists(): 
            messages.info(request, 'Bill already exists')
        else: 
            bill_id = bill_id.upper()
            booking_id = booking_id.upper()
            bill_type = bill_type.title()
            cr.execute(f'''INSERT INTO billing(bill_id, 
                                            booking_id, date, 
                                            bill_type, 
                                            bill_amount, 
                                            amount_paid)
                                            VALUE('{bill_id}', 
                                                  '{booking_id}', 
                                                  '{billing_date}',
                                                  '{bill_type}',
                                                  {bill_amount},  
                                                  {amt_paid});''')
            con.commit()
        return redirect('billing')
    else: 
        return redirect('billing')
        
def delBill(request): 
    if request.method == 'POST':  
        bill_id = request.POST.get('bill_id')
        booking_id = request.POST.get('booking_id')
        billDetails = Billing.objects.filter(bill_id=bill_id, booking_id = booking_id)
        if billDetails.exists(): 
            billDetails.delete()
            messages.info(request, 'Bill Deleted')
        else:
            messages.info(request, 'Bill not found')
    return redirect('billing')

def uptBill(request): 
    if request.method == 'POST':  
        bill_id = request.POST.get('bill_id')
        booking_id = request.POST.get('booking_id')
        attr = request.POST.get('update_field')
        value = request.POST.get('value')
        value.title()
        print(value)
        if Billing.objects.filter(bill_id = bill_id).exists():
            cr.execute(f'''UPDATE billing SET {attr} = '{value}' WHERE bill_id = '{bill_id}' AND booking_id = '{booking_id}' ''')
            con.commit()
        else:
            messages.info(request, 'Bill not found')
    return redirect('billing')

#--------------------------View for rendering cars on click in models page----------------------
def carpg(request): 
    return render(request, 'car.html', {})