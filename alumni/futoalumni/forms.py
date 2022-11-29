from dataclasses import fields
from django.forms import ModelForm
from .models import Alumni
class RegisterAlumni(ModelForm):
    class Meta:
        model = Alumni
        fields = (
            'firstname',
            'surname',
            'othernames',
            'phone_number',
            'email',
            'year_of_graduation',
            'discipline',
            'passport',
            'subscribed',
            'company_name',
            'nature_of_biz',
            'bussines_photo'
           
            )