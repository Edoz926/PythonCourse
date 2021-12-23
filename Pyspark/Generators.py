"""
Generators
"""

"""
Un generatore serve per concentrarsi su un singolo valore per volta senza storare un'intera lista di oggetti
lavorando su un loop efficente
"""

#classe che genera tutti i numeri al quadrato di una lista
class Gen:
    def __init__(self,n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        """Generera la sequenza di numeri dal primo all'ultimo ^2"""
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2
        self.last += 1
        return rv

g = Gen(100)

while True:
    try:
        print(next(g))
    except StopIteration:
        break


def gen2(n):
    for i in range(n):
        yield i**2
        #al posto di fermare la funzione, abbiamo una pausa, al posto di un return che è lo stop
        #pausa la funzione fino a quando non è richiamata di nuovo -> più ottimale, meno

g = gen2(100)
for i in g:
    print(i)

#riazzero l'iteratore per il prossimo passo
g = gen2(100)
#se utilizzassi al posto del looè il next, prendendo come valore quello dell'iteratore
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#memorywise
import sys
g = gen2(10000)
x = [i ** 2 for i in range(10000)]
print(sys.getsizeof(x))
print(sys.getsizeof(g))