import random

namen = {}
Lootjes = []

while True:
    Names = input("Welke namen wilt u toevoegen\n")
    Lootjes.append(Names)
    Lootjes.sort()
    namen[Names] = random.choices(Lootjes)
    Checker = input("Wilt u meer namen toevoegen? (J/N) als je klaar bent type je (done)\n")
    if Checker == 'N' or Checker == 'N':
        print('De getrokken lootjes\n' + str(namen))
        break
    elif Checker == 'J' or Checker == 'j':
        if len(Names) >= 0:
            print(namen)
        else:
            namen[Names] = Lootjes
            print(namen)