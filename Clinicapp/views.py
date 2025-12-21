from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# functions for the Patient 

def addpatient(request):
    if request.method=='POST':
        f=PatientForm(request.POST)
        f.save()
        return redirect('/dashboard')
    else:
        f=PatientForm()
        con={'form':f}
        return render(request,'addpatient.html',con)
    
def patientlist(request):
    search = request.GET.get("search", "")
    gender = request.GET.get("gender", "")

    patients = Patient.objects.all()

    # Search
    if search:
        patients = patients.filter(name__icontains=search)

    # Filter
    if gender:
        patients = patients.filter(gender=gender)

    # List of all genders (for right side panel)
    genders = set(Patient.objects.values_list("gender", flat=True))

    return render(request, "patientlist.html", {
        "patients": patients,
        "search": search,
        "gender": gender,
        "genders": genders
    })


def deletepatient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('/patient_list')

def editpatient(request,id):
    f=Patient.objects.get(id=id)
    if request.method=='POST':
        a=PatientForm(request.POST,instance=f)
        a.save()
        return redirect('/patient_list')
    else:
        a=PatientForm(instance=f)
        con={'form':a}
        return render(request,'editpatient.html',con)









# functions for the doctoer 

def adddoctor(request):
    if request.method=='POST':
        f=DoctorForm(request.POST)
        f.save()
        return redirect('/dashboard')
    else:
        f=DoctorForm()
        con={'form':f}
        return render(request,'adddoctor.html',con)
    
def doctorlist(request):
    search = request.GET.get("search", "")
    specialization = request.GET.get("specialization", "")

    doctors = Doctor.objects.all()

    if search:
        doctors = doctors.filter(name__icontains=search)

    if specialization:
        doctors = doctors.filter(specialization=specialization)

    specializations = set(Doctor.objects.values_list("specialization", flat=True))

    return render(request, "doctorlist.html", {
        "doctors": doctors,
        "search": search,
        "specialization": specialization,
        "specializations": specializations
    })


def deletedoctor(request,id):
    f=Doctor.objects.get(id=id)
    f.delete()
    return redirect('/doctor_list')

def editdoctor(request,id):
    f=Doctor.objects.get(id=id)
    if request.method=='POST':
        a=DoctorForm(request.POST,instance=f)
        a.save()
        return redirect('/doctor_list')
    else:
        a=DoctorForm(instance=f)
        con={'form':a}
        return render(request,'editdoctor.html',con)
    



# functions for the Appointment 

def addappointment(request):
    if request.method=='POST':
        f=AppointmentForm(request.POST)
        f.save()
        return redirect('/dashboard')
    else:
        f=AppointmentForm()
        con={'form':f}
        return render(request,'addappointment.html',con)
    
def appointmentlist(request):
    search = request.GET.get("search", "")
    status = request.GET.get("status", "")

    appointments = Appointment.objects.all()

    if search:
        appointments = appointments.filter(
            patient__name__icontains=search
        ) | appointments.filter(
            doctor__name__icontains=search
        ) | appointments.filter(
            problem__icontains=search
        )

    if status:
        appointments = appointments.filter(status=status)

    statuses = set(Appointment.objects.values_list("status", flat=True))

    return render(request, "appointmentlist.html", {
        "appointments": appointments,
        "search": search,
        "statuses": statuses,
        "status": status,
    })


def deleteappointment(request,id):
    f=Appointment.objects.get(id=id)
    f.delete()
    return redirect('/appointment_list')

def editappointment(request,id):
    f=Appointment.objects.get(id=id)

    if request.method=='POST':
        a=AppointmentForm(request.POST,instance=f)
        a.save()
        return redirect('/appointment_list')
    else:
        a=AppointmentForm(instance=f)
        con={'form':a}
        return render(request,'editappointment.html',con)
    


# Login function
def login_page(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            return render(request,'login.html',{"error":"Invalid credentials"})
        
    return render(request,'login.html')


@login_required
def logout_page(request):
    logout(request)
    return redirect("login")



# Dashboard Function
@login_required
def dashboard(request):
    con={
        "total_patients" : Patient.objects.count(),
        "total_doctors":Doctor.objects.count(),
        "total_appointments":Appointment.objects.count(),
    }
    return render(request,"dashboard.html",con)