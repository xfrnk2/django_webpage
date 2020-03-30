from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Tester
# Create your views here.
def index(request):
    return render(request, 'index.html')

def regConTester(request):
    name = request.POST['name']
    qs = Tester(t_name = name)
    qs.save()



    return HttpResponseRedirect(reverse('testers:allQuestions'))

def showQuestions(request):
        return render(request, 'testers/questions.html')

def conQuestions(request):
    answer = request.POST.get('cb', 0)
    qs = Tester(t_answer = answer)
    qs.save()
    context = {'tester': qs}
    return render(request, 'testers/results.html', context)
