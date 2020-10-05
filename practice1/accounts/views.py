from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from .forms import SignupForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")
            # next_url = request.GET.get('next', '/')
            # return redirect('admin/')
            return
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form' : form,
    })