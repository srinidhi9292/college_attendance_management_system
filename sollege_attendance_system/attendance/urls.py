"""
Complete Attendance App URL Configuration
Path: attendance/urls.py
"""

from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Department URLs
    path('manage/departments/', views.manage_departments, name='manage_departments'),
    path('manage/departments/add/', views.add_department, name='add_department'),
    path('manage/departments/edit/<int:pk>/', views.edit_department, name='edit_department'),
    path('manage/departments/delete/<int:pk>/', views.delete_department, name='delete_department'),
    
    # Branch URLs
    path('manage/branches/', views.manage_branches, name='manage_branches'),
    path('manage/branches/edit/<int:pk>/', views.edit_branch, name='edit_branch'),
    path('manage/branches/delete/<int:pk>/', views.delete_branch, name='delete_branch'),
    
    # Section URLs
    path('manage/sections/', views.manage_sections, name='manage_sections'),
    path('manage/sections/edit/<int:pk>/', views.edit_section, name='edit_section'),
    path('manage/sections/delete/<int:pk>/', views.delete_section, name='delete_section'),
    
    # Subject URLs
    path('manage/subjects/', views.manage_subjects, name='manage_subjects'),
    path('manage/subjects/edit/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('manage/subjects/delete/<int:pk>/', views.delete_subject, name='delete_subject'),
    
    # Faculty URLs (Admin)
    path('manage/faculty/', views.manage_faculty, name='manage_faculty'),
    path('manage/faculty/edit/<int:pk>/', views.edit_faculty, name='edit_faculty'),
    path('manage/faculty/delete/<int:pk>/', views.delete_faculty, name='delete_faculty'),
    
    # Student URLs (Admin)
    path('manage/students/', views.manage_students, name='manage_students'),
    path('manage/students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('manage/students/delete/<int:pk>/', views.delete_student, name='delete_student'),
    
    # Timetable URLs
    path('manage/timetable/', views.manage_timetable, name='manage_timetable'),
    path('manage/timetable/delete/<int:pk>/', views.delete_timetable, name='delete_timetable'),
    # subject assignment
    path('manage/subject-assignments/', views.manage_subject_assignments, name='manage_subject_assignments'),
    path('manage/subject-assignments/delete/<int:pk>/', views.delete_subject_assignment, name='delete_subject_assignment'),
    
    # Faculty URLs
    path('faculty/mark-attendance/<int:timetable_id>/', views.mark_attendance, name='mark_attendance'),
    path('faculty/edit-attendance/<int:timetable_id>/', views.edit_attendance, name='edit_attendance'),
    path('faculty/view-attendance/', views.view_attendance_records, name='view_attendance_records'),
    path('faculty/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('faculty/profile/', views.faculty_profile, name='faculty_profile'),
    path('faculty/change-password/', views.faculty_change_password, name='faculty_change_password'),
    path('faculty/weekly-schedule/',views.faculty_weekly_schedule, name='faculty_weekly_schedule'),
    
    # Student URLs
    path('student/my-attendance/', views.view_my_attendance, name='view_my_attendance'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/change-password/', views.student_change_password, name='student_change_password'),
]
