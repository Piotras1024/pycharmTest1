def pole_prostokata(a, b):
    pole = a * b
    return pole

def pole_kwadratu(a):
    pk = pole_prostokata(a, a)
    return pk

def pole_trapezu(a, b, h):
    return a * b * h / 2

print ("Pole prostokąta " + str(pole_prostokata(3, 4)))

print ("pole kwadratu " + str(pole_kwadratu(3)))

print ("pole trapezu " + str(pole_ trapezu(2,3,4)))
