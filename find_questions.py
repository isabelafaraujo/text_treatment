import os

path = "F:/Faculdade/UFG/...."

filelist = []

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
                print(frase + arquivo + '\n')
