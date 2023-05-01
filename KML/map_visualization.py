import simplekml
import random
import json

effektivitet_dict = {
    "NTNU. Main Administration Building": 2.60,
    "Fluids Engineering Building": 0, # No data
    "P-15": 2.25, # Tapirbygget
    "Product Design Building": 3.00, # Produkt design (IPD)
    "Metallurgy Building": 0, # No data
    "Berg": 1.33,
    "Ore Processing/Mining": 2.40, # Gruve
    "World Championship Pavilion": 0, # No data
    "Geology Building": 0, # No data
    "PFI Building": 0, # No data
    "Materials Engineering Laboratory": 3.22, # Verk
    "Perleporten": 0, # No data
    "Materials Technology Building": 0, # No data
    "Building Technology": 2.75, # Byggteknisk
    "Chemistry Block 1": 3.33,
    "Chemistry Block 2": 4.00,
    "Chemistry South Wing": 0, # No data
    "Chemistry Block 3": 0, # No data
    "Chemistry Block 4": 0, # No data
    "Chemistry Block 5": 2.00, 
    "Chemistry Hall": 0, # No data
    "Central Building 1, south wing": 2.91, 
    "Central Building 1, tower": 2.91,
    "Central Building 1, center wing": 2.91,
    "Central Building 2, tower": 2.25,
    "Central Building 2, north wing": 2.25,
    "Old Chemistry Building": 2.25, # Same as Central Building 2, north wind
    "IT Building, south wing": 4.00,
    "IT Building": 0, # No data
    "Old Physics Building": 4.00,
    "Electrical Engineering D+B2": 3.50,
    "Old Electrical Engineering Building": 3.88,
    "Water Power Laboratory" : 0, # No data
    "relation/13915142": 2.67,    # Realfagsbygget
    "way/1039396048": 3.95,       # Elektro F/E
    "way/1039395939": 3.86,       # Elektro B
    "way/1039395938": (3.50 + 3.00)/2,       # Varmeteksnik / Kjel
    "way/1039395917": 2.75,       # Byggteknisk (2.75)
    "relation/184384": 0
}

trivsel_dict = {
    "NTNU. Main Administration Building": 2.80,
    "Fluids Engineering Building": 0, # No data
    "P-15": 2.75, # Tapirbygget
    "Product Design Building": 4.00, # Produkt design (IPD)
    "Metallurgy Building": 0, # No data
    "Berg": 1.33,
    "Ore Processing/Mining": 3.20, # Gruve
    "World Championship Pavilion": 0, # No data
    "Geology Building": 0, # No data
    "PFI Building": 0, # No data
    "Materials Engineering Laboratory": 2.78, # Verk
    "Perleporten": 0, # No data
    "Materials Technology Building": 0, # No data
    "Building Technology": 2.50, # Byggteknisk
    "Chemistry Block 1": 3.00,
    "Chemistry Block 2": 5.00,
    "Chemistry South Wing": 0, # No data
    "Chemistry Block 3": 0, # No data
    "Chemistry Block 4": 0, # No data
    "Chemistry Block 5": 2.00, 
    "Chemistry Hall": 0, # No data
    "Central Building 1, south wing": 2.55, 
    "Central Building 1, tower": 2.55,
    "Central Building 1, center wing": 2.55,
    "Central Building 2, tower": 2.50,
    "Central Building 2, north wing": 2.50,
    "Old Chemistry Building": 2.55, # Same as Central Building 2, north wind
    "IT Building, south wing": 2.00,
    "IT Building": 0, # No data
    "Old Physics Building": 3.50,
    "Electrical Engineering D+B2": 3.75,
    "Old Electrical Engineering Building": 3.88,
    "Water Power Laboratory" : 0, # No data
    "relation/13915142": 2.60,    # Realfagsbygget
    "way/1039396048": 4.35,       # Elektro F/E
    "way/1039395939": 3.71,       # Elektro B
    "way/1039395938": (3.66 + 3.50)/2,       # Varmeteksnik / Kjel
    "way/1039395917": 2.75,       # Byggteknisk (2.75)
    "relation/184384": 0
}



