from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),  # Adjust to your latest migration
    ]

    operations = [
        # Add department field to Subject model
        migrations.AddField(
            model_name='subject',
            name='department',
            field=models.ForeignKey(
                default=1,  # Set a default department ID temporarily
                on_delete=django.db.models.deletion.CASCADE,
                related_name='subjects',
                to='attendance.department'
            ),
            preserve_default=False,
        ),
        
        # Add indexes for better performance
        migrations.AddIndex(
            model_name='subject',
            index=models.Index(fields=['department', 'branch'], name='idx_dept_branch'),
        ),
        migrations.AddIndex(
            model_name='subject',
            index=models.Index(fields=['semester'], name='idx_semester'),
        ),
        
        # Add updated_at to SubjectAssignment
        migrations.AddField(
            model_name='subjectassignment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        
        # Add indexes to SubjectAssignment
        migrations.AddIndex(
            model_name='subjectassignment',
            index=models.Index(fields=['faculty', 'is_active'], name='idx_faculty_active'),
        ),
        migrations.AddIndex(
            model_name='subjectassignment',
            index=models.Index(fields=['section', 'is_active'], name='idx_section_active'),
        ),
        
        # Add fields to Timetable for permanent scheduling
        migrations.AddField(
            model_name='timetable',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        
        # Add indexes to Timetable
        migrations.AddIndex(
            model_name='timetable',
            index=models.Index(fields=['day_of_week', 'is_active'], name='idx_day_active'),
        ),
        migrations.AddIndex(
            model_name='timetable',
            index=models.Index(fields=['subject_assignment', 'is_active'], name='idx_subj_assign_active'),
        ),
        
        # Add indexes to Attendance
        migrations.AddIndex(
            model_name='attendance',
            index=models.Index(fields=['date', 'status'], name='idx_date_status'),
        ),
        
        # Add indexes to AttendanceSummary
        migrations.AddIndex(
            model_name='attendancesummary',
            index=models.Index(fields=['academic_year', 'attendance_percentage'], name='idx_year_percentage'),
        ),
        
        # Add indexes to AuditLog
        migrations.AddIndex(
            model_name='auditlog',
            index=models.Index(fields=['user', 'timestamp'], name='idx_user_timestamp'),
        ),
        migrations.AddIndex(
            model_name='auditlog',
            index=models.Index(fields=['model_name', 'timestamp'], name='idx_model_timestamp'),
        ),
    ]