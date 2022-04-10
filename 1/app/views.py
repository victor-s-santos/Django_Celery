from django.shortcuts import render
from app.forms import EmailForm
from django.views.generic.edit import FormView

class EmailFormView(FormView):
    template_name = 'app/home.html'
    form_class = EmailForm
    success_url = '/'

    def form_valid(self, form):
        nome = form.name
        # context = {
        #     "nome": form.name,
        #     "mensagem": form.message,
        #     "email": form.email
        # }
        #print("O email será enviado em 20 segundos!")
        # print(f"O email será enviado para {context['nome']}")
        print(nome)
        return super().form_valid(form)