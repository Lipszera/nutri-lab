from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

def  cadastro(request):
  if request.method == "GET":
    return render(request, 'cadastro.html')
  elif request.method == "POST":
    username = request.POST.get('usuario')
    email = request.POST.get('email')
    password = request.POST.get('senha')
    confirm_password = request.POST.get('confirmar_senha')

    if not password_is_valid(request, password, confirm_password):
      return redirect('/auth/cadastro')

    try:
      user = User.objects.create_user(username=username,
                                      email=email,
                                      password=password,
                                      is_active=False)
      user.save()
      messages.add_message(request, constants.SUCCESS, 'Cadastro concluído com sucesso')
      return redirect('/auth/logar')
    except:
      messages.add_message(request, constants.ERROR, 'Erro do sistema')
      return redirect('/auth/cadastro')

def logar(request):
  return HttpResponse ("Você está na página de login")



# Create your views here.
