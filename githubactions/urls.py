from django.urls import path
from githubactions.views import ItemView

urlpatterns = [
    path('', ItemView.as_view()),
]
