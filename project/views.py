from django.shortcuts import render, redirect
from .models import register,service,admin
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout  


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        name = request.POST.get('name')  
        password1 = request.POST.get('password1')  
        password2 = request.POST.get('password2')  
        #user_type = request.POST.get('user_type')  
        cw=request.POST.get('cw')
        aadhar = request.POST.get('aadhar')  
        email = request.POST.get('email')  
        phone = request.POST.get('phone')  
        gender = request.POST.get('gender')  
        dob = request.POST.get('dob')  
        address=request.POST.get('address')
        pin=request.POST.get('pin')
        image = request.FILES.get('profimage')  

        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match !'})

        if len(phone) != 10 or not phone.isdigit():
            return render(request, 'register.html', {'error': 'Invalid phone number'})

        if len(aadhar) != 12 or not aadhar.isdigit():
            return render(request, 'register.html', {'error': 'Invalid aadhar number'})

        new_register = register(username=username, password=password1, name=name, op="service_provider",cw=cw,aadhar=aadhar, email=email, phone=phone, gender=gender,dob=dob,address=address,pin=pin,profimage=image)
        new_register.save()

        return redirect('login')  
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = register.objects.get(username=username)
            if user.password == password:
                request.session["uname"]=username
                return redirect('loginhome')
            else:
                return render(request, 'login.html', {'error_user': 'Wrong password'})
        except register.DoesNotExist:
            return render(request, 'login.html', {'error_user': 'User does not exist. Please register.'})
    else:
        return render(request, 'login.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('adminUsername')
        password = request.POST.get('adminPassword')

        try:
            user = admin.objects.get(username=username)
            if user.password == password:
                request.session["admin"] = username
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error_admin': 'Wrong password', 'admin_form_submitted': True})
        except admin.DoesNotExist:
            return render(request, 'login.html', {'error_admin': 'Admin does not exist.', 'admin_form_submitted': True})
    else:
        return render(request, 'login.html', {'admin_form_submitted': True})

def home(request):
    return render(request, 'home.html')

def loginhome(request):
    return render(request, 'loginhome.html')

def profile1(request):
    uname = request.session.get("uname")
    if uname:
        try:
            user = register.objects.get(username=uname)  
            return render(request, 'profile1.html', {"info": user})
        except register.DoesNotExist:
            pass  
    return render(request, 'profile1.html', {"error": "User not found"})

def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        cw = request.POST.get('cw').strip()  
        password1 = request.POST.get('password1')  
        password2 = request.POST.get('password2')

        try:
            user = register.objects.get(username=username)
            
            if user.cw.strip() != cw:
                return render(request, 'forgotpassword.html', {'error': 'Wrong code word'})
            else:
                if password1 != password2:
                    return render(request, 'forgotpassword.html', {'error': 'Passwords do not match'})
                else:
                    user.password = password1
                    user.save()
                    return render(request, 'login.html', {'success': 'Password updated successfully. You can now login with your new password.'})
            
        except register.DoesNotExist:
            return render(request, 'forgotpassword.html', {'error': 'User does not exist. Please register.'})
    else:
        return render(request, 'forgotpassword.html')

def provideservice(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        service_type = request.POST.get('service_type')
        description = request.POST.get('description')
        image = request.FILES.get('image')  
        form = request.POST.get('form')

        user = request.session.get("uname")
        
        if register.objects.filter(username=username, op='service_provider').exists():
            if image:
                service.objects.create(username=username, name=name, uservice=service_type, description=description, image=image,form=form)
                return render(request, 'provideservice.html', {"msg": "Service added successfully."})
            else:
                return render(request, 'provideservice.html', {"error": "Please select an image."})
        else:
            return render(request, 'provideservice.html', {"error": "You are not registered as a service provider."})
    else:
        return render(request, 'provideservice.html')

def familycare(request):
    services = service.objects.filter(uservice="family care")
    return render(request, 'familycare.html', {'services': services})

def loginfc(request):
    services = service.objects.filter(uservice="family care")
    return render(request, 'loginfc.html', {'services': services})

def myservices(request):
    uname = request.session.get("uname")
    services = service.objects.filter(username=uname)
    return render(request, 'myservices.html', {'services': services})

def beautyandhealth(request):
    services = service.objects.filter(uservice="beauty and health")
    return render(request, 'beautyandhealth.html', {'services': services}) 

def loginbah(request):
    services = service.objects.filter(uservice="beauty and health")
    return render(request, 'loginbah.html', {'services': services}) 

def academic(request):
    services = service.objects.filter(uservice="academic")
    return render(request, 'academic.html', {'services': services})   

def loginacad(request):
    services = service.objects.filter(uservice="academic")
    return render(request, 'loginacad.html', {'services': services})   

def logint(request):
    services = service.objects.filter(uservice="transportation")
    return render(request, 'logint.html', {'services': services})   

def househelp(request):
    services = service.objects.filter(uservice="house help")
    return render(request, 'househelp.html', {'services': services})  

def loginhh(request):
    services = service.objects.filter(uservice="house help")
    return render(request, 'loginhh.html', {'services': services})  

def technical(request):
    services = service.objects.filter(uservice="technical")
    return render(request, 'technical.html', {'services': services})  

def logintech(request):
    services = service.objects.filter(uservice="technical")
    return render(request, 'logintech.html', {'services': services})  

def transportation(request):
    services = service.objects.filter(uservice="transportation")
    return render(request, 'transportation.html', {'services': services})   

@csrf_protect
def changepreference(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        preference = request.POST.get('preference')

        try:
            user = register.objects.get(username=username)

            if user.password == password:
                if preference:
                    user.op = 'service_provider'
                    user.save()
                    return render(request, 'provideservice.html')  # Render success page or redirect as needed
                else:
                    return render(request, 'changepreference.html', {'message': 'Please check the preference box.'})
            else:
                return render(request, 'changepreference.html', {'message': 'Invalid password.'})
        except register.DoesNotExist:
            return render(request, 'changepreference.html', {'message': 'User does not exist.'})
    else:
        return render(request, 'changepreference.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def loginaboutus(request):
    return render(request, 'loginaboutus.html')

def delete_account(request):
    if request.method == 'POST':
        uname = request.session.get("uname")
        if uname:
            try:
                user = register.objects.get(username=uname)
                user.delete()
                service.objects.filter(username=uname).delete()
                del request.session["uname"]
                return redirect('login')
            except register.DoesNotExist:
                pass
    return redirect('home')

def logout_user(request):
    logout(request)  
    return redirect('home')  

def dashboard(request):
    users= register.objects.all()[:3]
    services = service.objects.all()[:3]
    return render(request,"dashboard.html",{'users':users,'services': services})

def userinfo(request):
    users = register.objects.all()
    return render(request, 'users.html', {'users': users})

from django.db.models import Count
from django.http import JsonResponse
from .models import register

def genderratio(request):
    # Fetch gender data from the register table
    gender_data = register.objects.values('gender').annotate(count=Count('gender'))

    # Calculate female to male ratio
    female_count = 0
    male_count = 0
    for entry in gender_data:
        if entry['gender'] == 'Female':
            female_count += entry['count']
        elif entry['gender'] == 'Male':
            male_count += entry['count']

    # Create data for the pie chart
    data = {
        'female': female_count,
        'male': male_count
    }

    return JsonResponse(data)

def usercount(request):
    # Count the total number of registered users
    user_count = register.objects.count()

    # Return the user count as JSON response
    return JsonResponse({'count': user_count})

def servicecount(request):
    # Count the total number of registered users
    service_count = service.objects.count()

    # Return the user count as JSON response
    return JsonResponse({'count': service_count})

def reviewservices(request):
    services = service.objects.all()
    return render(request, 'reviewservices.html', {'services': services})   

def addadmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')  

        try:
            if admin.objects.filter(username=username).exists():
                return render(request, 'addadmin.html', {'msg': 'Username already exists!'})

            new_admin = admin(username=username, password=password)
            new_admin.save()
            return render(request, 'addadmin.html', {'msg': 'Admin added successfully'})
        except Exception as e:
            return render(request, 'addadmin.html', {'msg': 'An error occurred while adding the admin: {}'.format(str(e))})

    return render(request, 'addadmin.html')

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import service

def delete_service(request, service_id):
    if request.method == 'POST' and request.is_ajax():
        service = get_object_or_404(service, id=service_id)
        if service.username == request.user.username:  # Assuming username is the user's identifier
            service.delete()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
