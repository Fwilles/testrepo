# my first python code file in a repository on GitHub

# BUBBLE SORT
def bubble_sort(lista: list):
  for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1, 1):
      if lista[j] >= lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
  return lista
