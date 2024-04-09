from abc import ABC, abstractmethod

# Clase
class MyFirstClass(ABC): # Se crea la primera clase - abstracta

    __attribute = "" # Atributo

    def __init__(self, attribute): # Método Constructor
        self.__attribute = attribute
    
    def method_void(self): # Método público
        print("Hello, this is a class")

    @abstractmethod # Estamos declarando al método como abstracto
    def method_abstract(self):
        pass # Se indica que el método no realiza ninguna acción

# Herencia
class MySecondClass(MyFirstClass): # Esta clase hereda de la clase 'MyFirstClass'

    def __init__(self, attribute, newPrivateattribute): # Método Constructor
        super().__init__(attribute) # Esta funcíon utiliza el método constructor de la clase padre
        self.__newPrivateattribute = newPrivateattribute

    def method_greet(self): # Método público
        print(f"Hello World! {self._MyFirstClass__attribute}") # Se accede al atributo privado de la clase padre
    
    def __method_private(self): # Encapsulamiento del método con el prefijo __
        print("This is a private function")
        # Una manera de acceder al método desde fuera es usando la siguiente sintaxis 'objectname._classname(methodname)'

    def getnewPrivateattribute(self):
        return self.__newPrivateattribute # Obtenemos el valor del atributo privado
        # Otra manera de obtener el valor es usando la siguiente sintaxis 'objectname._classname(attributename)'
    
    def setnewPrivateattribute(self, newPrivateattribute):
        self.__newPrivateattribute = newPrivateattribute # Establecemos un nuevo valor al atributo encapsulado

    # Tratar de usar más los property
    @property # Lo usamos como otra manera de obtener el valor de un atributo privado
    def newPrivateattribute(self):
        return self.__newPrivateattribute

    @newPrivateattribute.setter # Lo usamos como otra manera de establecer un nuevo valor al atributo privado
    def newPrivateattribute(self, newPrivateattribute):
        self.__newPrivateattribute = newPrivateattribute

    def method_abstract(self): # Se realiza la sobreescritura del método
        print("It was overwritten, MySecondClass")

class MyThirdClass(MyFirstClass):

    def __init__(self, attribute): # Método Constructor
        super().__init__(attribute)

    def method_abstract(self): # Se realiza la sobreescritura del método
        print("It was overwritten, MyThirdClass")

# objMyFirstClass = MyFirstClass("Attribute") # Instancia de la primera clase
# print(objMyFirstClass._MyFirstClass__attribute) # Se muestra la información del atributo

objMySecondClass = MySecondClass("A_T_R_B", "Hello!") # Instancia de la segunda clase
objMySecondClass.method_greet()
objMySecondClass.method_void() # Aquí se corrobora que 'MySecondClass' hereda de 'MyFirstClass'
objMyThirdClass = MyThirdClass("A_T_R_B_E")

# Uso de los property
objMySecondClass.newPrivateattribute = "Hello World!"
print(objMySecondClass.newPrivateattribute)

# Polimorfismo
objMySecondClass.method_abstract()
objMyThirdClass.method_abstract()