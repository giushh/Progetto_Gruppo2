"""
Concetti obbligatori: incapsulamento, ereditarietà, polimorfismo, uso di type() per controllare gli oggetti e metodi "variatici" (con parametri variabili).
Stai progettando il software di base per un'officina che si occupa di riparare elettrodomestici 
(lavatrici, frigoriferi, forni, ecc.). 
Il programma dovrà modellare gli elettrodomestici, i ticket di riparazione e alcune operazioni dell'officina, usando la programmazione ad oggetti.

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
                self.__anno_acquisto = anno_corrente
        else:
            self.__anno_acquisto = anno_corrente


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
