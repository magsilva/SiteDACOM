from django.contrib import admin


from desenvolvimento.models import DepartamentoAcademico
from desenvolvimento.models import Curso
from desenvolvimento.models import Professor
from desenvolvimento.models import Coordenacao
from desenvolvimento.models import Artigo
from desenvolvimento.models import ArtigoEmPeriodico
from desenvolvimento.models import ArtigoEmConferencia
from desenvolvimento.models import AreaDeAtuacao
from desenvolvimento.models import Evento
from desenvolvimento.models import Integrante
from desenvolvimento.models import IntegranteProfessor
from desenvolvimento.models import Projeto
from desenvolvimento.models import DadosDeProfessor
from desenvolvimento.models import Disciplina



admin.site.register(DepartamentoAcademico)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Coordenacao)
admin.site.register(Artigo)
admin.site.register(ArtigoEmPeriodico)
admin.site.register(ArtigoEmConferencia)
admin.site.register(Projeto)
admin.site.register(Evento)
admin.site.register(AreaDeAtuacao)
admin.site.register(Integrante)
admin.site.register(IntegranteProfessor)
admin.site.register(DadosDeProfessor)
admin.site.register(Disciplina)


