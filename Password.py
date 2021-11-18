##..................................................................................................................................................................................
##.PPPPPPPPP.......................................................................dddd.........GGGGGGG.....................................................ttt.....................
##.PPPPPPPPPP......................................................................dddd.......GGGGGGGGGG...................................................attt.....................
##.PPPPPPPPPPP.....................................................................dddd...... GGGGGGGGGGG..................................................attt.....................
##.PPPP...PPPP..aaaaaa...assssss...sssssss.sssw..wwww..wwww..oooooo..oorrrrrr.ddddddddd...... GGGG..GGGGG...eeeeee...ennnnnnn....eeeeee..eerrrrrr.aaaaaa.aaattttt..oooooo..oorrrrr..
##.PPPP...PPPP.Paaaaaaa.aasssssss.sssssssss.ssww.wwwww.wwwwwoooooooo.oorrrrrrrddddddddd..... GGG....GGG...Geeeeeee..ennnnnnnn..neeeeeee.eerrrrrrraaaaaaaaaattttttoooooooo.oorrrrr..
##.PPPPPPPPPPPPPaa.aaaaaaass.ssss.ssss.ssss.ssww.wwwwwwwww.wooo.ooooooorrr..rrddd.ddddd..... GG..........GGee.eeee..ennn.nnnnnnnee.eeee.eerrr..rraa.aaaaa.attt..tooo.ooooooorrr....
##.PPPPPPPPPP.....aaaaaaaasss.....sssss.....sswwwwwwwwwwwwwwoo...oooooorr...rrdd...dddd..... GG..GGGGGGGGGGee..eeee.ennn..nnnnnnee..eeeeeerr.......aaaaaa.attt.ttoo...oooooorr.....
##.PPPPPPPPP...Paaaaaaaa.asssss....ssssss....swwwwwwwwwwwwwwoo...oooooorr...rrdd...dddd..... GG..GGGGGGGGGGeeeeeeee.ennn..nnnnnneeeeeeeeeerr....raaaaaaaa.attt.ttoo...oooooorr.....
##.PPPP.......PPaaaaaaaa..sssssss...sssssss..swwwwwwwwwww.wwoo...oooooorr...rrdd...dddd..... GGG.GGGGGGGGGGeeeeeeee.ennn..nnnnnneeeeeeeeeerr...rraaaaaaaa.attt.ttoo...oooooorr.....
##.PPPP.......PPaa.aaaaa......ssss......ssss.swwwwwwwwwww.wwoo...oooooorr...rrdd...dddd...... GGGG....GGGGGGee.......ennn..nnnnnnee......eerr...rraa.aaaaa.attt.ttoo...oooooorr.....
##.PPPP.......PPaa.aaaaaaass..ssssssss..ssss..wwwwwwwwwww..wooo.ooooooorr...rrddd.ddddd...... GGGGGGGGGGG.GGee..eeee.ennn..nnnnnnee..eeeeeerr...rraa.aaaaa.attt..tooo.ooooooorr.....
##.PPPP.......PPaaaaaaaaaasssssss.sssssssss...wwwww.wwww...woooooooo.oorr....rddddddddd.......GGGGGGGGGG...Geeeeeee..ennn..nnnn.neeeeeee.eerr...rraaaaaaaa.attttttoooooooo.oorr.....
##.PPPP........Paaaaaaaa..ssssss....ssssss....wwww..wwww.....oooooo..oorr.....ddddddddd.........GGGGGGG.....eeeeee...ennn..nnnn..eeeeee..eerr....raaaaaaaa.attttt..oooooo..oorr.....
##..................................................................................................................................................................................

import random
import string
import time
from tqdm import tqdm #Importen van de progress bar

print("Welkom bij de Password generator!")
time.sleep(1)
print("Geef ons een momentje wij maken een perfect wachtwoord voor u...")
for i in tqdm([1,2,3,4,5]): #progress bar voor het genereren van uw wachtwoord
    time.sleep(1.4)
print("")

Lengte = int(24) #Aantal letters in het wachtwoord


# Generator
lower = string.ascii_lowercase
Upper = string.ascii_uppercase
num = string.digits
Symbols = string.punctuation

allemaal = lower + Upper + num + Symbols

temp = random.sample(allemaal, Lengte) 

Password = "".join(temp)

print("Uw nieuwe wachtwoord:" + (Password))
time.sleep(3)
Feedback = input("Geef ons een feedback.\n")