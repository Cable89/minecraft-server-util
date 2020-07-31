import sys
sys.path.append('/etc/minecraft')
import stations

worlds["island"] = "/etc/minecraft/minecraftexperiments/island"

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
            dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png", checked='True')],
"imgquality": 10
}

# minzoom = 7
# defaultzoom = 4

processes = 6

outputdir = "/etc/minecraft/overviewer_cut"
texturepath = "/etc/minecraft/versions/client.jar"
