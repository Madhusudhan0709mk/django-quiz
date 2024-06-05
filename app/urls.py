from django.urls import path
from . import views

urlpatterns = [
    path('',views.quizes,name="quizes"),
    path('quiz_detail/<int:quiz_id>/',views.quiz_detail,name="quiz_detail")
]
