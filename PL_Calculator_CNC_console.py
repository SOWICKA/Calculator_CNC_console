# PROJEKT : Kalkulator parametrów skrawania
# DATA    : 19.11.2023
# KODOWAL : Kamil Sulewski


print("TO KALKULATOR PARAMETROW SKRAWANIA")
print("__________________")
print("| 1 = FREZOWANIE |")
print("| 2 = WIERCENIE  |")
print("| 3 = PLANOWANIE |")
print("| 4 = TOCZENIE   |")
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
print("Podaj typ obrobki dla ktorej potrzebujesz obliczyc parametry ")
typ=input("1 czy 2 albo 3 lub 4: ")


try:
    if int(typ)!=1 and int(typ)!=2 and int(typ)!=3 and int(typ)!=4 :
        print("Ops... zle wpisales...")
        print("masz do wyboru tylko |1|, |2|, |3|, |4|")
        print("ZACZNIJMY JESZCZE RAZ")

    #FREZOWANIE
    if int(typ)==1 :
        try:
            szer = 96
            print("-" * szer)
            print("| POMOCNICZA TABELA WSTEPNYCH PATAMETROW POTRZEBNYCH DO OBLICZEN  DLA POSCZEGOLNYCH MATERIALOW |")
            print("-" * szer)
            print("|          FREZOWANIE - PARAMETRY DOBRANE DLA NARZEDZI WYKONANE Z WEGLIKA SPIEKANEGO           |")
            print("*" * szer)
            print("| WL10(WYK) | W(Profitool) | TZM(WYK) | Mo(WYK) | STAL(HPC) | Ta (WYK) |   ALU   | T.SZTUCZNE  |")
            print("-" * szer)
            print("|    80     |     55-60    |    90    |   110   |     110   |    65    |   300   |    50-200   |Vc [m/min]")
            print("-" * szer)
            print("|   0,02    |      0.04    |   0.03   |   0.03  |    0.05   |   0.03   |  0.06   |   0.1-0.5   |fz [mm]")
            print("*" * szer)

            vc = input("Podaj predkosc skrawania Vc w m/min: ")
            vc2 = vc.replace(",", ".")

            if 0 < float(vc2) :
                fi = input("Podaj srednice narzedzia Ø w mm: ")
                fi2 = fi.replace(",", ".")
            elif 0 >= float(vc2) :
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 < float(fi2) :
                z = input("Podaj liczbe zebow skrawajacych Z: ")
            elif 0 >= float(fi2) :
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 < int(z) :
                fz = input("Podaj posuw na zab fz: ")
                fz2 = fz.replace(",", ".")
            elif 0 >= int(z) :
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 >= float(fz2) :
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")


            if 0<float(vc2) and 0<float(fi2) and 0<float(fz2) and 0<int(z) :
                print()
                obroty=((float(vc2))*1000) /((float(fi2))*3.1416)
                print("Wyliczone obroty to:",int(obroty),"U/min")
                posuw=int(obroty)*float(fz2)*int(z)
                print("Wyliczony posuw to:",int(posuw),"mm/min")
        except ValueError:
            print("Ups.. Podales dane w sposob niepoprawny")
            print("Pamietaj : ")
            print(" wszystkie dane podajemy tylko w liczbach")
            print(" liczbe ostrzy podajemy w liczbach calkowitych")
        except :
            print()

    #WIERCENIE
    if int(typ)==2 :
        try:
            szer = 93
            print("-" * szer)
            print("|POMOCNICZA TABELA WSTEPNYCH PATAMETROW POTRZEBNYCH DO OBLICZEN DLA POSCZEGOLNYCH MATERIALOW|")
            print("-" * szer)
            print("|         WIERCENIE - PARAMETRY DOBRANE DLA NARZEDZI WYKONANE Z WEGLIKA SPIEKANEGO          |")
            print("*" * szer)
            print("|   WL10    |      W10     |   TZM    |    Mo   |  STAL   |    Ta    |   ALU   | T.SZTUCZNE |")
            print("-" * szer)
            print("|    30     |      30      |    90    |    90   |   45    |    40    |   150   |     180    |Vc [m/min]")
            print("-" * szer)
            print("|   0,02    |     0.04     |   0.03   |   0.03  |   0.1   |   0.03   |   0.2   |     0.15   |f/U [mm]")
            print("*" * szer)

            vc = input("Podaj predkosc skrawania VC w m/min: ")
            vc2 = vc.replace(",", ".")

            if 0 < float(vc2) :
                fi = input("Podaj srednice narzedzia Ø w mm: ")
                fi2 = fi.replace(",", ".")
            elif 0 >= float(vc2):
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 < float(fi2) :
                fu = input("Podaj posuw na obrot f/U w mm: ")
                fu2 = fu.replace(",", ".")
            elif 0 >= float(fi2):
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 >= float(fu2) :
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < float(fu2) :
                print()
                obroty=((float(vc2))*1000) /((float(fi2))*3.1416)
                print("Wyliczone obroty to:",int(obroty),"U/min")
                posuw=int(obroty)*float(fu2)
                print("Wyliczony posuw to:",int(posuw),"mm/min")
        except ValueError:
            print("Ups.. Podales dane w sposob niepoprawny")
            print("Pamietaj : ")
            print(" wszystkie dane podajemy tylko w liczbach dodatnich")
        except :
            print()

    #PLANOWANIE
    if int(typ)==3 :
        try:
            szer = 96
            print("-" * szer)
            print("| POMOCNICZA TABELA WSTEPNYCH PATAMETROW POTRZEBNYCH DO OBLICZEN  DLA POSCZEGOLNYCH MATERIALOW |")
            print("-" * szer)
            print("|                   PARAMETRY DOBRANE DLA GLOWIC DO PLANOWANIA  C270 & A270                    |")
            print("*" * szer)
            print("|WL10(H210T)| W(H210T) |TZM(H210T)|Mo(H210T)|STAL(GM 43)|Ta(H210T)|ALU(H216T)|T.SZTUCZNE(H216T)|")
            print("-" * szer)
            print("|    120    |    70    |    160   |   160   |    150    |    90   |    500   |        250      |Vc [m/min]")
            print("-" * szer)
            print("|   0.08    |   0.11   |   0.12   |   0.12  |    0.1    |   0.06   |  0.15   |     0.1-0.5     |fz [mm]")
            print("=" * szer)
            print("|                     PARAMETRY DOBRANE DLA GLOWIC DO PLANOWANIA  CHSC                         |")
            print("-" * szer)
            print("|WL10(XDKT) | W(XDKT)  |TZM(XDKT) |Mo(XDKT) |STAL(GM 43)| Ta(XDKT) |ALU(XDKT)|T.SZTUCZNE(XDKT) |")
            print("-" * szer)
            print("|    140    |    85    |    180   |   180   |    150    |    95   |    500   |        260      |Vc [m/min]")
            print("-" * szer)
            print("|   0.08    |   0.08   |    0.1   |   0.1   |    0.08   |   0.05   |  0.12   |     0.1-0.5     |fz [mm]")
            print("*" * szer)

            vc = input("Podaj predkosc skrawania Vc w m/min: ")
            vc2 = vc.replace(",", ".")

            if 0 < float(vc2):
                fi = input("Podaj srednice narzedzia Ø w mm: ")
                fi2 = fi.replace(",", ".")
            elif 0 >= float(vc2):
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 < float(fi2):
                z = input("Podaj liczbe zebow skrawajacych Z: ")
            elif 0 >= float(fi2):
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 < int(z):
                fz = input("Podaj posuw na zab fz: ")
                fz2 = fz.replace(",", ".")
            elif 0 >= int(z):
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 >= float(fz2):
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < float(fz2) and 0 < int(z):
                print()
                obroty = ((float(vc2)) * 1000) / ((float(fi2)) * 3.1416)
                print("Wyliczone obroty to:", int(obroty), "U/min")
                posuw = int(obroty) * float(fz2) * int(z)
                print("Wyliczony posuw to:", int(posuw), "mm/min")
        except ValueError:
            print("Ups.. Podales dane w sposob niepoprawny")
            print("Pamietaj : ")
            print(" wszystkie dane podajemy tylko w liczbach")
            print(" liczbe ostrzy podajemy w liczbach calkowitych")
        except:
            print()

    #TOCZENIE
    if int(typ)==4 :
        try:
            szer = 101
            print("-" * szer)
            print("| Potrzebne dane czyli predkosc skrawania VC i posuw na obrot f/U znajdziesz w tabelach parametrow  |")
            print("| producenta narzedzi a jako srednice  materialu Ø podaj nawieksza srednice ktora bedzie toczona... |")
            print("-" * szer)
            vc = input("Podaj predkosc skrawania VC w m/min: ")
            vc2 = vc.replace(",", ".")
            if 0 < float(vc2) :
                fi = input("Podaj srednice materialu Ø w mm: ")
                fi2 = fi.replace(",", ".")
            elif 0 >= float(vc2):
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 < float(fi2) :
                fu = input("Podaj posuw na obrot f/U w mm: ")
                fu2 = fu.replace(",", ".")
            elif 0 >= float(fi2):
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 >= float(fu2) :
                print("Oj... portzebna wartosc dodatnia!")
                print("ZACZNIJ JESZCZE RAZ")

            if 0 < float(vc2) and 0 < float(fi2) and 0 < float(fu2) :
                print()
                obroty=((float(vc2))*1000) /((float(fi2))*3.1416)
                print("Wyliczone obroty to:",int(obroty),"U/min")
                posuw=int(obroty)*float(fu2)
                print("Wyliczony posuw to:",int(posuw),"mm/min")
        except ValueError:
            print("Ups.. Podales dane w sposob niepoprawny")
            print("Pamietaj : ")
            print(" wszystkie dane podajemy tylko w liczbach dodatnich")
        except :
            print()
except:
    print("Ops... zle wpisales...")
    print("masz do wyboru tylko |1|, |2|, |3|, |4|")
    print("ZACZNIJMY JESZCZE RAZ")

import datetime
x = datetime.datetime.now()
print()
print("Mamy godzine: ", (x.strftime("%H:%M")))
print("Dzisiejsza data: " , (x.strftime("%d.%m.%Y")))

input()