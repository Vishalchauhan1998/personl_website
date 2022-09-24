from django.shortcuts import render
from Profiles.models import Profile,Course,Project


def home_page(request):
    #post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:3]
    # context = {'post': post}
    prodata = Profile.objects.all()
    course_data = Course.objects.all()
    project_data = Project.objects.all()
    context = {'pro': prodata,'co_data': course_data,'pro_data' : project_data}
    return render(request, 'home.html', context)

#def course_page(request):
#    course_data = Course.objects.all()
    #context = {'post': post}
#    context = {'co_data': course_data}
 #   return render(request, 'home.html', context)


def service_page(request):
    return render(request, 'services.html')

def contact_page(request):
    return render(request, 'contact.html')

def course_details(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {'co_data': course}
    return render(request, 'course_details.html', context)

def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {'pro_data': project}
    return render(request, 'project_details.html', context)