#Temainnlevering
#INFO132 obligatorisk innleveringsoppgave 3
#Oppgave 2

#Tar i mot alder og antall år i Tulleby
alder = int(input("Oppgi alder:"))
lengde = int(input("Hvor lenge har du bodd i tulleby?"))

#Ordfører minst 30 år gammel og 9 år i Tulleby
if(alder>= 30 and lengde >=9):
    print("Du kan bli ordfører eller sitte i bystyret")
#Bystyret minst 25 år gammel og 5 år i Tulleby
elif(alder>= 25 and lengde >=5):
    alder_diff = 30-alder
    lengde_diff = 9 - lengde
    print("Du kan sitte i bystyret")
    if(alder_diff<lengde_diff):
        print("Prøv igjen om", lengde_diff, "år for å bli ordfører")
    else:
        print("Prøv igjen om", alder_diff, "år for å bli ordfører")
else:
    alder_diff = 25-alder
    lengde_diff = 5 - lengde    
    if(alder_diff<lengde_diff):
        print("Du er ikke kvalifisert enda, prøv ogjen om", lengde_diff, "år") 
    else:
        print("Du er ikke kvalifisert enda, prøv ogjen om", alder_diff, "år")

