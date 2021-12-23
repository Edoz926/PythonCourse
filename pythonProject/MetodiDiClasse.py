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

    @classmethod
    def from_string(cls,stringa_persona,*args):
        """
        Primo parametro da passare sarà LA CLASSE STESSA, metodi di classe legati alla classe e non alle istanze
        Per farsi che python passi la classe invece che l'istanza dobbiamo prima specificare un decoratore:
        @classmethod: decoratore per i metodi di classe
        Nome del costruttore alternativo molto specifico per lo scopo e l'ingestione
        """
        nome,cognome,età,residenza = stringa_persona.split('-')
        return cls(nome,cognome,età,residenza,*args)

    #Creo il metodo di classe
    @classmethod
    def occupazione(cls):
        if cls.__name__ == "Studente":
            return "Studente"
        else:
            return "Insegnante"

    @staticmethod
    def info_prog():
        info = """
        Nome: Persona
        Creato da: Edo
        Lezioni di Pymike
        """
        return  info

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
Metodo alternativo al costruttore init, che permetta di prelevare da una stringa passata i campi che servono
Alla decodifica e all'inserimento delle informazioni per le classi
"""

iron_man ="Tony-Stark-40-via archimede 15"
mark = "Mark-Zuck-33-California"
persona1 = Persona.from_string(iron_man)
print(persona1.scheda_personale())

"""
Chiaramente ereditaano tutte le classi figlie queste opzioni
Se passiamo il parametro in più delle materie, attenzione!!! era gestito dal suo __init__, non da quello ereditato
Dovrò passare *args in più nel costruttore: notazione specifica per dire che possono esserci zero o più paramentri
aggiuntivi da passare, alcune sottoclassi possono avere più parametri che la classe genitore non ha
"""
ins1 = Insegnante.from_string(iron_man,'Ingegneria')
stud1 = Studente.from_string(mark,"SEO")
print(ins1.scheda_personale())
print(stud1.scheda_personale())

"""
Altra cosa interessante: metodo che può cambiare dipendentemente dalla classe che lo sta chiamando
Modo per capire se studente o insegnante senza passare dalla scheda personale
"""
print(ins1.occupazione())

"""
Metodi statici con il decoratore appropriato: @staticmethod
Richiamabili direttamente dalla classe, senza aver instanziato nulla
"""
print(Persona.info_prog())
