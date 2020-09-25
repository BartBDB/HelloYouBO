print("Hello You!, ik ben Bart.")
print("Wie ben jij?")
Naam = input( )
print("Hello " + Naam + ", fijn om jou te zien.")
print("Ik ben dit jaar nieuw op het Mediacollege, en door middel van een paar vragen kan jij mij beter leren kennen.")
print("Met welke taal heb ik al ervaring?")
print("A - Lua")
print("B - Python")
print("C - C#")
Antwoord2 = input( )
if Antwoord2 == ("A") or Antwoord2 == ("a"):
    print("Jazeker! Ik heb Lua scripts geschreven voor de game Sonic Robo Blast 2, en ik heb zelfs een script in de Releases sectie gekregen.")
elif Antwoord2 == ("B") or Antwoord2 == ("b"):
    print("Al lijkt Python veel op Lua, de taal waar ik wel mee heb gewerkt, ik heb nooit met Python gewerkt.") 
elif Antwoord2 == ("C") or Antwoord2 == ("c"):
    print("Als de # er niet stond, was het correct geweest. Maar omdat dat geen antwoord is, is dit dus fout. Ik heb ervaring met Lua.")
print("Lua dus, die taal heeft mij in programmeren gekregen. Stuk minder irritant dan Python, dat is zeker. Vooral met indenting.")

print("Op welke middelbare school zat ik?")
print("A - Veenlanden College")
print("B - Alkwin Kollege")
print("C - Thamen")
Antwoord1 = input( )
if Antwoord1 == ("A") or Antwoord1 == ("a"):
    print("Deze school is dichterbij mijn huis, maar ik ben hier niet heengegaan.")
elif Antwoord1 == ("B") or Antwoord1 == ("b"):
    print("Correct!")
elif Antwoord1 == ("C") or Antwoord1 == ("c"):
    print("Bijna! De school waar ik op zat staat aan de overkant van deze school.")
print("Dit betekent dus dat ik een HAVO diploma heb (nauwelijks maar toch!)")

if Antwoord1 == ("B") or Antwoord1 == ("b"):
    print("Je weet dus al dat ik naar het Alkwin Kollege ben gegaan, mooi.")
    print("Hoe lang deed ik daar over mijn HAVO diploma?")
    print("A - 4 jaar")
    print("B - 5 jaar")
    print("C - 6 jaar")
    Antwoord1half = input( )
    if Antwoord1half == ("A") or Antwoord1half == ("a"):
        print("Ik heb geen klas overgeslagen in de HAVO. Het zou alsnog geen 4 jaar zijn.")
    elif Antwoord1half == ("B") or Antwoord1half == ("b"):
        print("Ik ben een keer blijven zitten in de HAVO, dus geen 5 jaar.")
    elif Antwoord1half == ("C") or Antwoord1half == ("c"):
        print("Top!")

if Antwoord1 == ("A") or Antwoord1 == ("a") or Antwoord1 == ("C") or Antwoord1 == ("c"):
    print("Ik heb op het Alkwin Kollege gezeten en de HAVO gedaan.")
    print("Misschien moet ik nog een vraag over mijn school stellen.")
    print("Hoe lang duurde het voor mij om naar school te fietsen?")
    print("A - 45 minuten")
    print("B - 15 minuten")
    print("C - 30 minuten")
    Antwoord2half = input( )
    if Antwoord2half == ("A") or Antwoord2half == ("a"):
        print("Zo lang duurde het gelukkig niet.")
    elif Antwoord2half == ("B") or Antwoord2half == ("b"):
        print("Ik had wel heel snel moeten fietsen om dat te redden, aangezien ik in Mijdrecht woon.")
    elif Antwoord2half == ("C") or Antwoord2half == ("c"):
        print("30 minuten ja, was best wel lekker om die afstand te fietsen.")

print("Laatste vraag, home stretch! Hoe lang wou ik al iets in de richting Software Development doen?")
print("A - 1 jaar")
print("B - 2 jaar")
print("C - 3 jaar")
Antwoord3 = input( )
if Antwoord3 == ("A") or Antwoord3 == ("a"):
    print("Mijn middelbare school startte vroeg met richtingen kiezen (ze starten al in de 4de). Omdat ik een jaar was blijven zitten, was het dus 3 jaar geleden, niet 1.")
elif Antwoord3 == ("B") or Antwoord3 == ("b"):
    print("Dichtbij, maar ik was een jaar blijven zitten. Mijn oude school startte met richtingen kiezen in de 4de, dus was het 3 jaar terug.") 
elif Antwoord3 == ("C") or Antwoord3 == ("c"):
    print("Correct! Mijn oude school startte vroeg met richtingen kiezen, al vanaf de 4de. Omdat ik een jaar was blijven zitten, was het dus 3 jaar terug.")