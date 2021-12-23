"""
Context manager

Usefull for shared resources
Exemple: writing on the same file
"""
#we have to ensure that this file will be closed
file = open("file.txt","w")
file.write("hello")
file.close()

# #il with è il nostro context manager
# with open("file.txt","r") as file:
#     file.write("hello")
    #quando è finito il codice che dobbiamo scrivere -> exit code

#come è fatto
class File:
    def __init__(self, filename, method):
        self.file = open(filename,method)

    def __enter__(self): #prima cosa da fare
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):
        #se non siamo in un'eccezione -> chiama quella particolare eccezione
        print("Exit")
        print(f"{type}, {value}, {traceback}")
        #inserendo il blocco e andando a vedere l'esito con un'exception -> tipo: <class 'Exception'> , value:  ,traceback: <traceback object at 0x0000020DFB064748>
        self.file.close()
        #aggiungendo un return True, non abbiamo più un crash con l'eccezione inserita
        #! non inserire un return diretto se abbiam oexception che devono essere risolte accuratamente
        if type == Exception:
            return True

with File("file.txt","w") as f:
    print("Middle")
    f.write("hello")

#come creare il context manager a partire da un generator
import contextlib
#importo un decorator che può decorare un generator per farlo diventare un context manager

@contextlib.contextmanager
def file(filename, method):
    print('enter')
    file = open(filename,method)
    yield file
    file.close()

with file('text.txt',"w") as f:
    print("middle")
    f.write("hello")
