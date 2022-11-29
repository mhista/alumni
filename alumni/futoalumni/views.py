from django.shortcuts import render,reverse
from django.views import generic,View
from .forms import RegisterAlumni
# Create your views here.

class AlumniRegister(generic.CreateView):
    form_class = RegisterAlumni
    template_name = 'index.html'
    context_object_name = 'alumni'

    def get_success_url(self) :
        return reverse('alumni:register')


        
    
