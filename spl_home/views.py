from django.shortcuts import render
from .models import OnGoingProject
from .models import UpcomingProject
from .models import CompletedProject
from .models import Home
from django.core.paginator import Paginator
from django.views.generic import ListView


ongoing_details = OnGoingProject.objects.all()
upcoming_details = UpcomingProject.objects.all()
completed_details = CompletedProject.objects.all()
home_details = Home.objects.all()


def home(request):#instead we can use ListView class view instead of function
    #return HttpResponse("<h1>This home Page</h1>")
    oproject_list = ongoing_details
    count = len(oproject_list)
    paginator = Paginator(oproject_list, count) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'home_details': 'home_details',
        'page_obj': page_obj,
        'count': count
    }
    return render(request, 'spl_home/home.html', context)


def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'spl_home/about.html', context)


def contact(request):
    context ={
        'title': "Contact Us"
    }
    return render(request, 'spl_home/contact.html', context)


def ongoing_projects(request):
    oproject_list = ongoing_details
    paginator = Paginator(oproject_list, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': "On Going Projects",
        'ongoing_details': ongoing_details,
        'page_obj': page_obj
    }
    return render(request, 'spl_home/ongoing_projects.html', context)


def upcoming_projects(request):
    uproject_list = upcoming_details
    paginator = Paginator(uproject_list, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={
        'title': "Upcoming Projects",
        'upcoming_details': upcoming_details,
        'page_obj': page_obj
    }
    return render(request, 'spl_home/upcoming_projects.html', context)


def completed_projects(request):
    cproject_list = completed_details
    paginator = Paginator(cproject_list, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': "Completed Projects",
        'completed_details': completed_details,
        'page_obj': page_obj
    }
    return render(request, 'spl_home/completed_projects.html', context)

