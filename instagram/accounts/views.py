from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next', '/')
            signed_user.send_welcome_email() #FIXME : Celery로 처리하는것을 추천

            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form' : form, 
    })