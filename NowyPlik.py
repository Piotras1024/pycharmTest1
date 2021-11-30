def pole_prostokata(a, b):
    pole = a * b
    return pole

def pole_kwadratu(a):
    pk = pole_prostokata(a, a)
    return pk

print ("Pole prostokąta " + str(pole_prostokata(3, 4)))

print ("pole kwadratu " + str(pole_kwadratu(3)))
