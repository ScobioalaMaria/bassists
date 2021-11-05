list_of_bassists = {
'Flea': 'Red Hot Chili Peppers',
'Geddy Lee': 'Rush',
'Les Claypool': 'Primus',
'John Paul Jones': 'Led Zeppelin',
'John Deacon': 'Queen',
'Roger Waters': 'Pink Floyd',
'Tony Levin': 'King Crimson',
'Tony Levin': 'Peter Gabriel',
'Tony Levin': 'Liquid Tension Experiment',
'Leland Sklar': 'Phil Collins',
'John Myung': "Dream Theater",
'John Entwistle': 'The Who',
'Robert Trujillo': 'Metallica',
'Chris Squire': 'Yes', 
'Faso': 'Elio e le Storie Tese'
}

def check_bassist(bass_player):
    if bass_player in list_of_bassists:
        print("{} plays for {}".format(bass_player, list_of_bassists[bass_player]))
    else:
        print("Sorry, {} does not seem to be a known bassist".format(bass_player))

def check_band(band_name):
    for bassist, band in list_of_bassists.items():
        if band == band_name:
            print("The bass hero of {} is {}".format(band, bassist))
            return
    print("Sorry, we don't know who is the bass hero of {}".format(band_name))
