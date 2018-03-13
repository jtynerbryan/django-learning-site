from django.http import HttpResponse
from django.shortcuts import render

from .models import Course


def course_list(request):
    courses = Course.objects.all()
    c = ""
    for course in courses:
        c += f"\n{course.title}: {course.description}\n"

    return HttpResponse(c)
