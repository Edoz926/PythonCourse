"""
Metodi DUNDER, o metodi speciali, che iniziano con __ (già visto un init)
Non chiamati da noi, ma dietro le quinte, chimaati solo in certe circostanze
"""


class Studente:
    '''
    Aggiunta una variabile
    '''
    ore_settimanali = 36
    corpo_studentesco = 0
    '''
    Cosi facendo sarà disponibile se verrà usata nella classe (Ore_settimanali) e non verrà assegnata a una nuova istanza
    Posso aggiungere la stessa variabile all'init per far si che si aggiorni ogni volta che lancio il costruttore
    VAR: corpo_studentesco (variabile di Istanza)

    Aggiungo gli attributi di ogni studente
    metodo init (inizializzatore o costruttore)
    '''

    def __init__(self, nome, cognome, corso_di_studi):
        '''
        self: se stesso passato come primo attributo
        rappresenta L'istanza, ciascun singolo oggetto creato dalla classe
        rappresenta una referenza ad ogni singolo oggetto creato dalla classe
        il metodo init INIZIALIZZA E ATTIVA le proprietà di ciascun oggetto o istanza

        per ciascun self -> nome passato sarà il nome del nome passato, ecc
        Sono le VARIABILI DELL'ISTANZA
        '''
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
        Studente.corpo_studentesco += 1

    def scheda_personale(self):
        return f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso di Studi:{self.corso_di_studi}\n Ore Settimanali:{Studente.ore_settimanali}"

    def __add__(self, other):
        """ other rappresenta l'altro studente da aggiungere via dunder """
        return self.nome + " " + other.cognome

    """
    Aggiunta dei dunder __str__ (rappresentazione in stringa) e __repr__ (rappresentazione esaustiva e non ambigua, orientato agli sviluppatori) 
    facilmente leggibile e immediata per il pubblico
    """
    def __str__(self):
        """Rappres leggibile per il pubblico"""
        return f"Lo Studente {self.nome} {self.cognome}"
        pass
    def __repr__(self):
        """Rappre non Ambigua e per svilupatori"""
        return f"Studente('{self.nome}','{self.cognome}','{self.corso_di_studi}')"
        pass

"""
Da console: se creo un dizionario e lo invoco: 
alfabeto = {1:"a",2:"b",3:"c",4:"d"}
alfabeto[4] -> python in realtà sta richiamando un metodo speciale, chiamato __getitem__
per vederli tutti -> help(alfabeto), e ne troveremo molti con __

Un esempio possono essere i metodi polimorfi, che cambiano dal tipo di informazioni in input
5+5 = 10
"veni, vidi, " + "vici" = "veni, vidi, vici"
metodo __add__ -> int.__add__(5,10) o str.__add__("a","b")
"""

studente1 = Studente("john","cena","wrestler")
studente2 = Studente("big","show","retired")

print(studente1+studente2)

"""
Agli oggetti di tipo studente manca la funzionalità di rappresentazione in stringa
Infatti stampando sotto otteniamo solo la visualizzazione dello spazio in meoìmoria sottostante
Metodi dunder __str__ e __repr__
Sarebbero da portare in ogni classe per portare il print a tutti
"""

#Chiamata esplicita
print(studente1)
print(str(studente2))
print(repr(studente1))

#Chiamata implicita
print(Studente.__str__(studente1))
print(Studente.__repr__(studente1))

#oppure
print(studente1.__str__())

