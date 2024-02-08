from django.urls import path
from . import views


urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    path('enrollments/', views.EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/<int:pk>/', views.EnrollmentDetailView.as_view(), name='enrollment-detail'),
    path('', views.EnrollmentCreateView.as_view(), name='enrollment-create'),
    path('enrollments/<int:pk>/update/', views.EnrollmentUpdateView.as_view(), name='enrollment-update'),
    path('enrollments/<int:pk>/delete/', views.EnrollmentDeleteView.as_view(), name='enrollment-delete'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
