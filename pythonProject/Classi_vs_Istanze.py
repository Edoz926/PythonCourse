'''
Python CLASSI VS ISTANZE
'''

#CLASSSI COME STAMPINI PER I BISCOTTI

#Modellaare la realtà in modo efficiente e riutilizzabile in un modello generico
#Assegnandogli i suoi attributi personali
#

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
    def __init__(self,nome,cognome,corso_di_studi):
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


stud_uno = Studente('edo','zucca','python')
stud_due = Studente('fabio','zucca','edo')

print(stud_due.scheda_personale())
print(stud_uno.scheda_personale())

print(stud_uno.__dict__)
'''Se non viene aggiunto sull'istanza, non compare nel dict
"{'nome': 'edo', 'cognome': 'zucca', 'corso_di_studi': 'python', 'ore_settimanali': 40}'''
stud_uno.ore_settimanali += 4
#in alternativa
print(Studente.__dict__)
print(stud_uno.__dict__)


print(Studente.corpo_studentesco)