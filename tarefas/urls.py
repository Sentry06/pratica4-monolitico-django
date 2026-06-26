from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_tarefas, name="lista_tarefas"),
    path("nova/", views.criar_tarefa, name="criar_tarefa"),
    path("editar/<int:id>/", views.editar_tarefa, name="editar_tarefa"),
    path("deletar/<int:id>/", views.deletar_tarefa, name="deletar_tarefa"),

    path("api/tarefas/", views.api_lista_tarefas),
    path("api/tarefa/<int:id>/", views.api_buscar_tarefa),
    path("api/tarefas/nova/", views.api_criar_tarefa),
    path("api/tarefa/editar/<int:id>/", views.api_editar_tarefa),
    path("api/tarefa/deletar/<int:id>/", views.api_deletar_tarefa),
]