from email import message

from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

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

    #.is_valid() MÉTODO DO PRÓPRIO DJANGO QUE VALIDA O FORMULÁRIO
    #.save() MÉTODO DO PRÓPRIO DJANGO QUE SALVA O FORMULÁRIO
    if form.is_valid():
        form.save()
        messages.success(request,'Your user has been created, please log in')

        #APAGA OS DADOS DA SESSÃO(FORMULÁRIO)
        del(request.session['register_form_data'])

    return redirect('authors:register')
