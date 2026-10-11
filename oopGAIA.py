# Definizione della classe Studente
from other_data_structures import lista_studenti


class Studente:
    # Attributi
    # matricola = 0
    # nome = ""
    # cognome = ""

    # Costruttore, funzione standard per inizializzare l'oggetto
    def __init__(self, matricola, nome, cognome):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome

    # Altre funzioni della classe Studente
    def sostiene_esame(self):
        print("Sostiene esame")

    def si_unisce_a_gruppo_studentesco(self):
        print("Si unisce a gruppo studentesco")



# Creo un oggetto/istanza della classe Studente

s = Studente(123456, "Mario", "Rossi")
               # Sto creando uno studente ed inizializzandolo
               # Python chiama la funzione __init__()
#print(s)
#acedo alla pancia dell'oggetto per leggere o scrivere i suoi contenuti
print(f"{s.matricola} - {s.nome} - {s.cognome}")
s.sostiene_esame()  #posso invocare su quello studente Mario Rossi la funz che sereve per fargli sostenere l'esame
                    #i dati e le operazioni sui dati sono incapsulati nell'oggeto!!!

#vogliamo creare un "contenitore" di studenti, in questo caso una lista
lista_studenti = []
lista_studenti.append(s)
lista_studenti.append(Studente(67890, "Gianni", "Verdi"))

#per la lunghezza della lista len
#n = len(lista_studenti)
#print(n)

#ora scandiamo e poi stampiamo la lista di studenti con for in
for studente in lista_studenti:
    print(studente.matricola, studente.nome, studente.cognome)



