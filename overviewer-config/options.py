import sys
sys.path.append('/etc/minecraft')
sys.path.append('/etc/minecraft/overviewer-config')
import stations
import railways
import custom_pois

worlds["island"] = "/etc/minecraft/island"
worlds["island_nether_old"] = "/etc/minecraft/island_nether_old"

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
"manualpois": stations.overworld + railways.overworld + custom_pois.overworld,
"markers": [
            dict(name='Player', filterFunction=_PlayerIcons),
            dict(name='PlayerSpawn', filterFunction=_PlayerSpawns),
            custom_pois.overworldBaseDict,
            #custom_pois.overworldBannerDict,
            dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png", checked='True'),
            dict(name='Exploration Station', filterFunction=stations.explorationfilterfunction, icon="icons/marker_transport_yellow.png"),
            dict(name='Railways', filterFunction=railways.filterfunction)
            ],
"imgquality": 10,
"defaultzoom": 4,
"rerenderprob": 0.1
#"forcerender": True
}

renders["biomeoverlay"] = {
"world": "island",
"title": "Biomes",
"dimension": "overworld",
"rendermode": [ClearBase(), BiomeOverlay()],
"northdirection": "upper-right",
"overlay": ["survivalday"]
}

nether_custom = [Base(), EdgeLines(), Nether(), Hide(blocks=[7])] # Standard nether render, but hiding all bedrock.

renders["survivalnether"] = {
"world": "island",
"title": "Nether",
"rendermode": nether_custom,
"dimension": "nether",
"northdirection" : "upper-right",
"manualpois": stations.nether,
"markers": [dict(name='Player', filterFunction=_PlayerIcons),
            dict(name='PlayerSpawn', filterFunction=_PlayerSpawns),
            dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png", checked='True')],
"imgquality": 10,
"defaultzoom": 6
#"forcerender": True
}

renders["survivalnether_old"] = {
"world": "island_nether_old",
"title": "Nether",
"rendermode": nether,
"dimension": "nether",
"northdirection" : "upper-right",
"manualpois": stations.nether,
"markers": [dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png", checked='True')],
"imgquality": 10,
"defaultzoom": 6,
"renderchecks": 3 # Do not rerender
}

renders["survivalend"] = {
"world": "island",
"title": "The End",
"rendermode": normal,
"dimension": "end",
"northdirection" : "upper-right",
"manualpois": stations.end,
"markers": [dict(name='Player', filterFunction=_PlayerIcons),
            dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png")],
"imgquality": 10,
"defaultzoom": 6
}

renders["cavetest"] = {
"world": "island",
"title": "Cave test",
"dimension": "overworld",
"northdirection" : "upper-right",
"crop": [(-321, -1344, -192, -1473),(728, 0, 832, 128)],
"rendermode": cave
}

renders["cavetestlowerleft"] = {
"world": "island",
"title": "Cave test2",
"dimension": "overworld",
"northdirection" : "lower-left",
"crop": [(-321, -1344, -192, -1473),(728, 0, 832, 128)],
"rendermode": cave
}

processes = 4

outputdir = "/etc/minecraft/overviewer"
texturepath = "/etc/minecraft/versions/client.jar"

# Import the Observers
from .observer import MultiplexingObserver, ProgressBarObserver, JSObserver 

# Construct the ProgressBarObserver
pbo = ProgressBarObserver()

# Construct a basic JSObserver
jso = JSObserver(outputdir, 30) 

# Set the observer to a MultiplexingObserver
observer = MultiplexingObserver(pbo, jso)

