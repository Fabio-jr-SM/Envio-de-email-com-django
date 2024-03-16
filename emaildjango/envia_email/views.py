from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def envia_email(request):
    send_mail('Assunto','Esse é o Email que estou te enviando','fabbhio007@gmail.com',['fabiojunimif@gmail.com'])
    return HttpResponse('olá')