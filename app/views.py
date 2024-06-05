from django.shortcuts import render,get_object_or_404
from .models import Quiz,Question,Choice
def quizes(request):
    quizes= Quiz.objects.all()
    context={
        "quizes":quizes
    }
    return render(request,'quizes.html',context)

def quiz_detail(request,quiz_id):
    quiz = get_object_or_404(Quiz,pk=quiz_id)
    questions = quiz.question_set.all()
    context={
        "questions":questions
    }
    return render(request,'quizes_detail.html',context)