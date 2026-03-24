import flet as ft

from gestionale.gestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self, v):
        self._view = v
    def add_ordine(self, evento): #l'evento serve per registrare il momento in cui si verifica l'eccezione nei metodoi in cui uso viewer
        #Prodotto
        nomeP = self._view._txtInNomeP.value
        if nomeP == "":
            self._view._lvOut.controls.append(
                ft.Text(value="Nome prodotto non può essere vuoto!", color="red"))
            self._view.aggiorna_pagina()
            return
        self._modello = GestoreOrdini()
        try:
            prezzoP = float(self._view._txtInPrezzoP.value)
        except ValueError: #teniamo conto dell'eccezione in cui l'utente inserisca valore alfa anzichè solo numeri ecc
            self._view._lvOut.controls.append(ft.Text(value = "Dio merda devi mettere solo numeri cazzo di dio non lettere nel Prezzo!" , color="red"))
            self._view.aggiorna_pagina()
            return

        try:
            quantitaP = int(self._view._txtInQuantitaP.value)
        except ValueError:#intercetta l'errore scatenato dal cast int
            self._view._lvOut.controls.append(
                ft.Text(value="Dio merda devi mettere solo numeri cazzo ed Interi di dio non lettere o float nella QUANTITA'!", color="orange"))
            self._view.aggiorna_pagina()
            return
        #Cliente
        #nome mail categoria
        nomeC = self._view._txtInNomeC.value
        if nomeC == "":
            self._view._lvOut.controls.append(
                ft.Text(value="Nome cliente non può essere vuoto!", color="red"))
            self._view.aggiorna_pagina()
            return
        mailC = self._view._txtInMailC.value
        if mailC == "":
            self._view._lvOut.controls.append(
                ft.Text(value="Email cliente non può essere vuoto!", color="red"))
            self._view.aggiorna_pagina()
            return
        categoria = self._view._txtInCategoriaC.value
        if categoria == "":
            self._view._lvOut.controls.append(
                ft.Text(value="Categoria non può essere vuoto!", color="red"))
            self._view.aggiorna_pagina()
            return

        ordine = self._modello.crea_ordine(nomeP, prezzoP, quantitaP, nomeC, mailC, categoria)
        self._modello.add_ordine(ordine) #lo aggiungo sfruttando l'apposita classe
        #finito questo pacchetto di ordine + cliente pulisco tutta l'interfaccia se ok

        #pulisco prodotto
        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzoP.value = ""
        self._view._txtInQuantitaP.value = ""
        #pulisco cliente
        self._view._txtInNomeC.value = ""
        self._view._txtInMailC.value = ""
        self._view._txtInCategoriaC.value = ""

        self._view._lvOut.controls.append(ft.Text(value = "Ordine inserito correttamente! Cazzo di bolly", color="green"))
        self._view._lvOut.controls.append(ft.Text(ordine.riepilogo())) #apposito comando che stampa i valori dell ordine già formattati


        self._view.aggiorna_pagina()


        #crea metodo per aggiungere e registrare questi 6 parametri dentro l oggetto ordine della classe gestoreOrdini il quale richiamerò qua
    #chiamandolo crea ordine(6 parametri)


    def gestisci_ordine(self, e):
        pass
    def gestisci_tutti_ordini(self, e):
        pass
    def stampa_sommario(self, e):
        pass