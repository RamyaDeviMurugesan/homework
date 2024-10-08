def format_post_data(request):
    form_data = {}
    for key, value in request.POST.items():
        if key in ["grade", "section", "homeworkdate"]:
            form_data[key] = value
        elif key in ["Subject"]:
            form_data[key] = request.POST.getlist(key)
        elif key.upper().startswith(("ENGLISH", "TAMIL", "MATHS", "SCIENCE", "SOCIAL_SCIENCE")):
            subject = key.split("[]")[0]
            form_data[subject] = request.POST.getlist(key)
        else:
            form_data[key] = value
    return form_data
        