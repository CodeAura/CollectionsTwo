# CollectionsTwo

## Boodschappenlijst
import time

Dict = {}

while True:
    print("SHOP: Wilt u wat toevoegen aan uw boodschappenlijst (J/N)")
    YN = input("Gebruiker: ")
    if YN == "J" or YN == "j":
        print("SHOP: Wat wilt u toevoegen aan uw boodschappenlijst?")
        BL = input("Gebruiker: ")
        print("SHOP: Hoeveel wilt u toevoegen?")
        HM = int(input("Gebruiker: "))
        if HM in Dict:
            Dict[BL] += HM
        else:
            Dict.update({BL : HM})
        print(Dict)
    elif YN == "N" or YN == "n":
        print("-----------------------")
        print("  Boodschappenlijst:   ")
        print(Dict)
        print("-----------------------")
        break
    else:
        print("Sorry maar ik begrijp het niet.")
