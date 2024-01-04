from . import views
from django.urls import path

urlpatterns = [
    path('question_creator/', views.question_creator_function, name="question_creator_function"),
]

