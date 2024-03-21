# PROJEKT: Berechnung der Schneidparameter
# DATUM: 19.11.2023
# CODIERT VON: Kamil Sulewski

print("WILLKOMMEN BEI DEM SCHNEIDPARAMETERRECHNER")
print("__________________")
print("| 1 = FRÄSEN     |")
print("| 2 = BOHREN     |")
print("| 3 = PLANEN     |")
print("| 4 = DREHEN     |")
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
print("Geben Sie den Bearbeitungstyp ein, für den Sie die Parameter berechnen möchten ")
typ = input("1 für 2, 3 oder 4: ")


try:
    if int(typ) != 1 and int(typ) != 2 and int(typ) != 3 and int(typ) != 4:
        print("Hoppla... Sie haben falsch eingegeben...")
        print("Sie haben nur vier Optionen: |1|, |2|, |3|, |4|")
        print("LASSEN SIE UNS NOCHMAL VERSUCHEN")

    # FRÄSEN
    if int(typ) == 1:
        try:
            breite = 96
            print("-" * breite)
            print("| HILFSTABELLE FÜR VORBESTIMMTE PARAMETER, DIE FÜR VERSCHIEDENE MATERIALIEN BENÖTIGT WERDEN |")
            print("-" * breite)
            print("|          FRÄSEN - PARAMETER AUSGEWÄHLT FÜR WERKZEUGE AUS WOLFRAMKARBIT          |")
            print("*" * breite)
            print("| WL10(WK) | W(Profitool) | TZM(WK) | Mo(WK) | STAHL(HPC) | Ta (WK) |   ALUMINIUM   | KÜNSTLICH   |")
            print("-" * breite)
            print("|    80    |     55-60     |    90    |   110   |     110     |    65   |    300        |   50-200    |Vc [m/min]")
            print("-" * breite)
            print("|   0.02   |      0.04     |   0.03   |   0.03  |    0.05     |   0.03  |   0.06        |   0.1-0.5   |fz [mm]")
            print("*" * breite)

            vc = input("Geben Sie die Schnittgeschwindigkeit Vc in m/min ein: ")
            vc2 = vc.replace(",", ".")

            if 0 < float(vc2):
                durchmesser = input("Geben Sie den Werkzeugdurchmesser Ø in mm ein: ")
                durchmesser2 = durchmesser.replace(",", ".")
            elif 0 >= float(vc2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < float(durchmesser2):
                z = input("Geben Sie die Anzahl der Schneidzähne Z ein: ")
            elif 0 >= float(durchmesser2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < int(z):
                fz = input("Geben Sie den Vorschub pro Zahn fz ein: ")
                fz2 = fz.replace(",", ".")
            elif 0 >= int(z):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 >= float(fz2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < float(vc2) and 0 < float(durchmesser2) and 0 < float(fz2) and 0 < int(z):
                print()
                rpm = ((float(vc2)) * 1000) / ((float(durchmesser2)) * 3.1416)
                print("Berechnete U/min:", int(rpm), "U/min")
                vorschub = int(rpm) * float(fz2) * int(z)
                print("Berechnete Vorschubgeschwindigkeit:", int(vorschub), "mm/min")
        except ValueError:
            print("Hoppla.. Sie haben Daten in einem falschen Format eingegeben")
            print("Denken Sie daran: ")
            print("Alle Daten sollten nur in Zahlen angegeben werden")
            print("Die Anzahl der Zähne sollte in Ganzzahlen angegeben werden")
        except:
            print()

    # BOHREN
    if int(typ) == 2:
        try:
            breite = 93
            print("-" * breite)
            print("| HILFSTABELLE FÜR VORBESTIMMTE PARAMETER, DIE FÜR VERSCHIEDENE MATERIALIEN BENÖTIGT WERDEN |")
            print("-" * breite)
            print("|           BOHREN - PARAMETER AUSGEWÄHLT FÜR WERKZEUGE AUS WOLFRAMKARBIT             |")
            print("*" * breite)
            print("|   WL10   |      W10     |   TZM    |    Mo   |  STAHL   |    Ta    |   ALUMINIUM  | KÜNSTLICH   |")
            print("-" * breite)
            print("|    30    |      30      |    90    |    90   |   45     |    40    |   150        |   180       |Vc [m/min]")
            print("-" * breite)
            print("|   0.02   |     0.04     |   0.03   |   0.03  |   0.1    |   0.03   |   0.2        |   0.15      |f/U [mm]")
            print("*" * breite)

            vc = input("Geben Sie die Schnittgeschwindigkeit VC in m/min ein: ")
            vc2 = vc.replace(",", ".")

            if 0 < float(vc2):
                durchmesser = input("Geben Sie den Werkzeugdurchmesser Ø in mm ein: ")
                durchmesser2 = durchmesser.replace(",", ".")
            elif 0 >= float(vc2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < float(durchmesser2):
                fu = input("Geben Sie den Vorschub pro Umdrehung f/U in mm ein: ")
                fu2 = fu.replace(",", ".")
            elif 0 >= float(durchmesser2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 >= float(fu2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < float(vc2) and 0 < float(durchmesser2) and 0 < float(fu2):
                print()
                rpm = ((float(vc2)) * 1000) / ((float(durchmesser2)) * 3.1416)
                print("Berechnete U/min:", int(rpm), "U/min")
                vorschub = int(rpm) * float(fu2)
                print("Berechnete Vorschubgeschwindigkeit:", int(vorschub), "mm/min")
        except ValueError:
            print("Hoppla.. Sie haben Daten in einem falschen Format eingegeben")
            print("Denken Sie daran: ")
            print("Alle Daten sollten nur in positiven Zahlen angegeben werden")
        except:
            print()

    # PLANEN
    if int(typ) == 3:
        try:
            breite = 96
            print("-" * breite)
            print("| HILFSTABELLE FÜR VORBESTIMMTE PARAMETER, DIE FÜR VERSCHIEDENE MATERIALIEN BENÖTIGT WERDEN |")
            print("-" * breite)
            print("|        PARAMETER FÜR SCHNITTKÖPFE ZUR PLANUNG C270 & A270 AUSGEWÄHLT        |")
            print("*" * breite)
            print("|WL10(H210T)| W(H210T) |TZM(H210T)|Mo(H210T)|STAHL(GM 43)|Ta(H210T)|ALUMINIUM(H216T)|KÜNSTLICH(H216T)|")
            print("-" * breite)
            print("|    120    |    70    |    160   |   160   |    150     |    90   |    500       |     250        |Vc [m/min]")
            print("-" * breite)
            print("|   0.08   |   0.11   |   0.12   |   0.12  |    0.1     |   0.06  |   0.15       |     0.1-0.5    |fz [mm]")
            print("=" * breite)
            print("|       PARAMETER FÜR SCHNITTKÖPFE ZUR PLANUNG CHSC AUSGEWÄHLT           |")
            print("-" * breite)
            print("|WL10(XDKT) | W(XDKT)  |TZM(XDKT) |Mo(XDKT) |STAHL(GM 43)|Ta(XDKT)|ALUMINIUM(XDKT)|KÜNSTLICH(XDKT)|")
            print("-" * breite)
            print("|    140    |    85    |    180   |   180   |    150     |    95   |    500       |     260        |Vc [m/min]")
            print("-" * breite)
            print("|   0.08   |   0.08   |    0.1   |   0.1   |    0.08    |   0.05  |   0.12       |     0.1-0.5    |fz [mm]")
            print("*" * breite)

            vc = input("Geben Sie die Schnittgeschwindigkeit Vc in m/min ein: ")
            vc2 = vc.replace(",", ".")

            if 0 < float(vc2):
                durchmesser = input("Geben Sie den Werkzeugdurchmesser Ø in mm ein: ")
                durchmesser2 = durchmesser.replace(",", ".")
            elif 0 >= float(vc2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < float(durchmesser2):
                z = input("Geben Sie die Anzahl der Schneidzähne Z ein: ")
            elif 0 >= float(durchmesser2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < int(z):
                fz = input("Geben Sie den Vorschub pro Zahn fz ein: ")
                fz2 = fz.replace(",", ".")
            elif 0 >= int(z):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 >= float(fz2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < float(vc2) and 0 < float(durchmesser2) and 0 < float(fz2) and 0 < int(z):
                print()
                rpm = ((float(vc2)) * 1000) / ((float(durchmesser2)) * 3.1416)
                print("Berechnete U/min:", int(rpm), "U/min")
                vorschub = int(rpm) * float(fz2) * int(z)
                print("Berechnete Vorschubgeschwindigkeit:", int(vorschub), "mm/min")
        except ValueError:
            print("Hoppla.. Sie haben Daten in einem falschen Format eingegeben")
            print("Denken Sie daran: ")
            print("Alle Daten sollten nur in positiven Zahlen angegeben werden")
            print("Die Anzahl der Zähne sollte in Ganzzahlen angegeben werden")
        except:
            print()

    # DREHEN
    if int(typ) == 4:
        try:
            breite = 101
            print("-" * breite)
            print("| Die benötigten Daten, d.h. Schnittgeschwindigkeit VC und Vorschub pro Umdrehung f/U, finden Sie in den Parameter- |")
            print("| tabellen des Werkzeugherstellers. Geben Sie den größten Materialdurchmesser Ø an, der gedreht werden soll... |")
            print("-" * breite)
            vc = input("Geben Sie die Schnittgeschwindigkeit VC in m/min ein: ")
            vc2 = vc.replace(",", ".")
            if 0 < float(vc2):
                durchmesser = input("Geben Sie den Materialdurchmesser Ø in mm ein: ")
                durchmesser2 = durchmesser.replace(",", ".")
            elif 0 >= float(vc2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < float(durchmesser2):
                fu = input("Geben Sie den Vorschub pro Umdrehung f/U in mm ein: ")
                fu2 = fu.replace(",", ".")
            elif 0 >= float(durchmesser2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 >= float(fu2):
                print("Hoppla... Sie benötigen einen positiven Wert!")
                print("LASSEN SIE UNS NOCHMAL BEGINNEN")

            if 0 < float(vc2) and 0 < float(durchmesser2) and 0 < float(fu2):
                print()
                rpm = ((float(vc2)) * 1000) / ((float(durchmesser2)) * 3.1416)
                print("Berechnete U/min:", int(rpm), "U/min")
                vorschub = int(rpm) * float(fu2)
                print("Berechnete Vorschubgeschwindigkeit:", int(vorschub), "mm/min")
        except ValueError:
            print("Hoppla.. Sie haben Daten in einem falschen Format eingegeben")
            print("Denken Sie daran: ")
            print("Alle Daten sollten nur in positiven Zahlen angegeben werden")
        except:
            print()
except:
    print("Hoppla... Sie haben falsch eingegeben...")
    print("Sie haben nur vier Optionen: |1|, |2|, |3|, |4|")
    print("LASSEN SIE UNS NOCHMAL BEGINNEN")

import datetime
x = datetime.datetime.now()
print()
print("Aktuelle Uhrzeit: ", (x.strftime("%H:%M")))
print("Heutiges Datum: " , (x.strftime("%d.%m.%Y")))

input()