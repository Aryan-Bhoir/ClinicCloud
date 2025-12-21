from django.urls import path
from .import views as v

urlpatterns = [

    path('', v.login_page, name='login'),


    path('add_patient',v.addpatient,name='add_patient'),
    path('patient_list',v.patientlist,name='patient_list'),
    path('edit_patient/<int:id>/', v.editpatient,name='edit_patient'),
    path('delete_patient/<int:id>/', v.deletepatient,name='delete_patient'),

    path('add_doctor',v.adddoctor,name='add_doctor'),
    path('doctor_list',v.doctorlist,name='doctor_list'),
    path('delete_doctor/<int:id>',v.deletedoctor,name='delete_doctor'),
    path('edit_doctor/<int:id>',v.editdoctor,name='edit_doctor'),

    path('add_appointment',v.addappointment,name='add_appointment'),
    path('appointment_list',v.appointmentlist,name='appointment_list'),
    path('delete_appointment/<int:id>',v.deleteappointment,name='delete_appointment'),
    path('edit_appointment/<int:id>',v.editappointment,name='edit_appointment'),
    
    
    path('logout/',v.logout_page,name='logout'),

    path('dashboard/',v.dashboard,name='dashboard')

    



]
    

    
