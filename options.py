import sys
sys.path.append('/etc/minecraft')
import stations

worlds["island"] = "/etc/minecraft/island"

def _PlayerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

def _PlayerSpawns(poi):
    if poi['id'] == 'PlayerSpawn':
        return "Spawn for %s" % poi['EntityId']

renders["survivalday"] = {
"world": "island",
"title": "Overworld",
"rendermode": normal,
"dimension": "overworld",
"northdirection" : "upper-right",
"manualpois": stations.overworld,
"markers": [dict(name='Player', filterFunction=_PlayerIcons),
            dict(name='PlayerSpawn', filterFunction=_PlayerSpawns),
            dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png", checked='True'),
            dict(name='Exploration Station', filterFunction=stations.explorationfilterfunction, icon="icons/marker_transport_yellow.png")],
"imgquality": 10
}

#renders["biomeoverlay"] = {
#"world": "island",
#"title": "Biomes",
#"rendermode": [ClearBase(), BiomeOverlay()],
#"northdirection": "upper-right",
#}

renders["survivalnether"] = {
"world": "island",
"title": "Nether",
"rendermode": nether,
"dimension": "nether",
"northdirection" : "upper-right",
"manualpois": stations.nether,
"markers": [dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png", checked='True')],
"imgquality": 10
}

renders["survivalend"] = {
"world": "island",
"title": "The End",
"rendermode": normal,
"dimension": "end",
"northdirection" : "upper-right",
"imgquality": 10
}

processes = 4

outputdir = "/etc/minecraft/overviewer"
texturepath = "/etc/minecraft/versions/client.jar"
