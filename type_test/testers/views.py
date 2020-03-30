from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Tester
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
    answer = request.POST.get('cb', False)
    qs = Tester(t_answer = answer)
    qs.save()
    context = {'tester': qs}
    return render(request, 'testers/results.html', context)
