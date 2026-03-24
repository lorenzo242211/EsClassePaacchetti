import flet as ft
from IU.controllerPerAggiornareInterfacciaGrafica import Controller
from IU.visualizzaInterfacciaGraficaOggettiGrafici import View


def main(pagina: ft.Page): #metodo per far parlare main view e controller
    v = View(pagina)
    c = Controller(v)
    v.set_controller(c)
    v.carica_interfaccia() #stampa tutto con pulsanti eccetera per gestire l'interfaccia





ft.app(target=main)