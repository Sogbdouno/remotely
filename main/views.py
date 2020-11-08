from django.shortcuts import render,redirect
from .models import Job
from .forms import JobForm

# Create your views here.
def home(request):
    ctx = {}
    ctx['tous_les_jobs'] = Job.objects.all()
    ctx['un_seul_job'] = Job.objects.get(title="manager")
    return render(request, "home.html", ctx)
def contact(request):
    return render(request, "contact.html")
def about(request):
    return render(request, "about.html")

def create(request):
    if request.method == "POST":
        form = JobForm(request.POST).save()
        return redirect('create')
    else:
        form = JobForm()
    return render(request, 'create.html',{'form':form,'tous_les_jobs':Job.objects.all()})

def job_delete(request, job_id):
    
    pid = int(job_id)
    # try except verification sur la gestion des erreurs
    try:
        job = Job.objects.get(id = pid)
    except Job.DoesNotExist:
        return redirect('create')
    job.delete()
    return redirect('create')


def job_update(request, job_id):
    pid = int(job_id)
    try:
        job = Job.objects.get(id = pid)
    except Job.DoesNotExist:
        return redirect('create')
     
    job_form = JobForm(request.POST or None, instance = job)
    if job_form.is_valid():
        job_form.save()
        return redirect('create')
    return render(request, 'create.html', {'form':job_form})