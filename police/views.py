from django.shortcuts import render,redirect
from django.db.models import Count
# Create your views here.
from higher_officer.models import station_details
from django.contrib import messages
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
# Create your views here.
from django.contrib.auth.models import User

from police.models import criminal_details
from user.models import user_complaints


def police_login(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        pswd = request.POST.get('password')
        try:
            check = station_details.objects.get(userid=userid, password=pswd)
            request.session['userid'] = check.id
            request.session['username'] = check.userid
            request.session['email'] = check.email
            request.session['area_code'] = check.area_code
            request.session['station_name'] = check.station_name
            return redirect('police_home')

        except:
            pass
        return redirect('police_login')
    return render(request,'police/police_login.html')


def police_home(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        pswd = request.POST.get('password')
        try:
            check = station_details.objects.get(userid=userid, password=pswd)
            request.session['userid'] = check.id

            return redirect('update_details')

        except:
            pass
        messages.success(request, 'Wrong Details')
        return redirect('police_home')
    return render(request,'police/police_home.html')

def update_details(request):
    unid=request.session['userid']
    if request.method == "POST":
        userid = request.POST.get('userid')
        pswd = request.POST.get('password')
        station_details.objects.filter(id=unid).update(userid=userid, password=pswd)
        return redirect('police_login')
    return render(request,'police/update_details.html')


def view_complaints(request):
    userid = request.session['userid']
    username = request.session['username']
    email = request.session['email']
    area_code = request.session['area_code']
    complaint_det=user_complaints.objects.filter(area_code=area_code)
    return render(request,'police/view_complaints.html',{'complaint_det':complaint_det})

def update_casestatus(request,pk):
    undata=user_complaints.objects.get(id=pk)
    unid=undata.id
    email=undata.email
    if request.method == "POST":
        case_status = request.POST.get('case_status')

        username1 = "admin"
        sts11 = "send"
        subject = "Complaint Status"
        text_content = ""

        html_content = case_status
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [email]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        if msg.send():
            user_complaints.objects.filter(id=unid).update(complaint_status=case_status)
            messages.success(request, 'Case Status Successfully Send To Email')
    return render(request,'police/update_casestatus.html')


def arrest_criminal(request,pk):
    unres=user_complaints.objects.get(id=pk)
    ctype=unres.complaint_type
    station_name=request.session['station_name']
    area_code=request.session['area_code']
    if request.method == "POST" and request.FILES['criminal_image']:
        station_name = request.POST.get('station_name')
        arae_code = request.POST.get('arae_code')
        city = request.POST.get('city')
        criminal_name = request.POST.get('criminal_name')
        mobile = request.POST.get('mobile')
        complaint_type = request.POST.get('complaint_type')
        acts = request.POST.get('acts')
        sessions = request.POST.get('sessions')
        year = request.POST.get('year')
        status = request.POST.get('status')
        criminal_image = request.FILES['criminal_image']
        criminal_details.objects.create(station_name=station_name,arae_code=arae_code,city=city,criminal_name=criminal_name,
                                        mobile=mobile,complaint_type=complaint_type,acts=acts,sessions=sessions,year=year,
                                        status=status,criminal_image=criminal_image)
    return render(request,'police/arrest_criminal.html',{'sname':station_name,'area_code':area_code,'ctype':ctype})


def upload_criminals(request):
    station_name=request.session['station_name']
    area_code=request.session['area_code']
    if request.method == "POST" and request.FILES['criminal_image']:
        station_name = request.POST.get('station_name')
        arae_code = request.POST.get('arae_code')
        city = request.POST.get('city')
        criminal_name = request.POST.get('criminal_name')
        mobile = request.POST.get('mobile')
        complaint_type = request.POST.get('complaint_type')
        acts = request.POST.get('acts')
        sessions = request.POST.get('sessions')
        year = request.POST.get('year')
        status = request.POST.get('status')
        criminal_image = request.FILES['criminal_image']
        criminal_details.objects.create(station_name=station_name,arae_code=arae_code,city=city,criminal_name=criminal_name,
                                        mobile=mobile,complaint_type=complaint_type,acts=acts,sessions=sessions,year=year,
                                        status=status,criminal_image=criminal_image)
    return render(request,'police/upload_criminals.html',{'sname':station_name,'area_code':area_code})



def crime_analysis(request):
    crimedet=''
    if request.method == "POST":
        year = request.POST.get('year')
        crimedet=criminal_details.objects.filter(year=year)
    return render(request,'police/crime_analysis.html',{'crimedet':crimedet})

def crime_chart(request):
    chart = criminal_details.objects.values('year').annotate(dcount=Count('year'))

    return render(request,'police/crime_chart.html',{'objects':chart})