from tasks.models import SchoolDetails

class SchoolDetailsDAO:
    def __init__(self, data):
        self.grade = data.get('grade')
        self.section = data.get('section')
        self.subject = data.get('sub_bit')

    def create_classroom(self):
        return SchoolDetails.objects.create(grade=self.grade,section=self.section,subject=self.subject)
    
    @staticmethod
    def get_all_classrooms():
        return list(SchoolDetails.objects.all().values('grade', 'section', 'subject', 'noOfStudents'))