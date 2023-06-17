from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404, redirect
from .forms import createNewTask, createNewProject

# Create your views here.
def hello(request, username):#para pasar parametros
    return HttpResponse("<h1> hello word %s</h1>" % username)

def about(request):
    return render(request,'about.html')

def index(request):
    title='Django Course'
    return render(request,'index.html',{
        'title': title
    })

def task(request):
    #task= get_object_or_404(Task, id=id)
    tasks=Task.objects.all()
    return render(request,'task/task.html',{
        'tasks':tasks
    })

def projects(request):
    projects = list(Project.objects.values())
    return render(request,'projects/projects.html',{
        'projects': projects
    })

def create_task(request):
    if request.method == 'GET':
        #show interface
         return render(request, 'task/createTask.html',{
            'form':createNewTask()
        })
    else:
         #print(request.GET['title'])
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'],
        project_id=2)
        return redirect('task')
    

def create_project(request):
    if request.method == 'GET':
        #show interface
         return render(request, 'projects/createProjects.html',{
            'form':createNewProject()
        })
    else:
         #print(request.GET['title'])
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')


def project_detail(request, id):
    project=get_object_or_404(Project, id=id)
    #Project.objects.get(id=id)

    tasks=Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html',{
    'project':project,
    'tasks':tasks
    }
    )
        
