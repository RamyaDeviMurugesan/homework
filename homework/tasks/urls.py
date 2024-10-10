from django.urls import path
from .views import HomeWorkCreateView, HomeWorkListView, AddClassroomView, ViewClassRoom, HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', TaskListView.as_view(), name='task_list'),
    # path('add/', TaskCreateView.as_view(), name='add_task'),
    # path('complete/<int:pk>/', TaskCompleteView.as_view(), name='complete_task'),
    path('add-homework/', HomeWorkCreateView.as_view(), name='add_homework'),
    path('view-homework/', HomeWorkListView.as_view(), name='view_homework'),
    path('add-classroom/', AddClassroomView.as_view(), name='add_classroom'),
    path('view-classroom/', ViewClassRoom.as_view(), name='view_classroom'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
