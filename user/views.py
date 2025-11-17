from django.shortcuts import render,redirect
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
# Create your views here.
from user.models import user_reg, user_complaints
from django.contrib.auth.models import User
from django.contrib import messages
def user_index(request):

    return render(request,'user/user_index.html')

def user_login(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        pswd = request.POST.get('password')
        try:
            check = user_reg.objects.get(userid=userid, password=pswd)
            request.session['userid'] = check.id
            request.session['username'] = check.userid
            request.session['email'] = check.email
            return redirect('upload_complaints')

        except:
            pass
        return redirect('user_login')
    return render(request,'user/user_login.html')

def user_register(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        user_reg.objects.create(fullname=fullname, email=email, mobile=mobile, gender=gender,location=location)
        return redirect('email_verification')
    return render(request,'user/user_register.html')

def email_verification(request):
    lastdetails = user_reg.objects.all().last()
    email=lastdetails.email
    unid=lastdetails.id
    username1 = "admin"
    sts11 = "send"
    userid1 = User.objects.make_random_password(length=5, allowed_chars="01234567889")
    print(userid1)
    password1 = User.objects.make_random_password(length=5, allowed_chars="ABCDEFGHJIKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz01234567889")
    subject = "Email Verification"
    text_content = ""

    html_content = "<br/><p>Userid:<strong>" + str(userid1) + "<strong></p>""<br/><p>Password:<strong>" + str(password1) + "<strong></p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives(subject, text_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        user_reg.objects.filter(id=unid).update(userid=userid1,password=password1)

    return render(request,'user/email_verification.html')

def upload_complaints(request):
    userid = request.session['userid']
    username = request.session['username']
    email = request.session['email']
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        area_code = request.POST.get('area_code')
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        complaint_type = request.POST.get('complaint_type')
        complaint = request.POST.get('complaint')
        user_complaints.objects.create(userid=userid, username=name,email=email,  address=address,
                                       city=city,area_code=area_code,mobile=mobile,date=date,complaint_type=complaint_type,
                                       complaint=complaint)
        return redirect('upload_complaints')
    return render(request,'user/upload_complaints.html',{'username':username,'email':email})


def change_details(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        pswd = request.POST.get('password')
        try:
            check = user_reg.objects.get(userid=userid, password=pswd)
            request.session['userid'] = check.id

            return redirect('change_details1')

        except:
            pass
        messages.success(request, 'Wrong Details')
        return redirect('change_details')
    return render(request,'user/change_details.html')


def change_details1(request):
    unid=request.session['userid']
    if request.method == "POST":
        userid = request.POST.get('userid')
        pswd = request.POST.get('password')
        user_reg.objects.filter(id=unid).update(userid=userid, password=pswd)
        return redirect('user_login')
    return render(request,'user/change_details1.html')