from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from delivery.models import Tasks
from delivery.forms import TaskForm
import datetime
import pika

# Create your views here.
def index(request):
    return render(request, "urban_piper/index.html")


@login_required
def dashboard(request):
    if request.user.is_staff:
        return HttpResponseRedirect("/dashboard/task")
    return HttpResponseRedirect("/dashboard/delivery_task")


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Login the user
            auth.login(request, user)
            return JsonResponse({"message": "Login Successful"}, status=200)
        else:
            return JsonResponse({"message": "Invalid Username/Password"}, status=500)

    return render(request, "urban_piper/login.html")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


@login_required
def task(request):
    tasks_list = Tasks.objects.all()
    return render(request, "urban_piper/task.html", {"tasks_list": tasks_list})


#     tasks = Task.objects.all()
#     return render(
#         request, "urban_piper/tasks_list.html", {"tasks": tasks, "title": "Task"}
#     )


@login_required
def newtask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return HttpResponseRedirect("/dashboard/task", {"success": "Task Added"})
        else:
            return render(
                request, "urban_piper/new_task.html", {"form": form, "title": "Task"}
            )
    else:
        form = TaskForm()
        return render(
            request, "urban_piper/new_task.html", {"form": form, "title": "Task"}
        )


def canceltask(request, id=None):
    print("delete")
    instance = Tasks.objects.get(id=id)
    instance.cancelled_on = datetime.datetime.now()
    instance.status = "cancelled"
    instance.cancelled_by = request.user
    print(instance.cancelled_on)
    instance.save()
    return HttpResponseRedirect("/dashboard/task")


def accepttask(request, id=None):
    instance = Tasks.objects.get(id=id)
    instance.accepted_on = datetime.datetime.now()
    instance.status = "accepted"
    instance.accepted_by = request.user
    instance.save()
    return HttpResponseRedirect("/dashboard/delivery_task")


def deliverytask(request):
    delivery_tasks_list = Tasks.objects.filter(accepted_by = request.user)
    #delivery_tasks_list = Tasks.objects.all()
    return render(
        request,
        "urban_piper/delivery_task.html",
        {"delivery_tasks_list": delivery_tasks_list},
    )

def completetask(request,id=None):
    instance = Tasks.objects.get(id=id)
    instance.completed_on = datetime.datetime.now()
    instance.status = "completed"
    instance.save()
    return HttpResponseRedirect("/dashboard/delivery_task")

def declinetask(request,id=None):
    instance = Tasks.objects.get(id=id)
    instance.declined_on = datetime.datetime.now()
    instance.status = "declined"
    instance.declined_by = request.user
    instance.save()
    return HttpResponseRedirect("/dashboard/delivery_task")



def send_message(request):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World1')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World2')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World3')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World4')
    print(" [x] Sent 'Hello World!'")
    connection.close()
    return 

def receive_message(request):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()


    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)
    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    return HttpResponseRedirect("/")

