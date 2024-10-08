from configs import subject_list
class SubjectHandler():

    def isSubjectAdded(self, grade, section, subject):
        # TO-DO: Create dao to get the details from table
        subject_details_for_class = 15 
        if (subject_list[subject] & subject_details_for_class):
            return True
        return False