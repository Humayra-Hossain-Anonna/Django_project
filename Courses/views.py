from django.http import HttpResponse
from django.template import loader
from .models import Summary


def index(request):
    all_courses = Summary.objects.all()
    template = loader.get_template('Courses/index.html')
    context = {
        'all_courses' : all_courses,
    }
    return HttpResponse(template.render(context, request))

def detail(request, Course_id):
    return HttpResponse("<h2> Details  for course :" + str(Course_id) + "</h2>")