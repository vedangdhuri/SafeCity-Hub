from django.shortcuts import render,redirect
# Create your views here.
from user.models import user_reg, user_complaints
from django.contrib import messages
from django.db.models import Q
import random
from django.core.mail import send_mail
from django.conf import settings
def user_index(request):
    return render(request,'user/user_index.html')

def user_login(request):
    if request.method == "POST":
        login_id = request.POST.get('userid')
        pswd = request.POST.get('password')
        try:
            check = user_reg.objects.get(Q(userid=login_id) | Q(email=login_id), password=pswd)
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
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        
        # Check if email or userid already exists to prevent duplicate OTP confusion
        if user_reg.objects.filter(Q(userid=userid) | Q(email=email)).exists():
            messages.error(request, 'User ID or Email already exists.')
            return redirect('user_register')
            
        # Generate OTP
        otp = str(random.randint(100000, 999999))
        
        # Temporarily store user data and OTP in session
        request.session['reg_data'] = {
            'fullname': fullname, 'email': email, 'mobile': mobile,
            'gender': gender, 'location': location, 'userid': userid, 'password': password
        }
        request.session['reg_otp'] = otp
        
        # Send Email
        subject = 'Email Verification OTP - Crime Hub'
        message = f'Your One Time Password (OTP) for registering on Crime Hub is: {otp}'
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        
        try:
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, f'OTP sent successfully to {email}')
            return redirect('register_otp_verify')
        except Exception as e:
            messages.error(request, 'Error sending verification email.')
            return redirect('user_register')
            
    return render(request,'user/user_register.html')

def register_otp_verify(request):
    if 'reg_data' not in request.session:
        messages.error(request, 'Session expired. Please register again.')
        return redirect('user_register')
        
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('reg_otp')
        
        if entered_otp == saved_otp:
            # OTP Verified, save the user
            data = request.session['reg_data']
            user_reg.objects.create(
                fullname=data['fullname'], email=data['email'], mobile=data['mobile'], 
                gender=data['gender'], location=data['location'], userid=data['userid'], password=data['password']
            )
            
            # Clean up
            del request.session['reg_data']
            del request.session['reg_otp']
            
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('user_login')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('register_otp_verify')
            
    return render(request, 'user/register_otp_verify.html')

def forgot_password(request):
    if request.method == "POST":
        login_id = request.POST.get('userid')
        
        try:
            user = user_reg.objects.get(Q(userid=login_id) | Q(email=login_id))
            
            # Generate 6 digit OTP
            otp = str(random.randint(100000, 999999))
            
            # Store in session
            request.session['reset_userid'] = user.id
            request.session['reset_otp'] = otp
            
            # Send Email
            subject = 'Password Reset OTP - Crime Hub'
            message = f'Your One Time Password (OTP) for resetting your Crime Hub password is: {otp}'
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            
            try:
                send_mail(subject, message, email_from, recipient_list)
                messages.success(request, f'OTP sent successfully to {user.email}')
                return redirect('otp_verify')
            except Exception as e:
                messages.error(request, 'Error sending email. Please check your connection or system settings.')
                return redirect('forgot_password')
                
        except user_reg.DoesNotExist:
            messages.error(request, 'No user found with the provided User ID or Email.')
            return redirect('forgot_password')
            
    return render(request, 'user/forgot_password.html')

def otp_verify(request):
    if 'reset_userid' not in request.session:
        messages.error(request, 'Session expired or invalid reset request.')
        return redirect('forgot_password')
        
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        saved_otp = request.session.get('reset_otp')
        
        if entered_otp == saved_otp:
            # OTP Verified, send to change password logic
            messages.success(request, 'OTP Verified! Please enter your new password.')
            return redirect('reset_new_password')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('otp_verify')
            
    return render(request, 'user/otp_verify.html')

def reset_new_password(request):
    if 'reset_userid' not in request.session:
        return redirect('forgot_password')
        
    if request.method == "POST":
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password != cpassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('reset_new_password')
            
        unid = request.session.get('reset_userid')
        user_reg.objects.filter(id=unid).update(password=password)
        
        # Clean up session
        del request.session['reset_userid']
        del request.session['reset_otp']
        
        messages.success(request, 'Password reset successfully. You can now log in.')
        return redirect('user_login')
        
    return render(request, 'user/reset_new_password.html')



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
        
        # Check if it was a custom category provided
        complaint_type = request.POST.get('complaint_type')
        if complaint_type == 'Other':
            complaint_type = request.POST.get('custom_complaint_type')
            
        complaint = request.POST.get('complaint')
        user_complaints.objects.create(userid=userid, username=name,email=email,  address=address,
                                       city=city,area_code=area_code,mobile=mobile,date=date,complaint_type=complaint_type,
                                       complaint=complaint)
        return redirect('upload_complaints')
    return render(request,'user/upload_complaints.html',{'username':username,'email':email})


def view_my_complaints(request):
    if 'userid' not in request.session:
        messages.error(request, 'Session expired. Please log in again.')
        return redirect('user_login')
        
    userid = request.session['userid']
    complaints = user_complaints.objects.filter(userid=userid).order_by('-id')
    return render(request, 'user/view_my_complaints.html', {'complaints': complaints})


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