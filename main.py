import os
import pandas as pd
from urllib.request import urlretrieve

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
#print (cwd)

file = 'lijst.xls'

def search_band():
    zoek_band = input("Naam van de band: ")
    subsetDataFrame = df[df['band'].str.lower() == zoek_band.lower()]
    print(subsetDataFrame.to_string(index=False))
    print(f'Aantal liedjes van {zoek_band}: {len(subsetDataFrame)}')
    return

def search_song():
    zoek_titel = input("Naam van het liedje: ")
    subsetDataFrame = df[df['titel'].str.lower() == zoek_titel.lower()]
    print(subsetDataFrame.to_string(index=False))
    print(f'Aantal liedjes met deze titel: {len(subsetDataFrame)}')
    return

def search_position():
    zoek_positie = int(input("Nummer op de lijst: "))
    subsetDataFrame = df[df['positie'] == zoek_positie]
    print(subsetDataFrame.to_string(index=False))
    return

def search_year():
    zoek_jaar = int(input("Jaartal: "))
    subsetDataFrame = df[df['jaar'] == zoek_jaar]
    print(subsetDataFrame.to_string(index=False))
    print(f'Aantal liedjes uit {zoek_jaar} : {len(subsetDataFrame)}')
    return

if not os.path.exists (file):
    # top2000 ophalen, wegschrijven naar disk
    print ("Downloading Top2000 of 2018...")
    dls = "http://www.nporadio2.nl/data/download/TOP-2000-2018.xls"
    urlretrieve (dls, "lijst.xls")

# read dataframe
df = pd.read_excel(file, header = None, index_col = None, names = ['positie', 'titel', 'band', 'jaar'])
# debug
# print (df)

# menu
while (1):
    print("")
    print("Welkom bij de Top2000 zoekmachine, editie 2018")
    print("")
    print ("Kies 1 om te zoeken op artiest/band")
    print ("Kies 2 om te zoeken op naam van het liedje")
    print ("Kies 3 om te zoeken op plek in de lijst")
    print ("Kies 4 om te zoeken op jaartal")
    print ("Kiez 0 om te stoppen")
    print ("")
    try:
        keuze = int(input("Maak keuze: "))
        if (keuze == 1):
            search_band()
        elif (keuze == 2):
            search_song()
        elif (keuze == 3):
            search_position()
        elif (keuze == 4):
            search_year()
        else:
            quit()
    except ValueError:
        print ("Onjuiste invoer, geef een getal op.")
print ("done")