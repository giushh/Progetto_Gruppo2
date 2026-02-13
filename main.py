"""
Concetti obbligatori: incapsulamento, ereditarietà, polimorfismo, uso di type() per controllare gli oggetti e metodi "variatici" (con parametri variabili).
Stai progettando il software di base per un'officina che si occupa di riparare elettrodomestici (lavatrici, frigoriferi, forni, ecc.). Il programma dovrà modellare gli elettrodomestici, i ticket di riparazione e alcune operazioni dell'officina, usando la programmazione ad oggetti.

1. Classe base: Elettrodomestico
    Crea una classe base chiamata Elettrodomestico che rappresenti un elettrodomestico generico. Attributi (incapsulati, cioè privati):
    __marca (stringa)

    __modello (stringa)

    __anno_acquisto (intero)

    __guasto (stringa che descrive il problema principale)
    Metodi:
    Costruttore __init__(self, marca, modello, anno_acquisto, guasto)
    Getter e setter per tutti gli attributi, con eventuali controlli minimi (es. l'anno non può essere nel futuro).
    descrizione(self): restituisce una stringa con marca, modello, anno e guasto.
    stima_costo_base(self): restituisce un valore numerico generico (es. costo base di diagnosi).
    Regola 1 - Incapsulamento: tutti gli attributi devono essere privati (__attributo) e accessibili solo tramite getter/setter.

2. Classi derivate (Ereditarietà + Polimorfismo)
    Crea almeno tre sottoclassi di Elettrodomestico:
    Lavatrice
    Attributi aggiuntivi: capacita_kg (intero), giri_centrifuga (intero).
    Override di stima_costo_base(self): la lavatrice ha un costo base diverso (ad esempio, maggiorato se la capacità è elevata).
    Frigorifero
    Attributi aggiuntivi: litri (intero), ha_freezer (booleano).
    Override di stima_costo_base(self): il costo può cambiare se ha il freezer o se i litri superano una certa soglia.
    Forno
    Attributi aggiuntivi: tipo_alimentazione (stringa: "elettrico", "gas"), ha_ventilato (booleano).
    Override di stima_costo_base(self): il costo può cambiare in base al tipo di alimentazione e alla presenza della funzione ventilata.
    Regola 2 - Ereditarietà: tutte le classi derivate devono usare Elettrodomestico come classe base ed ereditare i suoi attributi tramite super() nel costruttore. Regola 3 - Polimorfismo: tutte le sottoclassi devono fornire la propria versione di stima_costo_base(self), in modo che la chiamata a questo metodo su una lista mista di oggetti (Lavatrice, Frigorifero, Forno) produca risultati diversi a seconda del tipo.

3. Classe TicketRiparazione
    Crea una classe TicketRiparazione che rappresenta un ticket aperto in officina. Attributi (incapsulati):
    __id_ticket (intero o stringa univoca)
    __elettrodomestico (un oggetto di tipo Elettrodomestico o sottoclasse)
    __stato (stringa: "aperto", "in lavorazione", "chiusa")
    __note (lista di stringhe, inizialmente vuota)
    Metodi:
    Costruttore __init__(self, id_ticket, elettrodomestico)
    Getter e setter necessari (ad esempio per stato e note).
    aggiungi_nota(self, testo) per aggiungere una nota.
    *calcola_preventivo(self, voci_extra) -> metodo variadico:
    usa elettrodomestico.stima_costo_base() come costo di partenza
    somma tutte le voci extra passate come parametri (*voci_extra)
    restituisce il totale. Nota: questo metodo deve funzionare con qualsiasi sottoclasse di Elettrodomestico
    (polimorfismo sul metodo stima_costo_base).

4. Classe Officina
    Crea una classe Officina che gestisce i ticket e gli elettrodomestici. Attributi:
    nome (stringa)
    tickets (lista di oggetti TicketRiparazione)
    Metodi:
    aggiungi_ticket(self, ticket)
    chiudi_ticket(self, id_ticket)
    stampa_ticket_aperti(self): mostra ID, tipo di elettrodomestico e stato.
    totale_preventivi(self): somma i preventivi di tutti i ticket.

5. Uso di type() e controllo degli oggetti
    All'interno della classe Officina (o in una funzione separata) implementa un metodo, ad esempio:
    statistiche_per_tipo(self)
    Questo metodo deve:
    Iterare su tutti i ticket.
    Usare type() (oppure isinstance()) per capire se l'elettrodomestico associato al ticket è una Lavatrice, un Frigorifero o un Forno.
    Contare quanti ticket ci sono per ciascuna sottoclasse.
    Stampare un piccolo report, per esempio:
    "Numero di lavatrici in riparazione: X"
    "Numero di frigoriferi in riparazione: Y"
    "Numero di forni in riparazione: Z"

Requisito: il metodo deve utilizzare type() (o, come variante consigliata, isinstance()) 
per differenziare in base al tipo reale degli oggetti.
"""

