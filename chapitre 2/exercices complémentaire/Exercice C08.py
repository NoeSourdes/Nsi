# # -*- coding: utf-8 -*-
# départ=input("Saisir l'horraire de départ sous le fomat HH:MM:SS : " )
# hd=int(départ[0:2])
# md=int(départ[3:5])
# sd=int(départ[6:8])
# if départ[2]!=":" or départ[5]!=":" or hd>24 or md>60 or sd>60:
#     print("Entrée invalide")
# else:
#     arrivée=input("Saisir l'horraire d'arrivée sous le fomat HH:MM:SS : " )
#     ha=int(arrivée[0:2])
#     ma=int(arrivée[3:5])
#     sa=int(arrivée[6:8])
#     if arrivée[2]!=":" or arrivée[5]!=":" or ha>24 or ma>60 or sa>60:
#         print("Entrée invalide")
#     else:
#         if hd==24:
#             hd=0
#         if md==60:
#             md=0
#         if sd==60:
#             sd=0
#         if ha==24:
#             ha=0
#         if ma==60:
#             ma=0
#         if sa==60:
#             sa=0
#         xs=0
#         a=False
#         while sd!=sa:
#             sd=sd+1
#             xs=xs+1
#             if sd==60:
#                 a=True
#                 sd=0
#         if a==True:
#             md=md+1
#         xm=0
#         a=False
#         while md!=ma:
#             md=md+1
#             xm=xm+1
#             if md==60:
#                 a==True
#                 md=0
#         if a==True:
#             hd=hd+1
#         xh=0
#         a=False
#         while hd!=ha:
#             hd=hd+1
#             xh=xh+1
#             if hd==24:
#                 hd=0
#         secondes=xh*3600+xm*60+xs
#         if xh<10:
#             strh="0"+str(xh)
#         else:
#             strh=str(xh)
#         if xm<10:
#             strm=":0"+str(xm)
#         else:
#             strm=":"+str(xm)
#         if xs<10:
#             strs=(":0"+str(xs))
#         else:
#             strs=":"+str(xs)
#         print("La durée du trajet est de",strh+strm+strs,"soit",secondes,"secondes")

heuredepart = input(
    "Dooner moi l'heure de votre départ sous forme de HH:MM:SS : ")
if heuredepart[2] != ":" or heuredepart[5] != ":":
    print("ce n'est pas les bonnes valeurs recommance !!")
else:
    hdeprat = int(heuredepart[0:2])
    mindeprat = int(heuredepart[3:5])
    secdeprat = int(heuredepart[6:8])
heurearrive = input(
    "Dooner moi l'heure de votre départ sous forme de HH:MM:SS : ")
if heurearrive[2] != ":" or heurearrive[5] != ":":
    print("ce n'est pas les bonnes valeurs recommance !!")
else:
    harrive = int(heurearrive[0:2])
    minarrive = int(heurearrive[3:5])
    secarrive = int(heurearrive[6:8])
if hdeprat > harrive:
    print("mauvais resulat")
else:
    hd = hdeprat*3600+mindeprat*60+secdeprat
    ha = harrive*3600+minarrive*60+secarrive
    secondetrajet = ha-hd
    h = secondetrajet // 3600
    resteh = secondetrajet % 3600
    min = resteh // 60
    restemin = resteh % 60
    sec = restemin % 60
    print(h, ":", min, ":", sec)
    print("ton trajet en seconde : ", secondetrajet)
