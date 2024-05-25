from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import  Project, Todolist
from django.contrib.auth.forms import AuthenticationForm
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def login_view(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_project')  
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Username already exists'})
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('login')  
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def create(request):
    return render(request,"create.html")

@login_required
def create_code(request):
    title=request.POST["title"]
    tasks=request.POST["tasks"]
    created_by = request.user
    ob=Project()
    ob.title=title
    ob.created_by = created_by 
    ob.todos=tasks
    ob.created_date=datetime.datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Project Created"); window.location="/view_project"</script>''')

@login_required
def view_project(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request,"view_project.html",{"projects": projects})


def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        project.title = request.POST["title"]
        project.save()
        return HttpResponse(f'''<script>alert("Project Title updated"); window.location="/show_todos/{id}/"</script>''')
    return render(request, 'edit_project.html', {'project': project})

@login_required
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        project.delete()
        return HttpResponse('''<script>alert("Project Deleted"); window.location="/view_project"</script>''')
    return render(request, 'confirm_delete.html', {'project': project})

@login_required
def add_todos(request, id):
    project = get_object_or_404(Project, id=id)
    request.session['project_id'] = id
    project = get_object_or_404(Project, id=id)
    existing_todos_count = Todolist.objects.filter(project=project).count()

    todo_range = range(1, project.todos - existing_todos_count + 1)
    return render(request, "add_todos.html", {'project': project, 'todo_range': todo_range})

@login_required
def add_todos_code(request):
    project_id = request.session.get('project_id')
    project = get_object_or_404(Project, id=project_id)
    updated_date = datetime.datetime.today()
    description = request.POST.get(f'description')

    if description:
            todo = Todolist(
                project=project,
                description=description,
                status=False,
                updated_date=updated_date
            )
            todo.save()

    return redirect('show_todos', project_id=project_id)

@login_required
def show_todos(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    todos = Todolist.objects.filter(project=project)
    completed_count = todos.filter(status=True).count()
    total_count = todos.count()

    if request.method == "POST":
        completed_todo_ids = [int(key.split('_')[1]) for key in request.POST if key.startswith('todo_')]
        new_title = request.POST.get("title")
        if new_title:
            project.title = new_title
            project.save()
        
        for todo in todos:
            if todo.id in completed_todo_ids:
                todo.status = True  
            else:
                
                if todo.status:
                    todo.status = True
                else:
                    todo.status = False 
            todo.save()
        
        return redirect('show_todos', project_id=project_id)
    
    return render(request, 'show_todos.html', {'project': project, 'todos': todos, 'completed_count': completed_count,
        'total_count': total_count})


@login_required
def edit_project_todos(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    todos = Todolist.objects.filter(project=project)
    
    if request.method == "POST":
        for todo in todos:
            todo.status = f'todo_{todo.id}' in request.POST
            todo.description = request.POST.get(f'description_{todo.id}', todo.description)
            todo.updated_date=datetime.datetime.now()
            todo.save()
        return HttpResponse(f'''<script>alert("Todos updated"); window.location="/show_todos/{project_id}/"</script>''')
    
    return render(request, 'edit_todos.html', {'project': project, 'todos': todos})

@login_required
def delete_todos(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    todos = Todolist.objects.filter(project=project)
    
    if request.method == "POST":
        for todo in todos:
            todo_id = str(todo.id)
           
            if todo_id in request.POST:
                todo.delete()
        return HttpResponse(f'<script>alert("Selected todos deleted"); window.location="/show_todos/{project_id}/"</script>')
    
    return render(request, 'delete_todos.html', {'project': project, 'todos': todos})










