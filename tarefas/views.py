from django.shortcuts import render, redirect, get_object_or_404
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


# To do: criar view para mostrar os detalhes de um unico objeto em especifico  