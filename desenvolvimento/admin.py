from django.contrib import admin


from desenvolvimento.models import DepartamentoAcademico
from desenvolvimento.models import Curso
from desenvolvimento.models import Professor
from desenvolvimento.models import Coordenacao
from desenvolvimento.models import Artigo
from desenvolvimento.models import ArtigoEmPeriodico
from desenvolvimento.models import ArtigoEmConferencia
from desenvolvimento.models import Projeto


admin.site.register(DepartamentoAcademico)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Coordenacao)
admin.site.register(Artigo)
admin.site.register(ArtigoEmPeriodico)
admin.site.register(ArtigoEmConferencia)
admin.site.register(Projeto)

