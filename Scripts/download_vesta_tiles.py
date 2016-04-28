import requests
import os
from lxml import etree
from io import StringIO
import json

#zoom lvl to download
download_zoom = 4  #is max for DEM

print("==[[SPACE MONKEYES!]]==")

print("Starting download...")

#read the list of WMTS layer services from our file
capabilities = [\
                "https://api.nasa.gov/vesta-wmts/catalog/Vesta_Dawn_HAMO_TrueClr_DLR_global_74ppd/1.0.0/WMTSCapabilities.xml", \
                "https://api.nasa.gov/vesta-wmts/catalog/Vesta_Dawn_HAMO_DTM_DLR_Global_48ppd8/1.0.0/WMTSCapabilities.xml" \
                ]

    
http_namespaces = namespaces={'base':'http://www.opengis.net/wmts/1.0','ows': 'http://www.opengis.net/ows/1.1'}    
https_namespaces = namespaces={'base':'https://www.opengis.net/wmts/1.0','ows': 'https://www.opengis.net/ows/1.1'}    
namespaces = http_namespaces

for url in capabilities:
    response = requests.get(url.strip())

    #response check
    if response.status_code!=200:
        print("Error\n status:"+response.status_code+"\nurl: "+url)
        continue
    if len(response.content) == 0:
        print("Error\n empty response\nurl: "+url)
        continue
        
    capabilites_xml = etree.fromstring(response.content)
    
    #checking namespaces, for some reason Vesta DTM is https
    service_identification_title = capabilites_xml.xpath("ows:ServiceIdentification/ows:Title", namespaces=namespaces)
    if(len(service_identification_title)==0):
        namespaces = https_namespaces
        service_identification_title = capabilites_xml.xpath("ows:ServiceIdentification/ows:Title", namespaces=namespaces)
    
    if(len(service_identification_title)==0):
        print("Can't find service identification\nurl: {0}".format(url))
        continue
        
    service_identification_title = service_identification_title[0].text

    #create folder if necesary
    if not os.path.exists("./"+service_identification_title):
        os.makedirs("./"+service_identification_title)

    #save xml
    with open("./"+service_identification_title+"/WMTSCapabilities.xml", 'wb') as f:
        data = response.content
        f.write(data)

    style = capabilites_xml.xpath("base:Contents/base:Layer/base:Style/ows:Identifier", namespaces=namespaces)[0].text
    tileMatrixSet = capabilites_xml.xpath("base:Contents/base:TileMatrixSet/ows:Identifier", namespaces=namespaces)[0].text
    resourceURL = capabilites_xml.xpath("base:Contents/base:Layer/base:ResourceURL", namespaces=namespaces)[0].attrib['template']

    #get tile matrices
    matrices = []
    tileMatrices = capabilites_xml.xpath("base:Contents/base:TileMatrixSet/base:TileMatrix", namespaces=namespaces)
    for matrix in tileMatrices:
        zoom = matrix.xpath("./ows:Identifier", namespaces=namespaces)[0].text
        scale = matrix.xpath("./base:ScaleDenominator", namespaces=namespaces)[0].text
        width = int(float(matrix.xpath("./base:MatrixWidth", namespaces=namespaces)[0].text))
        height = int(float(matrix.xpath("./base:MatrixHeight", namespaces=namespaces)[0].text))
        top_left = matrix.xpath("./base:TopLeftCorner", namespaces=namespaces)[0].text
        matrices.append({'zoom':zoom, 'scale':scale, 'tileCols': width, 'tileRows': height, 'top_left': top_left})
    
    #save a json for future references
    with open(service_identification_title+'.json', 'w') as fp:
        json_info = {'id':service_identification_title, 'format':resourceURL[resourceURL.rfind("."):], 'tileMatrices':matrices} 
        json.dump(json_info, fp)
        
    #save everything
    print("Downloading service: {0}".format(service_identification_title))
    base_dir = "./"+service_identification_title
    for matrix in matrices:
        if int(matrix['zoom'])!= download_zoom:
            continue;
        if not os.path.exists("{0}/{1}".format(base_dir, matrix['zoom'])):
            os.makedirs("{0}/{1}".format(base_dir, matrix['zoom']))
        print("\tDownloading tile matrix (zoom level): {0}".format(matrix['zoom']))
        for row in range(0, matrix['tileRows']):
            if not os.path.exists("{0}/{1}/{2}".format(base_dir, matrix['zoom'], row)):
                os.makedirs("{0}/{1}/{2}".format(base_dir, matrix['zoom'], row))
            for col in range(0, matrix['tileCols']):
                print("\t\tDownloading tile row: {0} column: {1}".format(row, col))
                resource_url = resourceURL.replace("{Style}",style,).replace("{TileMatrixSet}",tileMatrixSet).replace("{TileMatrix}",matrix['zoom']).replace("{TileRow}", str(row)).replace("{TileCol}", str(col))
                response = requests.get(resource_url)
                tile_extension = resource_url[resource_url.rfind('.')+1:]
                with open("{0}/{1}/{2}/{3:04d}.{4}".format(base_dir, matrix['zoom'], row, col, tile_extension), 'wb') as f:
                    tile = response.content
                    f.write(tile)

print("Download finished!")
                    
print("==[[SPACE MONKEYES!]]==")