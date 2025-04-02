from django.urls import path
from .views import attendance_list, update_attendance

urlpatterns = [
    path('', attendance_list, name="attendance_list"),  # Main attendance view
    path('update/<int:attendance_id>/', update_attendance, name="update_attendance"),  # AJAX update view
]
