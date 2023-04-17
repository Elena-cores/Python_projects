l = []
l.append(2)
l.append('hola mundo')
l.extend([2, 'halo', 'nails'])
l = l + ['helooo', 4]
print(l)
print(len(l))
print()

obj = {"name": "elena", "age": 20} #JSON javascript object ntoation
print(obj)
print(obj["name"])
estudiantes = []
estudiantes.append(obj)
print(estudiantes)
estudiantes.append({"name": "pepe", "age": 12})
print(estudiantes)
class Estudiante:
    def __init__(self, name, age):
        self.name = name
        self.age = age

estudiantes.append(Estudiante("carlos", 12))
print(estudiantes[2].__dict__)
print(estudiantes[2].name)
print(estudiantes)

