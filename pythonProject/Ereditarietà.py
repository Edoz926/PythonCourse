class Persona:
    ore_settimanali = 36
    corpo_studentesco = 0


    def __init__(self, nome, cognome, eta,residenza):

        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.residenza = residenza
        Persona.corpo_studentesco += 1

    def scheda_personale(self):
        scheda =  f"""
        Nome:{self.nome}
        Cognome:{self.cognome}
        Età:{self.eta}
        Residenza:{self.residenza}"""

        return scheda

    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")

        scelta = input("Cosa desideri modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome --> ")
        if scelta == "2":
            self.nome = input("Nuovo Cognome --> ")
        if scelta == "3":
            self.nome = input("Nuova Età --> ")
        if scelta == "4":
            self.nome = input("Nuova Residenza  --> ")
        else:
            pass

"""
Devo creare delle classi figlie per Insegnanti e Alunni
"""

class Studente(Persona):
    """Con la dicitura tra parentesi indico la classe GENITORE, la risultante sarà la classe FIGLIA che
    erediterà gli attributi e i metodi della classe Genitore
    Alcuni attributi saranno ereditati dalla genitore, vorremo gestire le altre con un init"""
    profilo = "Studente"
    def __init__(self, nome,cognome,eta, residenza,corso_di_studio):
        """Richiamo super per far si che vengano prese dalla genitore nome,cognome,eta,residenza
        Python andrà a controllare la presenza di un metodo costruttore dalla classe genitore per gestire gli altri"""
        super().__init__(nome,cognome,eta, residenza)
        self.corso_di_studio = corso_di_studio

    """Posso permettermi di cambiare dei metodi inportati dalla genitore, sovrascrivendoli OVERWRITING"""
    def scheda_personale(self):
        scheda = f"""
        Profilo:{Studente.profilo}
        Corso di Studi:{self.corso_di_studio}"""

        return super().scheda_personale() + scheda #Overwriting classe super

    def cambio_corso(self,corso):
        """Creo una funzione per cambiare corso di studi"""
        self.corso_di_studio = corso
        print("Corso aggiornato")

class Insegnante(Persona):
    profilo = "Insegnante"
    def __init__(self, nome,cognome,eta, residenza,materia=None):
        """Richiamo super per far si che vengano prese dalla genitore nome,cognome,eta,residenza
        Python andrà a controllare la presenza di un metodo costruttore dalla classe genitore per gestire gli altri"""
        super().__init__(nome,cognome,eta, residenza)
        if materia is None:
            self.materia = []
        else:
            self.materia = materia

    def aggiungi_materia(self,nuova_materia):
        if nuova_materia not in self.materia:
            self.materia.append(nuova_materia)
        print("Elenco materie aggiornato!")


    def scheda_personale(self):
        scheda = f"""
        Profilo:{Insegnante.profilo}
        Materie Insegnate:{self.materia}"""

        return super().scheda_personale() + scheda #Overwriting classe super

"""
Creo un soggetto da referenziare (studente_uno)
"""

studente_uno = Studente("Edoardo","Zucca","28","Via archimede 15","Python")
insegnante_uno = Insegnante("Mario","Rossi","38","Via le mani 6",["Informatica","Statistica"])


insegnante_uno.modifica_scheda()

print(studente_uno.scheda_personale())
print(insegnante_uno.scheda_personale())

insegnante_uno.aggiungi_materia("Filosofia")
print(insegnante_uno.scheda_personale())

