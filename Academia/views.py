from django.shortcuts import render
from django.http import HttpResponse

# RestFramework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Academia.models import Aulas, Aluno
# Create your views here.

def listaClientes(request):

    
    aulas = Aulas.objects.all()
    print(list(aulas))
    html = "<html><body>"
    for x in list(aulas):
        html += f"<h2> Aula de {x.name} - ministrada pelo(a) prof {x.prof.name} </h2>"

    html += "</body></html>"

    return HttpResponse(html)

class AlunoView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        alunos = Aluno.objects.all().values()
        data = {"message": "ok", "alunos": list(alunos)}
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        #TODO inserir o serializer
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()

        print(request.data)
        name = request.data.get('name')
        peso = request.data.get('peso')
        idade = request.data.get('idade')

        
        if name==None or name=="" or peso==None or peso=="" or idade==None or idade=="":
            return Response(data={"message": "abstence of parameters"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Aluno.objects.create(
                name = name,
                peso = peso,
                idade = idade
            )
        except Exception as e:
            print(e)
            return Response(data={"message": "abstence of parameters"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
        return Response(data={"message": "created"}, status=status.HTTP_201_CREATED) 
