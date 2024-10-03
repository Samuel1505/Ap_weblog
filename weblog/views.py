from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from weblog.models import weblog
from django.urls import reverse_lazy
# Create your views here.
class homepage(ListView):
    model = weblog
    template_name = 'weblog/index.html'
    context_object_name = 'all_weblog'
class aboutpage(ListView):
    model = weblog
    template_name = 'weblog/about.html'
    context_object_name = 'all_weblog'
class weblogDetailview(DetailView):
    template_name = 'weblog/detail_post.html'
    model= weblog
class weblogcreateView(CreateView):
    template_name = 'weblog/create.html'
    model=weblog
    fields=['Firstname','Lastname','Gender','Date_of_birth','email','phone_number','Matric_number']
class weblogupdateview(UpdateView):
    template_name='weblog/update.html'
    model=weblog
    fields=['Firstname','Lastname','Gender','Date_of_birth','email','phone_number','Matric_number']
class weblogdeleteview(DeleteView):
    template_name='weblog/delete.html'
    model=weblog
    fields=['title','body']
    success_url= reverse_lazy('home')
 