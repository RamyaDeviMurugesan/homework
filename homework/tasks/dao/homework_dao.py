from tasks.models import HomeWork
from redis import Redis

class HomeWorkDAO:
    def __init__(self, data=None):
        if data:
            self.grade = data.get('grade')
            self.section = data.get('section')
            self.hwDate = data.get('homeworkdate')
            self.subject = data.get('subject')
            self.task = data.get('task')
            self.added_by = data.get('added_by')
        self.redis = Redis(host='localhost', port=6379)


    def create_homework(self):
        task_id = HomeWork.objects.create(grade=self.grade,
                                       section=self.section,
                                       subject=self.subject,
                                       hwDate=self.hwDate,
                                       tasks=self.task,
                                       added_by=self.added_by).id
        self.redis.sadd(str(task_id)+"_Completed", "")
        return task_id
        
    
    @staticmethod
    def get_homework_by_date(user, grade, section, hwDate):
        homework_queryset = HomeWork.objects.filter(hwDate=hwDate, added_by=user, grade=grade, section=section)
        homework_list = [
            {
                'grade': homework.grade,
                'section': homework.section,
                'hwDate': homework.hwDate.strftime("%Y-%m-%d"),
                'subject': homework.subject,
                'tasks': homework.tasks,
                'id': homework.id
            }
            for homework in homework_queryset
            ]
        return homework_list
    
    def get_homework_by_class(grade, section):
        return HomeWork.objects.filter(grade=grade, section=section)
    
    def get_homework_by_user(user):
        return HomeWork.objects.filter(added_by=user).values('hwDate', 'grade', 'section')