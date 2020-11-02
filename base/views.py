from django.shortcuts import render
from django.http import HttpResponse

from .models import Post,About,Skill,Service,Project
# Create your views here.

from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


#for sending emails
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def home(request):  
    posts = Post.objects.filter(active=True,featured=True)[0:3]
    me = About.objects.first()
    skills = Skill.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()

    

    context = {'posts':posts,'me':me,'skills':skills,'services':services,'projects':projects}
    return render(request, 'base/index.html',context)
    
def blog(request):
    posts = Post.objects.filter(active=True)
    
    page = request.GET.get('page')
    paginator = Paginator(posts, 6)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {'posts':posts}
    return render(request, 'base/blog.html',context)
    
def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {"post":post}
    return render(request, 'base/post.html',context)

def sendEmail(request):

    if request.method == 'POST':
        template = render_to_string('base/email_template.html',{
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['azzam49coder@gmail.com']
        )

        email.fail_silently = False
        email.send()

    return  render(request, 'base/email_sent.html')
