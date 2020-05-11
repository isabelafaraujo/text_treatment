#script para ler txt e contar palavras
import fileinput

file=open('diabetes_e_saude_bucal.txt', 'r')

#contar paragrafos e tirar linhas em branco
with file as f:
#    texto = [texto.rstrip() for texto in f]
    texto = list(filter(lambda value: value != '', [value.replace('\n', '').strip('"') for value in f])) #tira \n

qnt_paragrafos= (len(texto))-1 #nao leva em consideracao o titulo do arquivo
print(texto[0])
print("Quantidade de paragrafos: ", qnt_paragrafos)
print("Quantidade de paragrafos + titulo: ", len(texto))
print(texto)

