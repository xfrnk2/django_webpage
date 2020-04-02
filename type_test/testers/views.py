from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Tester, Feedback
from .forms import FeedbackForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def regConTester(request):
    Tester.objects.all().delete()
    name = request.POST['name']
    answer = request.POST['answer']
    qs = Tester(t_name = name, t_answer = answer)
    qs.save()

    return HttpResponseRedirect(reverse('testers:allQuestions'))

def showQuestions(request):
    qs = Tester.objects.all()[0]
    context = {'tester_value': qs}
    return render(request, 'testers/questions.html', context)

def conQuestions(request):
    answer = sum(list(map(int, request.POST.getlist('cb'))))
    qs = Tester(t_answer = answer)
    qs.save()
    context = {'tester': qs}
    return render(request, 'testers/results.html', context)

def createFeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('testers:feedbackList')
    else:
        form = FeedbackForm()

    return render(request, 'testers/feedbacks.html', {'form': form})

def getFeedbackList(request):
    qs = Feedback.objects.all()
    context = {'feedback_list': qs}
    return render(request, 'testers/recievedfeedback.html', context)