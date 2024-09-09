#Temainnlevering
#INFO132 obligatorisk innleveringsoppgave 2
#Oppgave 3

#Importer math library
import math

#Angi pertsoner og plass
personer = int(input("Hvor mange personer skal du hente?"))
plasser = int(input("Hvor mange passasjerer har du plass til i bilen?"))
turer = personer/plasser
print(math.ceil(turer))
