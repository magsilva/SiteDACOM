from desenvolvimento.models import DepartamentoAcademico
from desenvolvimento.models import Curso
from desenvolvimento.models import Funcionario
from desenvolvimento.models import Professor
from desenvolvimento.models import Coordenacao
from desenvolvimento.models import Artigos
from django.contrib import admin

admin.site.register(DepartamentoAcademico)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Coordenacao)
admin.site.register(Funcionario)
admin.site.register(Artigos)
