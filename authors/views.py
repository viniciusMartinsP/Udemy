from email import message
from xml.dom import ValidationErr

from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from genericpath import exists

from .forms import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    
    if form.is_valid():
        #O DJANGO NÃO ESTÁ SALVANDO DE FATO O FORMULÁRIO, ESTÁ APENAS ARMAZENANDO EM UMA VARÍAVEL
        user = form.save(commit=False)
        #O .SET_PASSWORD É UM MÉTODO DO PRÓPRIO DJANGO QUE CONVERTE A STRING DE SENHA EM UM HASH
        user.set_password(user.password)
        user.save()
        messages.success(request,'Your user has been created, please log in')

        #APAGA OS DADOS DA SESSÃO(FORMULÁRIO)
        del(request.session['register_form_data'])

    return redirect('authors:register')

def clean_email(self):
    email = self.cleaned_data.get('email','')
    exists = User.objects.filter(email=email).exists()

    if exists:
        raise ValidationError(
            'User e-mail is already in use', code='invalid',
        )

    return email

