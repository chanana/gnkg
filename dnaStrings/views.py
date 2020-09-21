from celery.result import AsyncResult
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from dnaStrings.forms import dnaStringSubmission
from dnaStrings.models import Tasks
from dnaStrings.tasks import findProtein
from django.contrib import messages


@require_http_methods(["GET", "POST"])
def dnaStringsView(request):
    if request.method == "POST":
        form = dnaStringSubmission(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            job_name = data["job_name"]
            dna_string = data["dna_string"]
            findProtein.delay(job_name=job_name, dna_string=dna_string)
            messages.success(
                request,
                f"Your job {job_name} was submitted. Click Monitor Jobs to see its progress.",
            )
            return render(request, "submit.html", context={"form": dnaStringSubmission})
    else:
        return render(request, "submit.html", context={"form": dnaStringSubmission})


def track_jobs():
    entries = Tasks.objects.all()
    information = []
    for item in entries:
        progress = 100  # max value for bootstrap progress
        # bar, when  the job is finished
        result = AsyncResult(item.task_id)
        if isinstance(result.info, dict):
            progress = result.info["progress"]
        information.append(
            [item.job_name, item.dna_string, item.dna_result, result.state, progress, item.task_id]
        )
        # information.append([result.state, progress, item.task_id])
    return information


@require_GET
def monitor(request):
    info = track_jobs()
    # return render(request, "monitor.html", context={"info": info})
    return render(request, "index.html", context={"info": info})


@require_GET
def cancel_job(request, task_id=None):
    result = AsyncResult(task_id)
    result.revoke(terminate=True)
    info = track_jobs()
    return render(request, "index.html", context={"info": info})
    # return render(request, "monitor.html", context={"info": info})


@require_GET
def delete_job(request, task_id=None):
    a = Tasks.objects.filter(task_id=task_id)
    a.delete()
    info = track_jobs()
    # return render(request, "monitor.html", context={"info": info})
    return render(request, "index.html", context={"info": info})
