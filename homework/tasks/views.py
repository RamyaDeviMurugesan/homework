
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import HomeWork
from django.contrib.auth.mixins import LoginRequiredMixin
from .configs import subject_list, grades, sections, fields_for_homework_view
from .utils import format_post_data
from tasks.dao.school_details_dao import SchoolDetailsDAO
from tasks.dao.homework_dao import HomeWorkDAO
import datetime
import json

class HomeWorkCreateView(ListView):

    # This method handles GET requests (form rendering)
    def get(self, request):

        subjects_and_tasks = {
            "ENGLISH": [],
            "TAMIL": [],
            "MATHS": [],
            "SCIENCE": [],
            "SOCIAL_SCIENCE": []
        }


        context = {
            "grades": grades,
            "sections": sections,
            "subjects_and_tasks": subjects_and_tasks
        }
        return render(request, 'tasks/hw_add.html', context)

    # This method handles POST requests (form submission)
    def post(self, request, *args, **kwargs):
        user = request.user.username
        form_data = format_post_data(request)
        for subject in subject_list.keys():
            if form_data.get(subject) and len(form_data[subject]) > 0:
                for task in form_data[subject]:
                    homework_data = {'grade': form_data['grade'], 
                                     'section': form_data['section'],
                                     'homeworkdate': datetime.datetime.strptime(form_data['homeworkdate'], "%Y-%m-%d"), 
                                     'subject': subject, 
                                     'task': task, 
                                     'added_by': user
                                     }
                    HomeWorkDAO(homework_data).create_homework()
        # request.content_params
        return render(request, 'tasks/hw_view.html')
        
    
class HomeWorkListView(ListView):
    model = HomeWork
    context_object_name = 'homeworks'  #

    def get(self, request):
        user = request.user.username
        homework_details = HomeWorkDAO.get_homework_by_user(user)
        homework_list = {}
        for fields in fields_for_homework_view:
            homework_list[fields] = []
        for homework in homework_details:
            if homework['grade'] not in homework_list['grade']:
                homework_list['grade'].append(homework['grade'])
            if homework['section'] not in homework_list['section']:
                homework_list['section'].append(homework['section'])
            if homework['hwDate'] not in homework_list['hwDate']:
                homework_list['hwDate'].append(homework['hwDate'])
        print(homework_list)
        return render(request, 'tasks/hw_search.html', {"homework_list": homework_list})
    
    def post(self, request):
        user = request.user.username
        grade = request.POST.get('grade')
        section = request.POST.get('section')
        hwDate = request.POST.get('hwDate')
        homework_list_by_date = HomeWorkDAO.get_homework_by_date(user, grade, section, hwDate)
        print(homework_list_by_date)
        return render(request, 'tasks/hw_view.html', {"homework_list": homework_list_by_date})

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class AddClassroomView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            "subjects": list(subject_list.keys()),
            "grades": grades,
            "sections": sections
        }
        return render(request, 'tasks/class_add.html', context)

    def post(self, request):
        form_data = format_post_data(request)
        subjects = form_data.get('Subject')
        sub_bit = 0
        for sub in subjects:
            sub_bit += subject_list[sub]
        form_data['sub_bit'] = sub_bit
        print(form_data)
        SchoolDetailsDAO(form_data).create_classroom()
        
        # Render the template showing the added classroom
        return redirect('view_classroom')


class ViewClassRoom(View):
    def get(self, request):
       print(request.user.id)
       classroom_details = SchoolDetailsDAO.get_all_classrooms()
       for classroom in classroom_details:
        sub_list = []
        for subject in subject_list.keys():
            if (classroom['subject'] & subject_list[subject]):
                sub_list.append(subject)
        classroom['subject'] = sub_list
       return render(request, 'tasks/class_view.html', {'classroom_details': classroom_details})
        
               
           
           
