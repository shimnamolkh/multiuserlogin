from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import DoctorSignUpForm, PatientSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
def index(request):
    return render(request, 'account/index.html')



class doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'account/doctor_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'account/patient_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'account/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
def doctor_home(request):
    return render(request, 'account/doctor_home.html')
def patient_home(request):
    return render(request, 'account/patient_home.html')

