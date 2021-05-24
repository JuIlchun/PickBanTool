import urllib.request

champion_raw="""AATROX
AHRI
AKALI
ALISTAR
AMUMU
ANIVIA
ANNIE
APHELIOS
ASHE
AURELION SOL
AZIR
BARD
BLITZCRANK
BRAND
BRAUM
CAITLYN
CAMILLE
CASSIOPEIA
CHO'GATH
CORKI
DARIUS
DIANA
DR. MUNDO
DRAVEN
EKKO
ELISE
EVELYNN
EZREAL
FIDDLESTICKS
FIORA
FIZZ
GALIO
GANGPLANK
GAREN
GNAR
GRAGAS
GRAVES
GWEN
HECARIM
HEIMERDINGER
ILLAOI
IRELIA
IVERN
JANNA
JARVAN IV
JAX
JAYCE
JHIN
JINX
KAI'SA
KALISTA
KARMA
KARTHUS
KASSADIN
KATARINA
KAYLE
KAYN
KENNEN
KHA'ZIX
KINDRED
KLED
KOG'MAW
LEBLANC
LEE SIN
LEONA
LILLIA
LISSANDRA
LUCIAN
LULU
LUX
MALPHITE
MALZAHAR
MAOKAI
MASTER YI
MISS FORTUNE
MORDEKAISER
MORGANA
NAMI
NASUS
NAUTILUS
NEEKO
NIDALEE
NOCTURNE
NUNU
OLAF
ORIANNA
ORNN
PANTHEON
POPPY
PYKE
QIYANA
QUINN
RAKAN
RAMMUS
REK'SAI
RELL
RENEKTON
RENGAR
RIVEN
RUMBLE
RYZE
SAMIRA
SEJUANI
SENNA
SERAPHINE
SETT
SHACO
SHEN
SHYVANA
SINGED
SION
SIVIR
SKARNER
SONA
SORAKA
SWAIN
SYLAS
SYNDRA
TAHM KENCH
TALIYAH
TALON
TARIC
TEEMO
THRESH
TRISTANA
TRUNDLE
TRYNDAMERE
TWISTED FATE
TWITCH
UDYR
URGOT
VARUS
VAYNE
VEIGAR
VEL'KOZ
VI
VIEGO
VIKTOR
VLADIMIR
VOLIBEAR
WARWICK
WUKONG
XAYAH
XERATH
XIN ZHAO
YASUO
YONE
YORICK
YUUMI
ZAC
ZED
ZIGGS
ZILEAN
ZOE
ZYRA"""

champion_split = [x for x in champion_raw.split("\n")]

#Capitalize
champion_cap = []

for x in champion_split:
    if not x.isalnum():
        temp=[ y.capitalize() for y in x.split() ]
        champion_cap.append(''.join(temp))
    else:
        champion_cap.append(x.capitalize())

champion_cap[champion_cap.index("JarvanIv")] = "JarvanIV"
champion_cap[champion_cap.index("Kog'maw")] = "KogMaw"
champion_cap[champion_cap.index("Rek'sai")] = "RekSai"
champion_cap[champion_cap.index("Wukong")] = "MonkeyKing"

champion = [''.join(filter(str.isalnum, x)) for x in champion_cap]

print(champion)

url = 'https://ddragon.leagueoflegends.com/cdn/11.10.1/img/champion/'

for i in champion:
    championurl = url+i+'.png'
    urllib.request.urlretrieve(championurl, i+'.png')