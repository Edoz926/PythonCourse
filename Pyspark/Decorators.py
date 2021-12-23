"""
Decorators
"""

def func(string):
    def wrapper():
        print("Started")
        print(string)
        print("Ended")

    #ritorna i valori del wrapper perchè lo invoco
    return wrapper()
    #se fosse stato solo l'oggetto wrapper -> diverso
    #return wrapper

x = func("hello")

#oppure possiamo richiamare una funzione
def funci(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")

    # ritorna i valori del wrapper perchè lo invoco
    return wrapper
    # se fosse stato solo l'oggetto wrapper -> diverso

def func2():
    print("Hello, i'm a function")

def func3():
    print("Hello, i'm function 3")

xx = funci(func2)
print(xx)
xx()

y = funci(func3)
print(y)
y()

#stores the function in another function
func3=funci(func3)
func3()

"""
Per definirlo basta imporre un decoratore con @funzione
"""
@funci
def func4():
    print("Hello, i'm function 4")

func4()

#Devo quindi di base descrivere sempre un wrapper di quella funzione, che prenda però in considerazione
#diverse funzioni e diversi argomenti -> far si che venga reso il più plasmabile possibile

def decoratore(f):
    def wrapper(*args,**kwargs):
        print("Started")
        f(*args,**kwargs)
        print("Ended")

    return wrapper

def decoratore2(f):
    def wrapper(*args,**kwargs):
        print("Started")
        rv = f(*args,**kwargs)
        print("Ended")
        return rv

    return wrapper

@decoratore
def func2(x,y):
    print(x)
    return y

res = func2("AIUTOOOOOO!",8)
print(res)
# non stora il valore di ritorno il wrapper. dobbiamo sistemarlo

@decoratore2
def func2(x,y):
    print(x)
    return y

res = func2("AIUTOOOOOO!",8)
print(res)

#Esempio decoratore del tempo
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time:", total)
        return rv
    return wrapper

@timer
def test():
    for i in range(100000):
        pass

test()