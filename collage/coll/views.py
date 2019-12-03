from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import CollageDetails
# Create your views here.

class Addcollage(SuccessMessageMixin,CreateView):
    model = CollageDetails
    template_name = "register.html"
    success_url = '/addcollage/'
    success_message = "Collage Detail Saved"
    fields = ['col_id','col_name','course','m_student','f_student','image']

class CollegeDetail(ListView):
    model = CollageDetails
    template_name = "collagedetail.html"

def index(request):
    return render(request,'base.html',{})

class updaterecord(UpdateView):
    model = CollageDetails
    template_name = "update.html"
    fields = ['col_name','course','m_student','f_student','image']
    success_url = "/viewall/"


class deletecollage(DeleteView):
    model = CollageDetails
    success_url = "/viewall/"
    template_name = "delete.html"