from django.shortcuts import redirect
from .models import Registration
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from .forms import RegistrationForm
from django.urls import reverse_lazy

class create(CreateView):
    model=Registration
    form_class=RegistrationForm
    template_name='create.html'
    success_url=reverse_lazy('home')

class home(ListView):
    model=Registration
    template_name='home.html'

class update(UpdateView):
    model=Registration
    form_class=RegistrationForm
    template_name='update.html'
    success_url=reverse_lazy('home')

    def post(self,request,*args,**kwargs):
        if request.POST.get('action')=='cancel':
            return redirect('home')
        return super().post(request,*args,**kwargs)

class delete(DeleteView):
    model=Registration
    template_name='delete.html'
    success_url=reverse_lazy('home')

    def post(self,request,*args,**kwargs):
        if request.POST.get('action')=='cancel':
            return redirect('home')
        return super().post(request,*args,**kwargs)
    
class read(DetailView):
    model=Registration
    template_name='detail.html'




