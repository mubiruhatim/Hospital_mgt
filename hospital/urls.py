from django.contrib import admin
from django.urls import path,include
from hospital_management_system.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name = 'index_page'),
    path('patient/', PatientView.as_view(), name = 'patients_page'),
    path('Ward/', WardView.as_view(), name = 'Ward_page'),
    path('Bed/', BedView.as_view(), name = 'Bed_page'),
    path('Admission/', AdmissionView.as_view(), name = 'Admission_page'),
    path('Doctor/', DoctorView.as_view(), name = 'Doctor_page'),
    path('Payment/', PaymentView.as_view(), name = 'Payment_page'),



    path('delete-patient/<int:patient_id>', DeletePatient, name = 'delete-patient'),
    path('delete-ward/<int:ward_id>', DeleteWard, name = 'delete-ward'),
    path('delete-payment/<int:payment_id>', DeletePayment, name = 'delete-payment'),
    path('delete-doctor/<int:doctor_id>', DeleteDoctor, name = 'delete-doctor'),
    path('delete-bed/<int:bed_id>', DeleteBed, name = 'delete-bed'),
    path('delete-admission/<int:admission_id>', DeleteAdmission, name = 'delete-admission'),


    path('accounts/', include('django.contrib.auth.urls'))

    
    ]
    
