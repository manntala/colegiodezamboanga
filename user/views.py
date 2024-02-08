from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Student
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('home')

class EnrollmentCreateView(CreateView):
    model = Student
    fields = '__all__'
    # template_name = 'enrollment_create.html' 
    success_url = reverse_lazy('enrollment-create')

class EnrollmentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('student-list')

class EnrollmentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')

class EnrollmentDetailView(DetailView):
    model = Student

class EnrollmentListView(ListView):
    model = Student

class HomePageView(LoginView):
    template_name = 'index.html'

    def get_success_url(self):
        return reverse_lazy('enrollment-create')

    def form_valid(self, form):
        default_username = 'username'
        default_password = 'password'
        
        user = authenticate(username=default_username, password=default_password)
        
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)