# Ilaria: classi Elettrodomestico e derivate

from __future__ import annotations
from datetime import date

class Elettrodomestico:

    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str):
        self.set_marca(marca)
        self.set_modello(modello)
        self.set_anno_acquisto(anno_acquisto)
        self.set_guasto(guasto)

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca: str):
        if isinstance(marca, str) and marca.strip() != "":
            self.__marca = marca
        else:
            self.__marca = "Sconosciuta"

    def get_modello(self):
        return self.__modello

    def set_modello(self, modello: str):
        if isinstance(modello, str) and modello.strip() != "":
            self.__modello = modello
        else:
            self.__modello = "Sconosciuto"

    def get_anno_acquisto(self):
        return self.__anno_acquisto

    def set_anno_acquisto(self, anno_acquisto: int):
        anno_corrente = date.today().year
        if type(anno_acquisto) == int:
            if anno_acquisto >= 1900 and anno_acquisto <= anno_corrente:
                self.__anno_acquisto = anno_acquisto
            else:
                # self.__anno_acquisto = anno_corrente
                print("Anno non valido.")
        else:
            # self.__anno_acquisto = anno_corrente
            print("Anno non valido.")


    def get_guasto(self):
        return self.__guasto

    def set_guasto(self, guasto: str):
        if isinstance(guasto, str) and guasto.strip() != "":
            self.__guasto = guasto
        else:
            self.__guasto = "Non specificato"

    def descrizione(self):
        return f"{self.get_marca()} {self.get_modello()} ({self.get_anno_acquisto()}) - Guasto: {self.get_guasto()}"

    def stima_costo_base(self):
        return 30.0


class Lavatrice(Elettrodomestico):

    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, capacita_kg: int, giri_centrifuga: int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.set_capacita_kg(capacita_kg)
        self.set_giri_centrifuga(giri_centrifuga)

    def get_capacita_kg(self):
        return self.__capacita_kg

    def set_capacita_kg(self, capacita_kg: int):
        if isinstance(capacita_kg, int) and 1 <= capacita_kg <= 20:
            self.__capacita_kg = capacita_kg
        else:
            self.__capacita_kg = 7

    def get_giri_centrifuga(self):
        return self.__giri_centrifuga

    def set_giri_centrifuga(self, giri_centrifuga: int):
        if isinstance(giri_centrifuga, int) and 0 <= giri_centrifuga <= 2000:
            self.__giri_centrifuga = giri_centrifuga
        else:
            self.__giri_centrifuga = 1000

    def descrizione(self):
        base = super().descrizione()
        return f"{base} | Capacità: {self.get_capacita_kg()}kg, Giri: {self.get_giri_centrifuga()}"

    def stima_costo_base(self):
        costo = 35.0
        if self.get_capacita_kg() >= 9:
            costo += 10.0
        if self.get_giri_centrifuga() >= 1400:
            costo += 5.0
        return costo


