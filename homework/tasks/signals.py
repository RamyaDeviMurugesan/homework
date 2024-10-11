from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, SchoolDetails

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(instance.userprofile.section)
    instance.userprofile.save()

    try:
        classroom = SchoolDetails.objects.get(grade=instance.userprofile.grade, section=instance.userprofile.section)
        classroom.noOfStudents += 1
        classroom.save()
    except SchoolDetails.DoesNotExist:
        print("Classroom does not exist for the given grade and section")

@receiver(post_delete, sender=UserProfile)
def decrement_classroom_students(sender, instance, **kwargs):
    section = instance.section
    grade = instance.grade

    try:
        classroom = SchoolDetails.objects.get(grade=grade, section=section)
        if classroom.noOfStudents > 0:
            classroom.noOfStudents -= 1
            classroom.save()
    except SchoolDetails.DoesNotExist:
        print("Classroom does not exist for the given grade and section")
        raise
