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

class Officina:
    def __init__(self, nome:str, tickets:list[TicketRiparazione]):
        self.nome = nome
        self.tickets = tickets

    def aggiungi_ticket(self, ticket:TicketRiparazione):
        self.tickets.append(ticket)

    def chiudi_ticket(self, id_ticket):
        trovato = False
        for ticket in self.tickets:
            id = ticket.get_id_ticket()
            if id_ticket == id:
                self.tickets.remove(ticket)
                print("Il ticket", id_ticket, "è stato chiuso correttamente.")
                trovato = True
        if not trovato:
            print("Il ticket", id_ticket, "non è tra quelli aperti.")

    def stampa_ticket_aperti(self):
        print("I ticket aperti sono:")
        nessuno = True
        for ticket in self.tickets:
            if ticket.get_stato() == "aperto":
                nessuno = False
                print("ID", ticket.get_id(), "tipo di elettrodomestico:", ticket.get_elettrodomestico(), "stato:", ticket.get_stato())
        if nessuno:
            print("Non c'è nessun ticket aperto.")


    def totale_preventivi(self):
        pass


