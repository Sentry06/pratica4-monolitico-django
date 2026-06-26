from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Tarefa


def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, "tarefas/lista.html", {"tarefas": tarefas})


def criar_tarefa(request):
    if request.method == "POST":
        Tarefa.objects.create(
            nome=request.POST["nome"],
            descricao=request.POST["descricao"],
            data_inicio=request.POST["data_inicio"],
            status=request.POST["status"]
        )
        return redirect("lista_tarefas")

    return render(request, "tarefas/form.html")


def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == "POST":
        tarefa.nome = request.POST["nome"]
        tarefa.descricao = request.POST["descricao"]
        tarefa.data_inicio = request.POST["data_inicio"]
        tarefa.status = request.POST["status"]
        tarefa.save()
        return redirect("lista_tarefas")

    return render(request, "tarefas/form.html", {"tarefa": tarefa})


def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect("lista_tarefas")

@csrf_exempt
def api_lista_tarefas(request):

    if request.method == "GET":

        tarefas = list(Tarefa.objects.values())

        return JsonResponse(tarefas, safe=False)
    
@csrf_exempt
def api_buscar_tarefa(request, id):

    try:
        tarefa = Tarefa.objects.get(id=id)

        return JsonResponse({
            "id": tarefa.id,
            "nome": tarefa.nome,
            "descricao": tarefa.descricao,
            "data_inicio": tarefa.data_inicio,
            "status": tarefa.status
        })

    except Tarefa.DoesNotExist:

        return JsonResponse({
            "message": "Tarefa não encontrada"
        }, status=404)
    
@csrf_exempt
def api_criar_tarefa(request):

    if request.method == "POST":

        dados = json.loads(request.body)

        tarefa = Tarefa.objects.create(
            nome=dados["nome"],
            descricao=dados["descricao"],
            data_inicio=dados["data_inicio"],
            status=dados["status"]
        )

        return JsonResponse({
            "id": tarefa.id,
            "nome": tarefa.nome,
            "descricao": tarefa.descricao,
            "data_inicio": tarefa.data_inicio,
            "status": tarefa.status
        }, status=201)
    
@csrf_exempt
def api_editar_tarefa(request, id):

    try:

        tarefa = Tarefa.objects.get(id=id)

    except Tarefa.DoesNotExist:

        return JsonResponse({
            "message": "Tarefa não encontrada"
        }, status=404)

    if request.method == "PUT":

        dados = json.loads(request.body)

        tarefa.nome = dados.get("nome", tarefa.nome)
        tarefa.descricao = dados.get("descricao", tarefa.descricao)
        tarefa.data_inicio = dados.get("data_inicio", tarefa.data_inicio)
        tarefa.status = dados.get("status", tarefa.status)

        tarefa.save()

        return JsonResponse({
            "message": "Tarefa atualizada com sucesso"
        })
    
@csrf_exempt
def api_deletar_tarefa(request, id):
    try:

        tarefa = Tarefa.objects.get(id=id)

    except Tarefa.DoesNotExist:

        return JsonResponse({
            "message": "Tarefa não encontrada"
        }, status=404)

    if request.method == "DELETE":

        tarefa.delete()

        return JsonResponse({
            "message": "Tarefa excluída com sucesso"
        })

# To do: criar view para mostrar os detalhes de um unico objeto em especifico  