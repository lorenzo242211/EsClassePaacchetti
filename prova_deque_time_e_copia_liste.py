from gestionale.core.prodotti import ProdottoRecord
import copy

p1 = ProdottoRecord("Portatile" , 1200.0)
p2 = ProdottoRecord ("S26 Ultra" , 1500.55)
p3 = ProdottoRecord ("Mouse" , 20.0)

carrello = [p1, p2, p3, ProdottoRecord("iPhone 17 Pro", 1299)]
print("Prodotti nel carello:")
for i, p in enumerate(carrello):
    print(f"{i+1}) {p.name}: {p.prezzo_unitario} $")
carrello.sort(key=lambda x: x.prezzo_unitario) #guarda nelle altre classi questi metodi
totale = sum([p.prezzo_unitario for p in carrello])
print(f" il totale del carrello è: {totale} $")
#lista.extend aggiungi lista/iterable a fine di una lista già esistente, append aggiunge un elemento alla fine
#insert prevede inserimento di due argomenti, 1 indice al quale inserire nella lista e oggetto stesso
carrello.pop(2) #rimuove terzo oggetto
carrello.remove(p1) #rimuove prima occorrenza di p1
carrello.clear() #svuota lista
carrello = [p1, p2, p3, ProdottoRecord("iPhone 17 Pro", 1299)]
carrello_copia = carrello.copy() #è una copia degli oggetti, se modifico p1 si modifica in entrambi
carello_copia2 = copy.deepcopy(carrello) #crea copia anche del contenuto della lista

esempioTupla = (3, p2) #è immutabile, posso metterla nella lista
t2 = (2, p1)
t3 = (10, p3)
listaTuple = (esempioTupla, t2, t3)
print(listaTuple)
insieme = {t2, t3, esempioTupla, t3}


#proviamo deque! e time per cronometro tempo
print("\n\n\nFunzione deque e gestione cronometro\n\n\n")
import time
from collections import deque
import flet as ft

lista = []
t = time.time()
for i in range(100000):
    lista.append(i) #creo apposta lista molto grande per fare i miei test sulla velocità
print("tempo impiegato per aggiungerli alla lista")
print(time.time() - t) #cronometro che va avanti sempre e tolgo il tempo passato
t = time.time()
for i in range(100000):
    lista.pop(0)
print("tempo impiegato per rimuverli dalla lista")
print(time.time() - t) #cronometro che va avanti sempre e tolgo il tempo passato

d = deque()
t = time.time()
for i in range(100000):
    d.append(i)
print("tempo impiegato per aggiungerli al deque")
print(time.time() - t) #cronometro che va avanti sempre e tolgo il tempo passato

t = time.time()
for i in range(100000):
    d.popleft() #eseguibile e possibile solo su deque, performance molto superiori, il pop su lista richiede spostamento di tutti gli altri elementi, ecco perchè questa differenza di performance
print("tempo impiegato per toglierli al deque")
print(time.time() - t) #cronometro che va avanti sempre e tolgo il tempo passato
print("notiamo come deque è piu veloce!")


def main(pagina: ft.Page):
    testo = ft.Text(value = "DIOLADROCANEBOCCHINO porco bolly morto", size = 24, color = "yellow")
    pagina.controls.append(testo)
    pagina.update()

    testo2 = ft.Text(value = "sottotitolo inserito con page.add(testo2) che fa direttamente append + update", size = 19, color = "cyan")
    pagina.add(testo2)

    #colonna1 = ft.Row(controls : [ft.Text(value = "Colonna1"), ft.Text(value = "Colonna2"), ft.Text(value = "Colonna3")])
    #page.add(colonna1)

ft.app(target = main)









