from django.shortcuts import render,redirect
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
# Create your views here.
from django.contrib.auth.models import User
from higher_officer.models import station_details
from police.models import criminal_details


def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        if uname == 'admin' and password == 'admin':
            return redirect("admin_home")
    return render(request,'higher_officer/admin_login.html')

def admin_home(request):
    if request.method == "POST":
        police_name = request.POST.get('police_name')
        gender = request.POST.get('gender')
        station_name = request.POST.get('station_name')
        area_code = request.POST.get('area_code')
        location = request.POST.get('location')
        email = request.POST.get('email')
        area_name = request.POST.get('area_name')
        station_details.objects.create(police_name=police_name,gender=gender,station_name=station_name, area_code=area_code, location=location,
                                       email=email,area_name=area_name)
        return redirect('police_emailverify')
    return render(request,'higher_officer/admin_home.html')

def police_emailverify(request):
    lastdetails = station_details.objects.all().last()
    email=lastdetails.email
    unid=lastdetails.id
    username1 = "admin"
    sts11 = "send"
    userid1 = User.objects.make_random_password(length=5, allowed_chars="01234567889")
    print(userid1)
    password1 = User.objects.make_random_password(length=5, allowed_chars="ABCDEFGHJIKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz01234567889")
    subject = "Police Email Verification"
    text_content = ""

    html_content = "<br/><p>Userid:<strong>" + str(userid1) + "<strong></p>""<br/><p>Password:<strong>" + str(password1) + "<strong></p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        station_details.objects.filter(id=unid).update(userid=userid1,password=password1)

    return render(request,'higher_officer/police_emailverify.html')


def adminview_crime(request):

    crime_det=criminal_details.objects.all()
    return render(request,'higher_officer/adminview_crime.html',{'crime_det':crime_det})