import os

path = "F:/Faculdade/UFG/Mestrado/NPL/AmericansHealth/arquivos_diabetes"

filelist = []
questions = []

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            filelist.append(file)

for arquivo in filelist:
    f = open(arquivo, "r", encoding='ISO-8859-1')
    frases = f.readlines()
    words = '?'

    for frase in frases:
        for pergunta in frase:
            if pergunta == '?':
               questions.append(frase)

perguntas = [i for n, i in enumerate(questions) if i not in questions[n + 1:]]
for perguntas in perguntas:
    print(perguntas)

print(len(perguntas))

