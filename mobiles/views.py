# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

from .models import Devices
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from .models import Devices,DeviceDetails
from django.urls import reverse_lazy





def index(request):
    all_devices=Devices.objects.all()
    context={'all_devices': all_devices}
    return render(request,'mobiles/index.html',context)

def detail(request, device_id):
    if not request.user.is_authenticated():
        return render(request, 'mobiles/login.html')
    else:
        user = request.user
        device = get_object_or_404(Devices, pk=device_id)
        return render(request, 'mobiles/details.html', {'device': device, 'user': user})


class UserFormView(View):
    form_class=UserForm
    template_name='mobiles/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('mobiles:index')
        return render(request,self.template_name,{'form':form})

def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('mobiles:index')
            else:
                return render(request, 'mobiles/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'mobiles/login.html', {'error_message': 'Invalid login'})
    return render(request, 'mobiles/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('mobiles:login_user')



class DeviceCreate(CreateView):
    model = Devices
    fields = ['device_name','device_model']

    def add_device(self,request):

        return redirect(request,'mobiles/devices_form.html')

class DeviceUpdate(UpdateView):
    model = Devices
    fields = ['device_name','device_model']
    template_name = 'mobiles/deviceupdate_form.html'

class DeviceDelete(DeleteView):
        model = Devices
        success_url=reverse_lazy('mobiles:index')

        








