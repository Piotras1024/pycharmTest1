def pole_prostokata(a, b):
    pole = a * b
    return pole

def pole_kwadratu(a):
    pk = pole_prostokata(a, a)
    return pk

def pole_kola(r):
    return 3.14 * r * r

print ("Pole prostokąta " + str(pole_prostokata(3, 4)))

print ("pole kwadratu " + str(pole_kwadratu(3)))

print ("pole kola " + str(pole_kola(3)))
