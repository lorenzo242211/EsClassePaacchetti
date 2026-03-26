import flet as ft
from mysql.opentelemetry.importlib_metadata import pass_none


class View:
    def __init__(self, p):
        self._controller = None #non necessario ma buona norma
        self._pagina = p
        self._pagina.title = "TdP 2026 - Software prova gestionale"
        self._pagina.horizontal_aligment = ft.MainAxisAlignment.CENTER
        self._pagina.theme_mode = ft.ThemeMode.LIGHT
        self.aggiorna_pagina()

    def carica_interfaccia(self): #controlliamo dal file gestionale.gestoreOrdini di cosa abbiamo bisogno, cosa dobbiamo importare
        #cosa mostrare: 3 text field per def prodotto, 3 per il cliente, 3-4 pulsanti (richiama metodi) e finestra dove scrivere!

        #Prodotto
        self._txtInNomeP = ft.TextField(label = "Nome prodotto", width = 200) #larghezza massima di 200px
        self._txtInPrezzoP = ft.TextField(label = "Prezzo", width = 200)
        self._txtInQuantitaP = ft.TextField(label = "Quantità", width = 200)
        row1 = ft.Row(controls=[self._txtInNomeP, self._txtInPrezzoP, self._txtInQuantitaP], alignment=ft.MainAxisAlignment.CENTER)
        #qua sopra ho applicato tutte funzioni della libreria flet utili per visualizzare pulitamente

        # Cliente
        self._txtInNomeC = ft.TextField(label="Nome cliente", width=200)  # larghezza massima di 200px
        self._txtInMailC = ft.TextField(label="Mail", width=200)
        self._txtInCategoriaC = ft.TextField(label="Categoria", width=200)
        row2 = ft.Row(controls=[self._txtInNomeC, self._txtInMailC, self._txtInCategoriaC],
                      alignment=ft.MainAxisAlignment.CENTER)
        #qua sopra ho applicato tutte funzioni della libreria flet utili per visualizzare pulitamente

        #Bottoni

        self._btnAdd = ft.ElevatedButton(text = "Aggiungi ordine", on_click = self._controller.add_ordine, width=200)
        self._btnGestisciOrdine = ft.ElevatedButton(text = "Gestisci ordine", on_click = self._controller.gestisci_ordine, width=200)
        self._btnGestisciTuttiOrdini = ft.ElevatedButton(text = "Gestisci tutti gli ordini", on_click = self._controller.gestisci_tutti_ordini, width=200)
        self._btnStampaInfo = ft.ElevatedButton(text="Stampa sommario",on_click=self._controller.stampa_sommario, width=200)
        #on click è il metodo associato al pulsante, cioè quello che fa, in questo caso è richiamato da controller
        row3 = ft.Row(controls = [self._btnAdd, self._btnGestisciOrdine, self._btnGestisciTuttiOrdini, self._btnStampaInfo],alignment=ft.MainAxisAlignment.CENTER)

        #aggiungo finestra di testo per comunicare con l'utente, list view! --> oggetto di lista di controlli uno dopo l'altro
        self._lvOut = ft.ListView(expand=True)


        self._pagina.add(row1, row2, row3,self._lvOut) #aggiungo il contenuto alla pagina


    def set_controller(self, c):
        self._controller = c #in phyton si puo creare un attributo anche dopo non è necessario dichiararlo nel costruttore

    def aggiorna_pagina(self):
        self._pagina.update()