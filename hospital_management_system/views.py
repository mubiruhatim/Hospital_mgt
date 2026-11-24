from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.db import IntegrityError
from http import HTTPStatus
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class PatientView(LoginRequiredMixin, View):
    temp_name= 'patient.html'
    form = PatientForm()
    
    def get(self,request):
        all_patients = Patient.objects.all()
        context = {
                'patients': all_patients,
                'patients_count': all_patients.count(),
                'form': self.form
            }
        return render(request,self.temp_name,context)
    


    def post(self,request):
        form = PatientForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            name = data['name']
            dob = data['date_of_birth']
            gender = data['gender']
            contact = data['contact']
            address = data['address']
            care_taker = data['care_taker']
            care_taker_contact = data['care_taker_contact']
            ward = data['ward']
            selected_ward = Ward.objects.get(id=ward.id)

            new_patient = Patient.objects.create(
    name=name,date_of_birth=dob,gender=gender,contact=contact,address=address,care_taker=care_taker,care_taker_contact=care_taker_contact,ward=selected_ward)
            new_patient.save()
            messages.success(request, f'{new_patient.name} Added Successfully')    
            return redirect('patients_page')
            
        else:
            all_patients = Patient.objects.all()
            context = {
                'patients': all_patients,
                'patients_count': all_patients.count(),
                'form': form
            }
            return render(request, self.temp_name, context)

class  WardView(LoginRequiredMixin, View):
    temp_name= 'Ward.html'
    form =  WardForm()
    
    def get(self,request):
        all_Ward= Ward.objects.all()
        context = {
                'Wards': all_Ward,
                'wards_count': all_Ward.count(),
                'form': self.form,
                'message':'',
                'error': ''
            }
        return render(request,self.temp_name,context)


    def post(self,request):
        form = WardForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            capacity = data['capacity']
            amount = data['amount']
            new_ward = Ward.objects.create(
            name=name,  capacity= capacity,amount=amount,)
            new_ward.save()
            messages.success(request, f'{new_ward.name} Added Successfully' )   
            return redirect('Ward_page')
        else:
            all_Ward= Ward.objects.all()
            context = {
                'Wards': all_Ward,
                'wards_count': all_Ward.count(),
                'form': form
            }
            return render(request,self.temp_name,context)

class  BedView(LoginRequiredMixin, View):
    temp_name= 'Bed.html'
    form = BedForm()
    
    def get(self,request):
        all_Bed= Bed.objects.all()
        context = {
                'Beds': all_Bed,
                'Bed_count': all_Bed.count(),
                'form': self.form,
                'message':'',
                'error': ''
            }
        return render(request,self.temp_name,context)


    def post(self,request):
        form = BedForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            ward_id= data['ward']
            status = data['status']

            selected_ward = Ward.objects.get(id=ward_id.id)
            new_Bed = Bed.objects.create(
            ward = selected_ward, status= status,)
            new_Bed.save()
            messages.success(request, 'Bed Added Successfully' )   
            return redirect('Bed_page')
        else:
            all_Bed= Bed.objects.all()
            context = {
                'Beds': all_Bed,
                'Bed_count': all_Bed.count(),
                'form': form
            }
        return render(request,self.temp_name,context)

class DoctorView(LoginRequiredMixin, View):
    temp_name= 'Doctor.html'
    form =DoctorForm()
    
    def get(self,request):
        all_Doctor= Doctor.objects.all()
        context = {
                'Doctors': all_Doctor,
                'Doctor_count': all_Doctor.count(),
                'form': self.form
            }
        return render(request,self.temp_name,context)


    def post(self,request):
        form = DoctorForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            name= data['name']
            contact = data['contact']
            dept = data['department']

            new_Doc = Doctor.objects.create(
            name = name, contact= contact,department=dept)
            new_Doc.save()
            messages.success(request, f'Doctor {new_Doc.name} Added Successfully')    
            return redirect('Doctor_page')

        else:
            all_Doctor= Doctor.objects.all()
            context = {
                'Doctors': all_Doctor,
                'Doctor_count': all_Doctor.count(),
                'form': form
            }
        return render(request,self.temp_name,context)

