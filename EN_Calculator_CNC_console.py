# PROJECT: Machining Parameters Calculator
# DATE: 19.11.2023
# CODED BY: Kamil Sulewski

print("WELCOME TO THE MACHINING PARAMETERS CALCULATOR")
print("__________________")
print("| 1 = MILLING    |")
print("| 2 = DRILLING   |")
print("| 3 = PLANNING   |")
print("| 4 = TURNING    |")
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
print("Enter the type of machining for which you need to calculate parameters ")
typ = input("1 for 2, 3, or 4: ")


try:
    if int(typ) != 1 and int(typ) != 2 and int(typ) != 3 and int(typ) != 4:
        print("Oops... you typed incorrectly...")
        print("You have only four options: |1|, |2|, |3|, |4|")
        print("LET'S TRY AGAIN")

    # MILLING
    if int(typ) == 1:
        try:
            width = 96
            print("-" * width)
            print("| AUXILIARY TABLE OF PRELIMINARY PARAMETERS NEEDED FOR CALCULATIONS FOR DIFFERENT MATERIALS |")
            print("-" * width)
            print("|            MILLING - PARAMETERS SELECTED FOR TOOLS MADE OF CARBIDE ALLOY              |")
            print("*" * width)
            print("| WL10(WK) | W(Profitool) | TZM(WK) | Mo(WK) | STEEL(HPC) | Ta (WK) |   ALUMINUM   | ARTIFICIAL  |")
            print("-" * width)
            print("|    80    |     55-60     |    90    |   110   |     110    |    65   |    300       |   50-200    |Vc [m/min]")
            print("-" * width)
            print("|   0.02   |      0.04     |   0.03   |   0.03  |    0.05    |   0.03  |   0.06       |   0.1-0.5   |fz [mm]")
            print("*" * width)

            vc = input("Enter cutting speed Vc in m/min: ")
            vc2 = vc.replace(",", ".")

            if 0 < float(vc2):
                diameter = input("Enter tool diameter Ø in mm: ")
                diameter2 = diameter.replace(",", ".")
            elif 0 >= float(vc2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < float(diameter2):
                z = input("Enter number of cutting teeth Z: ")
            elif 0 >= float(diameter2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < int(z):
                fz = input("Enter feed per tooth fz: ")
                fz2 = fz.replace(",", ".")
            elif 0 >= int(z):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 >= float(fz2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < float(vc2) and 0 < float(diameter2) and 0 < float(fz2) and 0 < int(z):
                print()
                rpm = ((float(vc2)) * 1000) / ((float(diameter2)) * 3.1416)
                print("Calculated RPM:", int(rpm), "rev/min")
                feed = int(rpm) * float(fz2) * int(z)
                print("Calculated feed rate:", int(feed), "mm/min")
        except ValueError:
            print("Oops.. You provided data in an incorrect format")
            print("Remember: ")
            print("All data should be provided only in numbers")
            print("Number of teeth should be given in integers")
        except:
            print()

    # DRILLING
    if int(typ) == 2:
        try:
            width = 93
            print("-" * width)
            print("| AUXILIARY TABLE OF PRELIMINARY PARAMETERS NEEDED FOR CALCULATIONS FOR DIFFERENT MATERIALS |")
            print("-" * width)
            print("|           DRILLING - PARAMETERS SELECTED FOR TOOLS MADE OF CARBIDE ALLOY               |")
            print("*" * width)
            print("|   WL10   |      W10     |   TZM    |    Mo   |  STEEL  |    Ta    |   ALUMINUM  | ARTIFICIAL |")
            print("-" * width)
            print("|    30    |      30      |    90    |    90   |   45    |    40    |   150       |   180      |Vc [m/min]")
            print("-" * width)
            print("|   0.02   |     0.04     |   0.03   |   0.03  |   0.1   |   0.03   |   0.2       |   0.15     |f/U [mm]")
            print("*" * width)

            vc = input("Enter cutting speed VC in m/min: ")
            vc2 = vc.replace(",", ".")

            if 0 < float(vc2):
                diameter = input("Enter tool diameter Ø in mm: ")
                diameter2 = diameter.replace(",", ".")
            elif 0 >= float(vc2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < float(diameter2):
                fu = input("Enter feed per revolution f/U in mm: ")
                fu2 = fu.replace(",", ".")
            elif 0 >= float(diameter2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 >= float(fu2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < float(vc2) and 0 < float(diameter2) and 0 < float(fu2):
                print()
                rpm = ((float(vc2)) * 1000) / ((float(diameter2)) * 3.1416)
                print("Calculated RPM:", int(rpm), "rev/min")
                feed = int(rpm) * float(fu2)
                print("Calculated feed rate:", int(feed), "mm/min")
        except ValueError:
            print("Oops.. You provided data in an incorrect format")
            print("Remember: ")
            print("All data should be provided only in positive numbers")
        except:
            print()

    # PLANNING
    if int(typ) == 3:
        try:
            width = 96
            print("-" * width)
            print("| AUXILIARY TABLE OF PRELIMINARY PARAMETERS NEEDED FOR CALCULATIONS FOR DIFFERENT MATERIALS |")
            print("-" * width)
            print("|          PARAMETERS SELECTED FOR PLANING HEADS C270 & A270          |")
            print("*" * width)
            print("|WL10(H210T)| W(H210T) |TZM(H210T)|Mo(H210T)|STEEL(GM 43)|Ta(H210T)|ALUMINUM(H216T)|ARTIFICIAL(H216T)|")
            print("-" * width)
            print("|    120    |    70    |    160   |   160   |    150     |    90   |    500       |     250        |Vc [m/min]")
            print("-" * width)
            print("|   0.08    |   0.11   |   0.12   |   0.12  |    0.1     |   0.06  |   0.15       |     0.1-0.5    |fz [mm]")
            print("=" * width)
            print("|          PARAMETERS SELECTED FOR PLANING HEADS CHSC               |")
            print("-" * width)
            print("|WL10(XDKT)| W(XDKT)  |TZM(XDKT) |Mo(XDKT) |STEEL(GM 43)| Ta(XDKT)|ALUMINUM(XDKT)|ARTIFICIAL(XDKT)|")
            print("-" * width)
            print("|    140    |    85    |    180   |   180   |    150     |    95   |    500       |     260        |Vc [m/min]")
            print("-" * width)
            print("|   0.08    |   0.08   |    0.1   |   0.1   |    0.08    |   0.05  |   0.12       |     0.1-0.5    |fz [mm]")
            print("*" * width)

            vc = input("Enter cutting speed Vc in m/min: ")
            vc2 = vc.replace(",", ".")

            if 0 < float(vc2):
                diameter = input("Enter tool diameter Ø in mm: ")
                diameter2 = diameter.replace(",", ".")
            elif 0 >= float(vc2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < float(diameter2):
                z = input("Enter number of cutting teeth Z: ")
            elif 0 >= float(diameter2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < int(z):
                fz = input("Enter feed per tooth fz: ")
                fz2 = fz.replace(",", ".")
            elif 0 >= int(z):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 >= float(fz2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < float(vc2) and 0 < float(diameter2) and 0 < float(fz2) and 0 < int(z):
                print()
                rpm = ((float(vc2)) * 1000) / ((float(diameter2)) * 3.1416)
                print("Calculated RPM:", int(rpm), "rev/min")
                feed = int(rpm) * float(fz2) * int(z)
                print("Calculated feed rate:", int(feed), "mm/min")
        except ValueError:
            print("Oops.. You provided data in an incorrect format")
            print("Remember: ")
            print("All data should be provided only in numbers")
            print("Number of teeth should be given in integers")
        except:
            print()

    # TURNING
    if int(typ) == 4:
        try:
            width = 101
            print("-" * width)
            print("| You can find the required data, i.e., cutting speed VC and feed per revolution f/U, in the parameter tables |")
            print("| provided by the tool manufacturer. Enter the largest material diameter Ø to be turned... |")
            print("-" * width)
            vc = input("Enter cutting speed VC in m/min: ")
            vc2 = vc.replace(",", ".")
            if 0 < float(vc2):
                diameter = input("Enter material diameter Ø in mm: ")
                diameter2 = diameter.replace(",", ".")
            elif 0 >= float(vc2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < float(diameter2):
                fu = input("Enter feed per revolution f/U in mm: ")
                fu2 = fu.replace(",", ".")
            elif 0 >= float(diameter2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 >= float(fu2):
                print("Oops... you need a positive value!")
                print("LET'S START AGAIN")

            if 0 < float(vc2) and 0 < float(diameter2) and 0 < float(fu2):
                print()
                rpm = ((float(vc2)) * 1000) / ((float(diameter2)) * 3.1416)
                print("Calculated RPM:", int(rpm), "rev/min")
                feed = int(rpm) * float(fu2)
                print("Calculated feed rate:", int(feed), "mm/min")
        except ValueError:
            print("Oops.. You provided data in an incorrect format")
            print("Remember: ")
            print("All data should be provided only in positive numbers")
        except:
            print()
except:
    print("Oops... you typed incorrectly...")
    print("You have only four options: |1|, |2|, |3|, |4|")
    print("LET'S TRY AGAIN")

import datetime
x = datetime.datetime.now()
print()
print("Current time: ", (x.strftime("%H:%M")))
print("Today's date: " , (x.strftime("%d.%m.%Y")))

input()


