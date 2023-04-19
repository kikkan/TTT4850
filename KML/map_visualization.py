import simplekml
import random
import json

bygg_instabart = [
    'IPD',
    'Handleshøyskolen',
    'Berg',
    'Byggtkniks',
    'Elektro A',
    'Elektro B',
    'Elektro D+B2',
    'Eeltro E/F',
    'Gamle elektro',
    'Gamle fysikk',
    'Gamle kjemi',
    'Grønnbygget',
    'NTNU. Hovedbygningen',
    'IT-bygget',
    'IT-bygget, sydfløy',
    'Kjelhuset',
    'Kjemi 1',
    'Kjemi 2',
    'Kjemi 3',
    'Kjemi 4',
    'Kjemi 5',
    'Kjemihallen',
    'Metallurgi',
    'Oppredning/gruvedrift',
    'PFI',
    'Realfagsbygget',
    'Sentralbygg 1',
    'Sentralbygg 2',
    'Statsarkivet',
    'Tapirbygget',
    'VM-paviljongne',
    'Verkstedtekniks'
    ]

bygg_dict = {
    "NTNU. Main Administration Building": 2.60,
    "Fluids Engineering Building": 0, #
    "P-15": 2.25, # Tapirbygget
    "Product Design Building": 3.00, # Produkt design (IPD)
    "Metallurgy Building": 0, # No data
    "Berg": 1.33,
    "Ore Processing/Mining": 2.40, # Gruve
    "World Championship Pavilion": 0, # No data
    "Geology Building": 0, # No data
    "PFI Building": 0, # No data
    "Materials Engineering Laboratory": 0, # No data
    "Perleporten": 0, # No data
    "Materials Technology Building": 3.22, # Verk
    "Building Technology": 2.75, # Byggteknisk
    "Chemistry Block 1": 3.33,
    "Chemistry Block 2": 4.00,
    "Chemistry South Wing": 0, # No data
    "Chemistry Block 3": 0, # No data
    "Chemistry Block 4": 0, # No data
    "Chemistry Block 5": 2.00, 
    "Chemistry Hall": 0, # No data
    "Central Building 1: 0, south wing": 2.91, 
    "Central Building 1: 0, tower": 2.91,
    "Central Building 1: 0, center wing": 2.91,
    "Central Building 2: 0, tower": 2.25,
    "Central Building 2: 0, north wing": 2.25,
    "Old Chemistry Building": 0, # No data
    "IT Building: 0, south wing": 4.00,
    "IT Building": 0, # No data
    "Old Physics Building": 4.00,
    "Electrical Engineering D+B2": 3.50,
    "Old Electrical Engineering Building": 3.88,
    "Water Power Laboratory" : 0, # No data
    "relation/13915142": 2.67,    # Realfagsbygget
    "way/1039396048": 3.95,       # Elektro F/E
    "way/1039395939": 3.86,       # Elektro B
    "way/1039395938": 3.50,       # Varmeteksnik / Kjel
    "way/1039395917": 6,          # Byggteknisk (2.75)
    "relation/184384": 7
}

bygg_geo_engelsk = [
    'NTNU. Main Administration Building',
    'Fluids Engineering Building',
    'P-15',
    'Product Design Building',
    'Metallurgy Building',
    'Berg',
    'Ore Processing/Mining',
    'World Championship Pavilion',
    'Geology Building',
    'PFI Building',
    'Materials Engineering Laboratory',
    'Perleporten',
    'Materials Technology Building',
    'Building Technology',
    'Chemistry Block 1',
    'Chemistry Block 2',
    'Chemistry South Wing',
    'Chemistry Block 3',
    'Chemistry Block 4',
    'Chemistry Block 5',
    'Chemistry Hall',
    'Central Building 1, south wing',
    'Central Building 1, tower',
    'Central Building 1, center wing',
    'Central Building 2, tower',
    'Central Building 2, north wing',
    'Old Chemistry Building',
    'IT Building, south wing',
    'IT Building',
    'Old Physics Building',
    'Electrical Engineering D+B2',
    'Old Electrical Engineering Building',
    'Water Power Laboratory'
]
bygg_geo_norsk = [
    'NTNU. Hovedbygningen',
    'Strømningstekniske laboratorier',
    'P-15',
    'Fraggelberget',
    'Metallurgi',
    'Berg',
    'Oppredning/gruvedrift',
    'Geologen',
    'Papirindustriens forskningsinstitutt',
    'Verkstedtekniske laboratorier',
    'Perleporten',
    'Materialtekniske laboratorier',
    'Kjemiblokk 1',
    'Kjemiblokk 2',
    'Kjemi sydfløy',
    'Kjemiblokk 3',
    'Kjemiblokk 4',
    'Kjemiblokk 5',
    'Kjemihallen',
    'Sentralbygg 1, søndre lavblokk',
    'Sentralbygg 1, høyblokk',
    'Sentralbygg 1, midtre lavblokk',
    'Sentralbygg 2, høyblokk',
    'Sentralbygg 2, nordre lavblokk',
    'Sentralbygg 2, nordre lavblokk',
    'Gamle kjemi',
    'IT-bygget, sydfløy',
    'IT-bygget',
    'Gamle fysikk',
    'Gamle elektro',
    'Elektro D+B2',
    'Central Building 2, tower'
]    
bygg_geo_id = [
    'relation/13915142',    # Realfagsbygget
    'way/1039396048',       # Elektro F/E
    'way/1039395939',       # Elektro B
    'way/1039395938',       # Varmeteksnik / Kjel
    'way/1039395917',       # Byggteknisk
    'relation/184384'
]

# RGB HEX
intensity = 'FF'
R = 'FF'
G = 'FF'
B = '00'

with open("KML/files/export.geojson", 'r') as f:
    data = json.load(f)
kml = simplekml.Kml()

output_list = []

# Iterate throug the geojson file
for feature in data['features']:
    geom = feature['geometry']
    geom_type = geom['type']
    
    # Get name of buildings
    prop = feature['properties']
    try: 
        try:
            name = prop['name:en']
        except:
            name = prop['name']
    except:
        name = ''

    if name in bygg_geo_engelsk:
        output_list.append(name)
        if geom_type == 'Polygon' :
            test = kml.newpolygon(name=name,
                        outerboundaryis=geom['coordinates'][0])
            # test.style.polystyle.color = intensity + B + G + R 
            test.style.polystyle.colormode = 'random'

    # Execptions for buildings without name
    prop = feature['properties']
    try:
        _id = prop['@id']
    except:
        _id = ''
    
    if _id in bygg_geo_id:
        output_list.append(_id)
        if geom_type == 'Polygon':
            test = kml.newpolygon(name=name,
                        outerboundaryis=geom['coordinates'][0])
            #test.style.polystyle.color = intensity + B + G + R 
            test.style.polystyle.colormode = 'random'
    
print(output_list)
#kml.save('KML/output/kml_file.kml')