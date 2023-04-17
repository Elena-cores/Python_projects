a = 2
b = 3
#print(type(b))
#print(a)
#b = "Hola mundo"
#print(type(b))
#print(b)
count = "hola" + "hello"
colect = [1, 2, 3, 4]
print(count)
str(a) + b # por si a es int y b es string -> ej. 3Hola

#while count > 0:
   # print(count)
    #count -= 1

#for x in range(count):
 #   print(x)

for x in colect:
     print(x)

def sumar3(one, two):
        r = one + two
        return r

def sumar(one, two):
    if (type(one) is int and type(two) is int):
        r = one + two
        return r
    elif (type(one) is str and type(two) is str):
        r = one + two + "\n"
        return r
    else:
        raise Exception("invalid type") 


#temp = sumar(a, b)
#print(temp)

def recorrer(n):
    for i in range(n):
        print(i)
        


#__init_-> métodos para inicializar los miembros de una clase cada vez que creamos una instancia
# def __init__(self, [argumentValues(s)]):
# self.MemberName = argumentValue
# ej. clase point. Cuando llamemos a esa clase, deberia mantener los detalles de x, y coordenadas 