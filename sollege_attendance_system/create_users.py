# File: C:\Users\srini\Desktop\sollege_attendance_system\create_users.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sollege_attendance_system.settings')
django.setup()

from attendance.models import *
from datetime import date

print("Creating data...")

# Academic Year
academic_year, _ = AcademicYear.objects.get_or_create(
    year="2024-2025",
    defaults={
        'start_date': date(2024, 7, 1),
        'end_date': date(2025, 6, 30),
        'is_active': True
    }
)
print(f"✓ Academic Year: {academic_year.year}")

# Department
dept, _ = Department.objects.get_or_create(
    code="CSE",
    defaults={'name': "Computer Science Engineering"}
)
print(f"✓ Department: {dept.name}")

# Branch
branch, _ = Branch.objects.get_or_create(
    department=dept,
    code="BTCSE",
    defaults={
        'name': "B.Tech Computer Science",
        'duration_years': 4
    }
)
print(f"✓ Branch: {branch.name}")

# Section
section, _ = Section.objects.get_or_create(
    branch=branch,
    name="A",
    semester=5,
    academic_year=academic_year,
    defaults={'capacity': 60}
)
print(f"✓ Section: {section}")

# Admin User
try:
    admin_user = User.objects.get(username="admin")
    admin_user.role = 'admin'
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.set_password("admin")
    admin_user.save()
    print("✓ Admin user updated")
except User.DoesNotExist:
    admin_user = User.objects.create(
        username="admin",
        email="admin@college.edu",
        first_name="Admin",
        last_name="User",
        role="admin",
        is_staff=True,
        is_superuser=True
    )
    admin_user.set_password("admin")
    admin_user.save()
    print("✓ Admin user created")

# Faculty User
try:
    faculty_user = User.objects.get(username="faculty")
    faculty_user.role = 'faculty'
    faculty_user.set_password("faculty")
    faculty_user.save()
except User.DoesNotExist:
    faculty_user = User.objects.create(
        username="faculty",
        email="faculty@college.edu",
        first_name="John",
        last_name="Doe",
        role="faculty"
    )
    faculty_user.set_password("faculty")
    faculty_user.save()
print("✓ Faculty user created/updated")

# Faculty Profile
if not hasattr(faculty_user, 'faculty_profile'):
    Faculty.objects.create(
        user=faculty_user,
        employee_id="FAC001",
        department=dept,
        designation="Assistant Professor",
        qualification="M.Tech",
        date_of_joining=date(2020, 1, 1)
    )
    print("✓ Faculty profile created")

# Student User
try:
    student_user = User.objects.get(username="student")
    student_user.role = 'student'
    student_user.set_password("student")
    student_user.save()
except User.DoesNotExist:
    student_user = User.objects.create(
        username="student",
        email="student@college.edu",
        first_name="Jane",
        last_name="Smith",
        role="student"
    )
    student_user.set_password("student")
    student_user.save()
print("✓ Student user created/updated")

# Student Profile
if not hasattr(student_user, 'student_profile'):
    Student.objects.create(
        user=student_user,
        roll_number="20CS001",
        registration_number="REG2020001",
        section=section,
        date_of_admission=date(2020, 7, 1),
        current_semester=5
    )
    print("✓ Student profile created")
