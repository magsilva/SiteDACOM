from django.db import models
from weblattes.settings import STATIC_URL
from django.core.validators import validate_slug

CATEGORIAS = (
('0','Adm, Contabeis e Turismo'),
('1','Antropologia / Arqueologia'),
('2','Arquitetura e Urbanismo'),
('3','Artes / Musica'),
('4','Astronomia / Fisica'),
('5','Biodiversidade'),
('6','Biotecnologia'),
('7','Ciencia da Computacao'),
('8','Ciencia de Alimentos'),
('9','Ciencia Politica e Relacoes Internacionais'),
('10','Ciencias Agrarias'),
('11','Ciencias Ambientais'),
('12','Ciencias Biologicas I'),
('13','Ciencias Biologicas II'),
('14','Ciencias Biologicas III'),
('15','Ciencias Sociais Aplicadas I'),
('16','Direito'),
('17','Economia'),
('18','Educacao'),
('19','Educacao Fisica'),
('20','Enfermagem'),
('21','Engenharias I'),
('22','Engenharias II'),
('23','Engenharias III'),
('24','Engenharias IV'),
('25','Ensino'),
('26','Farmacia'),
('27','Filosofia/Teologia - Filosofia'),
('28','Filosofia/Teologia - Teologia'),
('29','Geociencias'),
('30','Geografia'),
('31','Historia'),
('32','Interdisciplinar'),
('33','Letras / Linguistica'),
('34','Matematica / Probabilidade e Estatistica'),
('35','Materiais'),
('36','Medicina I'),
('37','Medicina II'),
('38','Medicina III'),
('39','Medicina Veterinaria'),
('40','Nutricao'),
('41','Odontologia'),
('42','Planejamento Urbano e Regional / Demografia'),
('43','Psicologia'),
('44','Quimica'),
('45','Saude Coletiva'),
('46','Servico Social'),
('47','Sociologia'),
('48','Zootecnia / Recursos Pesqueiros'),

)

class CV(models.Model):
  lid = models.CharField(max_length=30, verbose_name="ID Lattes", validators=[validate_slug])
  categoria = models.CharField(max_length=2, choices=CATEGORIAS)
  status = models.SmallIntegerField()

  def __unicode__(self):
    return "%s - %s" % (self.lid, self.categoria)

  def get_absolute_url(self):
    return "%s/%s%s" % (STATIC_URL, self.lid, self.categoria)
