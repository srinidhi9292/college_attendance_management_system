from django.db import migrations


def link_subjects_to_departments(apps, schema_editor):
    """
    Link existing subjects to their departments through branches
    """
    Subject = apps.get_model('attendance', 'Subject')
    
    for subject in Subject.objects.all():
        # Set department based on branch's department
        if subject.branch and subject.branch.department:
            subject.department = subject.branch.department
            subject.save()


def reverse_migration(apps, schema_editor):
    """
    Reverse operation - no action needed
    """
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_add_department_to_subject'),
    ]

    operations = [
        migrations.RunPython(link_subjects_to_departments, reverse_migration),
    ]