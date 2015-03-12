#encoding: iso-8859-1
import sys
import shutil
import Levenshtein
import os, errno


def criarDiretorio(dir):
        if not os.path.exists(dir):
                try:
                        os.makedirs(dir)
                ### except OSError as exc:
                except:
                        print "\n[ERRO] Não foi possível criar ou atualizar o diretório: "+dir.encode('utf8')
                        print "[ERRO] Você conta com as permissões de escrita? \n"
                        return 0
        return 1

def copiarArquivos(dir):
        shutil.copy2(sys.path[0]+'/css/scriptLattes.css', dir)
        shutil.copy2(sys.path[0]+'/imagens/lattesPoint0.png', dir)
        shutil.copy2(sys.path[0]+'/imagens/lattesPoint1.png', dir)
        shutil.copy2(sys.path[0]+'/imagens/lattesPoint2.png', dir)
        shutil.copy2(sys.path[0]+'/imagens/lattesPoint3.png', dir)
        shutil.copy2(sys.path[0]+'/imagens/lattesPoint_shadow.png', dir)
        shutil.copy2(sys.path[0]+'/imagens/doi.png', dir)

def compararCadeias(str1, str2, qualis=False):
	str1 = str1.strip().lower()
	str2 = str2.strip().lower()

	if len(str1)==0 or len(str2)==0:
		return 0
	
	if len(str1)>=20 and len(str2)>=20 and (str1 in str2 or str2 in str1):
		return 1

	if qualis:
		dist = Levenshtein.ratio(str1, str2)
		if len(str1)>=10 and len(str2)>=10 and dist>=0.90: #0.8
			#return 1
			return dist

	else:
		if len(str1)>=10 and len(str2)>=10 and Levenshtein.distance(str1, str2)<=8: #5
			return 1
	return 0