class Frigorifero(Elettrodomestico):

    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, litri: int, ha_freezer: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.set_litri(litri)
        self.set_ha_freezer(ha_freezer)

    def get_litri(self):
        return self.__litri

    def set_litri(self, litri: int):
        if isinstance(litri, int) and 50 <= litri <= 800:
            self.__litri = litri
        else:
            self.__litri = 250

    def get_ha_freezer(self):
        return self.__ha_freezer

    def set_ha_freezer(self, ha_freezer: bool):
        self.__ha_freezer = bool(ha_freezer)

    def descrizione(self):
        base = super().descrizione()
        freezer = "sì" if self.get_ha_freezer() else "no"
        return f"{base} | Litri: {self.get_litri()}L, Freezer: {freezer}"

    def stima_costo_base(self):
        costo = 40.0
        if self.get_ha_freezer():
            costo += 10.0
        if self.get_litri() >= 350:
            costo += 10.0
        return costo


class Forno(Elettrodomestico):

    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, tipo_alimentazione: str, ha_ventilato: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.set_tipo_alimentazione(tipo_alimentazione)
        self.set_ha_ventilato(ha_ventilato)

    def get_tipo_alimentazione(self):
        return self.__tipo_alimentazione

    def set_tipo_alimentazione(self, tipo_alimentazione: str):
        if isinstance(tipo_alimentazione, str):
            t = tipo_alimentazione.strip().lower()
            if t in ["elettrico", "gas"]:
                self.__tipo_alimentazione = t
                return
        self.__tipo_alimentazione = "elettrico"

    def get_ha_ventilato(self):
        return self.__ha_ventilato

    def set_ha_ventilato(self, ha_ventilato: bool):
        self.__ha_ventilato = bool(ha_ventilato)

    def descrizione(self):
        base = super().descrizione()
        ventilato = "sì" if self.get_ha_ventilato() else "no"
        return f"{base} | Alimentazione: {self.get_tipo_alimentazione()}, Ventilato: {ventilato}"

    def stima_costo_base(self):
        costo = 30.0
        if self.get_tipo_alimentazione() == "gas":
            costo += 10.0
        if self.get_ha_ventilato():
            costo += 5.0
        return costo
    
    
# Veronica: classe Officina e punto 5

class Officina:
    def __init__(self, nome: str, tickets: list[TicketRiparazione]):
        self.nome = nome
        self.tickets = tickets

    def aggiungi_ticket(self, ticket: TicketRiparazione):
        self.tickets.append(ticket)

    def chiudi_ticket(self, id_ticket):
        trovato = False
        for ticket in self.tickets:
            id = ticket.get_id_ticket()
            if id_ticket == id:
                self.tickets.remove(ticket)
                print("Il ticket", id_ticket, "è stato chiuso correttamente.")
                trovato = True
                break
                
        if not trovato:
            print("Il ticket", id_ticket, "non è tra quelli aperti.")

    def stampa_ticket_aperti(self):
        print("I ticket aperti sono:")
        nessuno = True
        for ticket in self.tickets:
            if ticket.get_stato() == "aperto":
                nessuno = False
                elettro = ticket.get_elettrodomestico()
                print("ID", ticket.get_id_ticket(), "tipo di elettrodomestico:", type(elettro).__name__, "stato:", ticket.get_stato())
        if nessuno:
            print("Non c'è nessun ticket aperto.")


    def totale_preventivi(self):
        totale = 0.0
        for ticket in self.tickets:
            totale = totale + ticket.calcola_preventivo()
        return totale
    
    def statistiche_per_tipo(self):
        num_lavatrici = 0
        num_frigoriferi = 0
        num_forni = 0

        for ticket in self.tickets:
            elettro = ticket.get_elettrodomestico()

            if type(elettro) == Lavatrice:
                num_lavatrici += 1
            elif type(elettro) == Frigorifero:
                num_frigoriferi += 1
            elif type(elettro) == Forno:
                num_forni += 1

        print("Numero di lavatrici in riparazione:", num_lavatrici)
        print("Numero di frigoriferi in riparazione:", num_frigoriferi)
        print("Numero di forni in riparazione:", num_forni)
        
        
# Valerio: classe TicketRistorazione 

