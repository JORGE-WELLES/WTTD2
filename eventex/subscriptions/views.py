from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            body = render_to_string('subscriptions/subscription_email.txt',
                                    form.cleaned_data)
            mail.send_mail('Confirmação de inscrição',
                           body,
                           'vendas.pjhiramaq@gmail.com',
                           ['vendas.pjhiramaq@gmail.com', form.cleaned_data['email']])
            from django.contrib import messages
            messages.success(request, 'Inscricao realizada com sucesso!')
            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})
    else:

        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)



