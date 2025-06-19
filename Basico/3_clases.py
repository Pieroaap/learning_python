class Persona:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname #Asi se declaran atributos privados
        self.fullname = f"{self.__name} {self.__surname}" 

    def walk(self):
        print(f"{self.fullname} está caminando....")
    

my_person = Persona("Piero", "Alvarado")
my_person.walk()

var = False
print(not(1==1))

list = [1,2,3]
list.insert()