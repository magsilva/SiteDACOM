# Create your views here.

from django.shortcuts import render_to_response
from desenvolvimento.models import DepartamentoAcademico
from desenvolvimento.models import Curso
from desenvolvimento.models import Professor
from desenvolvimento.models import Coordenacao
from desenvolvimento.models import Funcionario
from django.http import HttpResponse


def index(request):
	return HttpResponse('Hello, World') 
