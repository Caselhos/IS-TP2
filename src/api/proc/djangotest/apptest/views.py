from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import xmlrpc.client
import xml.etree.ElementTree as E

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def query1(request):
    server = xmlrpc.client.ServerProxy('http://rpc-server:9000')
    # Comunica com o rpc-server
    # response = request("funcao1", parametro1=parametro1, parametro2=parametro2)
    response = server.listarTitulo()

    # Retorna a resposta do rpc-server
    return JsonResponse(response, safe=False)

def query2(request, title, filename):
    server = xmlrpc.client.ServerProxy('http://rpc-server:9000')
    # Comunica com o rpc-server
    response = server.listarAlbumTitulo(title, filename)

    # Retorna a resposta do rpc-server
    return JsonResponse(response, safe=False)

def query3(request, date, filename):
    server = xmlrpc.client.ServerProxy('http://rpc-server:9000')
    # Comunica com o rpc-server
    response = server.listarAlbumData(date, filename)

    # Retorna a resposta do rpc-server
    return JsonResponse(response, safe=False)

def query4(request, artist, filename):
    server = xmlrpc.client.ServerProxy('http://rpc-server:9000')
    # Comunica com o rpc-server
    response = server.listarMusicaArtista(artist, filename)

    # Retorna a resposta do rpc-server
    return JsonResponse(response, safe=False)