# Attributi privati (Incapsulamento). Attributi inizianti per __ quindi nessuno può modificarli dall'esterno.
class TicketRiparazione:
    def __init__(self, id_ticket, elettrodomestico):    # Costruttore __init__ per legare il ticket ad un elettrodomestico specifico.
        self.__id_ticket = id_ticket                    # Numero identificativo della riparazione.
        self.__elettrodomestico = elettrodomestico      # Salva l'intero oggetto (Lavatrice, Forno o Frigo) che "arriva" dagli "Elettrodomestici".
        self.__stato = "aperto"                         # Stato di base "aperto" (?)
        self.__note = []                                # Lista che serve a tenere traccia di cosa dicono i tecnici durante il lavoro (?)

# Metodi Getter e Setter per fornire le chiavi degli attributi per leggerli o modificarli.
    def get_id_ticket(self):
        return self.__id_ticket     # Per sapere qual è lo stato del ticket.
    def get_stato(self):
        return self.__stato
    def set_stato(self, s):         # Per cambiare lo stato (ad esempio da "aperto" a "chiuso" o viceversa).
        self.__stato = s
    def get_elettrodomestico(self): # Per sapere di che marca è l'elettrodomestico.
        return self.__elettrodomestico
    
    def aggiungi_nota(self, testo):
        self.__note.append(testo)

    def calcola_preventivo(self, *voci_extra):              # * Permette all'utente di inserire quanti numeri vuole, Python li raggruppa tutti in una tulpa che scorre con il ciclo for.
        # Polimorfismo: chiama il metodo corretto in base al tipo reale. Chiama stima_costo_base() dalla sottoclasse.
        totale = self.__elettrodomestico.stima_costo_base() # stima_costo_base dalla Classe base "Elettrodomestici".
        for spesa in voci_extra:
            totale += spesa
        return totale




# ******************* MAIN

if __name__ == "__main__":

    officina = Officina("Officina Centrale", [])
    stop = False

    while not stop:
        
        scelta = input("\nPuoi:"
                       "\n1. Aggiungere un ticket"
                       "\n2. Mostrare ticket aperti"
                       "\n3. Chiudere un ticket"
                       "\n4. Totale preventivi"
                       "\n5. Statistiche per tipo"
                       "\n6. Uscita"
                       "\nIndica il numero corrispondente \n> ")
        
        match scelta:
            
            case "1":
                tipo = input("Tipo elettrodomestico (1=Lavatrice, 2=Frigorifero, 3=Forno): ")
                id_ticket = input("Inserisci ID ticket: ")
                marca = input("Marca: ")
                modello = input("Modello: ")
                anno = int(input("Anno acquisto: "))
                guasto = input("Descrizione guasto: ")
                
                
                               
                if tipo == "1":
                    capacita = int(input("Capacità kg: "))
                    giri = int(input("Giri centrifuga: "))
                    elettro = Lavatrice(marca, modello, anno, guasto, capacita, giri)
                
                elif tipo == "2":
                    litri = int(input("Litri: "))
                    freezer_input = input("Ha freezer? (si/no): ")
                    ha_freezer = True if freezer_input == "si" else False
                    elettro = Frigorifero(marca, modello, anno, guasto, litri, ha_freezer)
                
                elif tipo == "3":
                    alimentazione = input("Tipo alimentazione (elettrico/gas): ")
                    ventilato_input = input("Ha ventilato? (si/no): ")
                    ha_ventilato = True if ventilato_input == "si" else False
                    elettro = Forno(marca, modello, anno, guasto, alimentazione, ha_ventilato)
                
                else:
                    print("Tipo non valido.")
                    continue
                
                ticket = TicketRiparazione(id_ticket, elettro)
                officina.aggiungi_ticket(ticket)
                print("Ticket aggiunto correttamente.")
            
            
            case "2":
                officina.stampa_ticket_aperti()
            
            
            case "3":
                id_ticket = input("Inserisci ID del ticket da chiudere: ")
                officina.chiudi_ticket(id_ticket)
            
            
            case "4":
                totale = officina.totale_preventivi()
                print("Totale preventivi:", totale)
            
            
            case "5":
                officina.statistiche_per_tipo()
            
            
            case "6":
                print("\n-- Uscita")
                stop = True
            
            
            case _:
                print("\nComando non valido. \nRiprova.")
