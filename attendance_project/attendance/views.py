from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import now
from .models import Student, Attendance
import datetime

def attendance_list(request):
    # Get the selected date from request or default to today
    selected_date = request.GET.get('date', now().date())

    # Ensure selected_date is in proper format
    if isinstance(selected_date, str):
        selected_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d").date()

    # Check if attendance for the selected date exists, else create it
    students = Student.objects.all()
    for student in students:
        Attendance.objects.get_or_create(student_id=student, date=selected_date, defaults={'present': False})

    # Fetch attendance records for the selected date
    attendance_records = Attendance.objects.filter(date=selected_date)

    # Get all unique attendance dates for dropdown
    available_dates = Attendance.objects.values_list('date', flat=True).distinct()

    return render(request, 'attendance_list.html', {
        'attendance_records': attendance_records,
        'selected_date': selected_date,
        'available_dates': available_dates
    })

def update_attendance(request, attendance_id):
    if request.method == 'POST':
        attendance = get_object_or_404(Attendance, id=attendance_id)
        attendance.present = not attendance.present  # Toggle attendance status
        attendance.save()
        return JsonResponse({'success': True, 'present': attendance.present})
    return JsonResponse({'success': False}, status=400)