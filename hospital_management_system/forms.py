from django.forms import ModelForm,DateInput,TextInput,CharField
from .models import *


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields ='__all__'
        widgets = {
            "date_of_birth": DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date", "class": "form-control"}
            )
        }

class WardForm(ModelForm):
    class Meta:
        model = Ward
        fields ='__all__'

class BedForm(ModelForm):
    class Meta:
        model = Bed
        fields ='__all__'

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields ='__all__'

class AdmissionForm(ModelForm):
    class Meta:
        model = Admission
        fields ='__all__'
        
class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields ='__all__'

class LoginForm(ModelForm):
    username = CharField(
        max_length=50,
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
            
        })
    )
    password = CharField(
        max_length=100,
        widget=TextInput(attrs={
            'type':'password',
            'class': 'form-control',
            'placeholder': 'Enter Password'
            
        })
    )
    class Meta:
        model= Patient
        fields = ['username','password']


        