def get_heatmap_color(value):
    # Map the input value to a color
    # if value >= 1 and value < 1.5:
    r_hex = 0
    g_hex = 0
    b_hex = 0

    if value >= 1 and value < 1.5:
        # Light blue
        r_hex, g_hex, b_hex = 173, 216, 230
    elif value >= 1.5 and value < 2:
        # Dark blue
        r_hex, g_hex, b_hex = 0, 0, 128
    elif value >= 2 and value < 2.5:
        # Light green
        r_hex, g_hex, b_hex = 144, 238, 144
    elif value >= 2.5 and value < 3:
        # Dark green
        r_hex, g_hex, b_hex = 0, 128, 0
    elif value >= 3 and value < 3.5:
        # Light yellow
        r_hex, g_hex, b_hex = 255, 255, 153
    elif value >= 3.5 and value < 4:
        # Dark yellow
        r_hex, g_hex, b_hex = 255, 215, 0
    elif value >= 4 and value <= 4.5:
        # Dark orange
        r_hex, g_hex, b_hex = 255, 140, 0
    else:
        # Dark red
        r_hex, g_hex, b_hex = 255, 0, 0
    
    # Convert the RGB components to HEX strings and return them
    r_str = format(r_hex, '02X')
    g_str = format(g_hex, '02X')
    b_str = format(b_hex, '02X')
    
    return r_str, g_str, b_str


    # # Round the input value to the nearest integer
    # rounded_value = value
    
    # # Map the rounded value to a color
    # r_hex = 0
    # g_hex = 0
    # b_hex = 0
    # if (rounded_value >= 0 and rounded_value < 1) :
    #     # Blue
    #     r_hex, g_hex, b_hex = 0, 0, 255
    # elif  (rounded_value >= 1 and rounded_value < 2) :
    #     # Green
    #     r_hex, g_hex, b_hex = 0, 255, 0
    # elif  (rounded_value >= 2 and rounded_value < 3) :
    #     # Yellow
    #     r_hex, g_hex, b_hex = 255, 255, 0
    # elif  (rounded_value >= 3 and rounded_value < 4) :
    #     # Orange
    #     r_hex, g_hex, b_hex = 255, 165, 0
    # elif  (rounded_value >= 4 and rounded_value <= 5) :
    #     # Red
    #     r_hex, g_hex, b_hex = 255, 0, 0
    
    # # Convert the RGB components to HEX strings and return them
    # r_str = format(r_hex, '02X')
    # g_str = format(g_hex, '02X')
    # b_str = format(b_hex, '02X')
    
    # return r_str, g_str, b_str



# RGB HEX
intensity = 'FF'
R = 'FF'
G = 'FF'
B = '00'

GRAY = 'FF'

with open("KML/files/export.geojson", 'r') as f:
    data = json.load(f)
kml = simplekml.Kml()

# EFEKTIVITET
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

    
    if name in effektivitet_dict:
        g_value = 0
        for key, value in effektivitet_dict.items():
            if key == name:
                g_value = value
                R, G, B = get_heatmap_color(value)
        
        if g_value == 0:
            B = GRAY  
            G = GRAY
            R = GRAY
        
        if geom_type == 'Polygon' :
            test = kml.newpolygon(name=name,
                        outerboundaryis=geom['coordinates'][0])
            test.style.polystyle.color = intensity + B + G + R                         
            # test.style.polystyle.colormode = 'random'

    # Execptions for buildings without name
    prop = feature['properties']
    try:
        _id = prop['@id']
    except:
        _id = ''
    
    if _id in effektivitet_dict:

        for key, value in effektivitet_dict.items():
            if key == _id:
                g_value = value
                R, G, B = get_heatmap_color(value)
               
        if g_value == 0:
            B = "FF"  
            G = "FF"
            R = "FF"

        if geom_type == 'Polygon':
            test = kml.newpolygon(name=_id,
                        outerboundaryis=geom['coordinates'][0])
            test.style.polystyle.color = intensity + B + G + R 
            # test.style.polystyle.colormode = 'random'
    
kml.save('KML/output/heatmap_effektivitet.kml') 

# TRIVSEL
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

    
    if name in trivsel_dict:
        g_value = 0
        for key, value in trivsel_dict.items():
            if key == name:
                g_value = value
                R, G, B = get_heatmap_color(value)
        
        if g_value == 0:
            B = GRAY  
            G = GRAY
            R = GRAY
        
        if geom_type == 'Polygon' :
            test = kml.newpolygon(name=name,
                        outerboundaryis=geom['coordinates'][0])
            test.style.polystyle.color = intensity + B + G + R                         
            # test.style.polystyle.colormode = 'random'

    # Execptions for buildings without name
    prop = feature['properties']
    try:
        _id = prop['@id']
    except:
        _id = ''
    
    if _id in trivsel_dict:

        for key, value in trivsel_dict.items():
            if key == _id:
                g_value = value
                R, G, B = get_heatmap_color(value)
               
        if g_value == 0:
            B = "FF"  
            G = "FF"
            R = "FF"

        if geom_type == 'Polygon':
            test = kml.newpolygon(name=_id,
                        outerboundaryis=geom['coordinates'][0])
            test.style.polystyle.color = intensity + B + G + R 
            # test.style.polystyle.colormode = 'random'
    
kml.save('KML/output/heatmap_trivsel.kml') 