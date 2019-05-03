from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts import forms
from accounts.forms import RegisterForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.

from accounts.models import User


@login_required
def login_success(request):
    info = User.objects.get(id=request.user.id).userprofile.is_validated
    if request.user.groups.filter(name="shops").exists():
        return HttpResponse('shop')
    else:
        if info:
            return HttpResponse('valid')
        else:
            return register(request)


@login_required
def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            user.userprofile.real_first_name = form.cleaned_data.get('real_first_name')
            user.userprofile.real_last_name = form.cleaned_data.get('real_last_name')
            user.userprofile.phone_number = form.cleaned_data.get('phone_number')
            user.userprofile.email = form.cleaned_data.get('email')
            user.save()
            user.userprofile.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.userprofile.is_validated = True
        user.save()
        user.userprofile.save()
        return HttpResponse('Validated')
    else:
        return HttpResponse('Activation link is invalid!')
