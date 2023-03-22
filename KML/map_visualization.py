import simplekml
import json

with open("KML/files/building_names.txt", 'r') as b:
    buildings = json.load(b)

# with open("KML/files/export.geojson", 'r') as f:
#     data = json.load(f)
# kml = simplekml.Kml()
# count = 0
# for feature in data['features']:
#     geom = feature['geometry']
#     geom_type = geom['type']
    
#     prop = feature['properties']
#     try: 
#         name = prop['name']
#     except:
#         name = ''
    
#     bygg = ['IPD' 'NTNU. Hovedbygningen', 'Abels hus']    
#     if name in bygg:
#         if geom_type == 'Polygon':
#             test = kml.newpolygon(name=name,
#                         outerboundaryis=geom['coordinates'][0])
#             test.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.red)

    
#     # elif geom_type == 'LineString':
#     #     kml.newlinestring(name='test',
#     #                       description='test',
#     #                       coords=geom['coordinates'])
        
#     # elif geom_type == 'Point':
#     #     kml.newpoint(name='test',
#     #                  description='test',
#     #                  coords=[geom['coordinates']])
#     # else:
#     #     print("ERROR: unknown type:", geom_type)


# kml.save('KML/output/kml_file.kml')