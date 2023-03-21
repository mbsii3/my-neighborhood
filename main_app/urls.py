from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reports/', views.reports_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('reports/create/', views.ReportCreate.as_view(), name='report_create'),
    path('reports/<int:pk>/delete/', views.ReportDelete.as_view(), name='reports_delete'),
    path('reports/<int:report_id>/', views.reports_detail, name='detail'),
]   

