from django.conf.urls import url
from dnaStrings import views

app_name = "dnaStrings"

urlpatterns = [
    url(r"^submit/$", views.dnaStringsView, name="submit"),
    url(r"^monitor/$", views.monitor, name="monitor"),
    url(r"^delete_job/(?P<task_id>.+)/$", views.delete_job, name="delete_job"),
    url(r"^cancel_job/(?P<task_id>.+)/$", views.cancel_job, name="cancel_job"),
]
