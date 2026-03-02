from django.shortcuts import render,redirect
# Create your views here.
from higher_officer.models import station_details
from police.models import criminal_details
def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        if (uname == 'admin' or uname == 'admin@crime.gov') and password == 'admin':
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
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        station_details.objects.create(police_name=police_name,gender=gender,station_name=station_name, area_code=area_code, location=location,
                                       email=email,area_name=area_name, userid=userid, password=password)
        return redirect('adminview_crime')
    return render(request,'higher_officer/admin_home.html')




def adminview_crime(request):

    crime_det=criminal_details.objects.all()
    return render(request,'higher_officer/adminview_crime.html',{'crime_det':crime_det})


def adminview_police(request):
    police_det = station_details.objects.all()
    return render(request, 'higher_officer/adminview_police.html', {'police_det': police_det})

def delete_police(request, pk):
    try:
        police_record = station_details.objects.get(id=pk)
        police_record.delete()
    except station_details.DoesNotExist:
        pass
    return redirect('adminview_police')