class AdmissionView(LoginRequiredMixin, View):
    temp_name= 'Admission.html'
    form =AdmissionForm()
    
    def get(self,request):
        all_Admission= Admission.objects.all()
        context = {
                'Admissions': all_Admission,
                'Admission_count': all_Admission.count(),
                'form': self.form
            }
        return render(request,self.temp_name,context)


    def post(self,request):
        form  =  AdmissionForm(request.POST)
        try:

            if form.is_valid():
                data =form.cleaned_data
                doc = data['doctor']
                patient= data['patient']

                selected_doctor = Doctor.objects.get(id=doc.id)
                selected_patient = Patient.objects.get(id=patient.id)
                new_Admission = Admission.objects.create(
                doctor = selected_doctor, patient= selected_patient,)
                new_Admission.save()
                messages.success(request, f'{new_Admission.patient.name} Admitted Successfully')    
                return redirect('Admission_page')
            else:
                all_Admission= Admission.objects.all()
            context = {
                    'Admissions': all_Admission,
                    'Admission_count': all_Admission.count(),
                    'form': form
                }
            return render(request,self.temp_name,context)
        except IntegrityError as e:
            messages.error(request,'Admission Failed : You cant create an Admission with the same patient by the same Doctor and on the same Day')
            return redirect('Admission_page')

class PaymentView(LoginRequiredMixin, View):
    temp_name= 'Payment.html'
    form =PaymentForm()
    
    def get(self,request):
        all_Payment= Payment.objects.all()
        context = {
                'Payments': all_Payment,
                'Payment_count': all_Payment.count(),
                'form': self.form
            }
        return render(request,self.temp_name,context)


    def post(self,request):
        form = PaymentForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            admission = data['admission']
            amount= data['amount']
            mode_of_payt= data['mode_of_payt']
            recieved_by= data['recieved_by']
        

            selected_admission = Admission.objects.get(id=admission.id)
        
            
            new_Payment = Payment.objects.create(
            admission = selected_admission, amount= amount,mode_of_payt=mode_of_payt,recieved_by=recieved_by)
            new_Payment.save()
            messages.success(request, "Payment Made Successfully")   
            return redirect('Payment_page')
        else:
            all_Payment= Payment.objects.all()
        context = {
                'Payments': all_Payment,
                'Payment_count': all_Payment.count(),
                'form': form
            }
        return render(request,self.temp_name,context)


def index_view(request):
    return render(request, 'index.html')

@login_required
def DeletePatient(request,patient_id):
    selected_patient = Patient.objects.get(id = patient_id)
    try:
        if selected_patient:
            selected_patient.delete()
            messages.success(request,'Patient Deleted Successfully')
            return redirect('patients_page')

    except Patient.DoesNotExist:
        messages.error(request,'Patient Not Found')
        return redirect('patients_page')

@login_required
def DeleteWard(request,ward_id):
    selected_ward = Ward.objects.get(id = ward_id)
    try:
        if selected_ward:
            selected_ward.delete()
            messages.success(request,'Ward Deleted Successfully')
            return redirect('Ward_page')

    except Ward.DoesNotExist:
        messages.error(request,'Ward Not Found')
        return redirect('Ward_page')
 
@login_required          
def DeleteDoctor(request,doctor_id):
    selected_doctor = Doctor.objects.get(id = doctor_id)
    try:
        if selected_doctor:
            selected_doctor.delete()
            messages.success(request,'Doctor Deleted Successfully')
            return redirect('Doctor_page')

    except Doctor.DoesNotExist:
        messages.error(request,'Doctor Not Found')
        return redirect('Doctor_page')

@login_required       
def DeletePayment(request,payment_id):
    selected_payment = Payment.objects.get(id = payment_id)
    try:
        if selected_payment:
            selected_payment.delete()
            messages.success(request,'Payment Deleted Successfully')
            return redirect('Payment_page')

    except Payment.DoesNotExist:
        messages.error(request,'Payment Not Found')
        return redirect('Payment_page')

@login_required
def DeleteBed(request,bed_id):
    selected_bed = Bed.objects.get(id = bed_id)
    try:
        if selected_bed:
            selected_bed.delete()
            messages.success(request,'Bed Deleted Successfully')
            return redirect('Bed_page')

    except bed.DoesNotExist:
        messages.error(request,'Bed Not Found')
        return redirect('Bed_page')

@login_required
def DeleteAdmission(request,admission_id):
    selected_admission = Admission.objects.get(id = admission_id)
    try:
        if selected_admission:
            selected_admission.delete()
            messages.success(request,'Admission Deleted Successfully')
            return redirect('Admission_page')

    except admission.DoesNotExist:
        messages.error(request,'Admission Not Found')
        return redirect('Admission_page')

