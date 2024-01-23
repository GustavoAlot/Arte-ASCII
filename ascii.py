# *=============================================================
#  UNIFAL = Universidade Federal de Alfenas .
#  BACHARELADO EM CIENCIA DA COMPUTACAO.
#  Trabalho...... : Imagem ASCII
#  Disciplina.... : Processamento de Imagens
#  Professor..... : Luiz Eduardo da Silva
#  Aluno......... : Gustavo Fernandez Pascoaleto
#  Data.......... : 1/05/2023
# =============================================================




import sys
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

larg = 0
alt = 0
soma = 0





def readpgm(name):
  global larg, alt

  f = open(name, "r")
  assert f.readline() == 'P2\n'
  line = f.readline()
  while (line[0] == '#'):
    line = f.readline()
  (width, height) = [int(i) for i in line.split()]
  print(width, height)
  depth = int(f.readline())
  assert depth <= 255
  print(depth)

  larg = width
  alt = height

  img = []
  row = []
  j = 0
  for line in f:
    values = line.split()
    for val in values:
      row.append(int(val))
      j = j + 1
      if j >= width:
        img.append(row)
        j = 0
        row = []
  f.close()
  return img


def imgalloc(nl, nc):
  img = []
  for i in range(nl):
    lin = []
    for j in range(nc):
      lin.append(0)
    img.append(lin)
  return img


img = readpgm(sys.argv[1])
newAlt = int(sys.argv[3])
newLarg = int(sys.argv[2])

arquivo = open("result.txt", "w")
newPixels = sys.argv[4]
espectro = int(256 / len(newPixels))

propAlt = int(alt / newAlt)
propLarg = int(larg / newLarg)




for i in range(0, newAlt):          #percorrendo a nova imagem
  for j in range(0, newLarg):

    soma = 0                            
    for k in range(0, propAlt):                       #percorrendo imagem base
      for l in range(0, propLarg):            
        soma += img[i * propAlt + k][j * propLarg + l]        #conta para redimensionar imagem

    arquivo.write(newPixels[int((soma / (propAlt * propLarg)) / espectro)])        #escrevendo os caraccteres a partir da proporcao de cinza
  arquivo.write("\n")
