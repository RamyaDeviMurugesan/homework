from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from tasks.models import HomeWork

class Command(BaseCommand):
    help = 'Create Teacher and Student groups with relevant permissions'

    def handle(self, *args, **kwargs):
        # Create Teacher group
        teacher_group, created = Group.objects.get_or_create(name='Teacher')
        student_group, created = Group.objects.get_or_create(name='Student')

        # Get the content type for the Task model
        task_content_type = ContentType.objects.get_for_model(HomeWork)

        # Assign permissions to Teacher group
        can_add_homework = Permission.objects.get(codename='add_homework', content_type=task_content_type)
        can_view_homework = Permission.objects.get(codename='view_homework', content_type=task_content_type)
        can_change_homework = Permission.objects.get(codename='change_homework', content_type=task_content_type)
        teacher_group.permissions.add(can_add_homework, can_view_homework, can_change_homework)

        # Assign view permission to Student group
        student_group.permissions.add(can_view_homework)

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions.'))
