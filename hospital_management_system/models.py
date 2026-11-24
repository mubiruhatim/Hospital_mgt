from django.db import models

GENDER_CHOICES = [
    ('male','MALE'),
    ('female','FEMALE')
]

BED_STATUSES = [
    ('free','FREE'),
    ('taken','TAKEN')
]
MODES_OF_PAYMENT = [
    ('cash','CASH'),
    ('mobile_money','MOBILE MONEY'),
    ('bank','BANK')
]
DEPARTMENTS = [
    ('sugery','SURGERY'),
    ('laboratory','LABORATORY'),
    ('pharmacy','PHARMACY'),
    ('medicine','MEDICINE'),
    ('dentistry','DENTISTRY')
]


class Patient(models.Model):
    name= models.CharField(max_length=50,unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES,default='male')
    contact = models.CharField(max_length=16,unique=True)
    address= models.TextField()
    care_taker  = models.CharField(max_length=50)
    care_taker_contact  = models.CharField(max_length=10)
    ward = models.ForeignKey('Ward',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name




class Ward(models.Model):
    name=models.CharField(max_length =50,unique=True)
    capacity= models.IntegerField(default=1)
    amount= models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Bed(models.Model):
    ward = models.ForeignKey(Ward, related_name='Beds', on_delete=models.CASCADE)
    status = models.CharField(max_length=6,choices=BED_STATUSES,default='free')

    def __str__(self):
        return f'Bed-{self.id}'

class Doctor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    contact = models.CharField(max_length=16,unique=True)
    department = models.CharField(max_length=50,choices=DEPARTMENTS,default='medicine')

    def __str__(self):
        return self.name

class Admission(models.Model):
    date = models.DateField(auto_now_add=True)
    doctor = models.ForeignKey( Doctor, related_name='doctor_admissions', on_delete=models.CASCADE)
    patient = models.ForeignKey( Patient, related_name='patient_admissions', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['doctor','patient','date']

    def __str__(self):
        return f'Admission {self.id} on {self.date}'


class Payment(models.Model):
    admission = models.ForeignKey( Admission, related_name='payments', on_delete=models.CASCADE)
    amount= models.IntegerField(default=0)
    mode_of_payt = models.CharField(max_length=14,choices=MODES_OF_PAYMENT,default='cash',verbose_name='Mode of Payment')
    date_of_payment = models.DateField(auto_now=True)
    recieved_by = models.CharField(max_length=50)

    def __str__(self):
        return f'payment - {self.id} to {self.recieved_by}'

