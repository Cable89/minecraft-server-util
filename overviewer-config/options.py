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

overworldmarkers = [
            dict(name='Player', filterFunction=_PlayerIcons),
            dict(name='PlayerSpawn', filterFunction=_PlayerSpawns),
            custom_pois.baseDict,
            custom_pois.farmDict,
            #custom_pois.bannerDict,
            dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png", checked='True'),
            dict(name='Exploration Station', filterFunction=stations.explorationfilterfunction, icon="icons/marker_transport_yellow.png"),
            dict(name='Railways', filterFunction=railways.filterfunction)
            ]

renders["survivalday"] = {
"world": "island",
"title": "Overworld",
"rendermode": normal,
"dimension": "overworld",
"northdirection" : "upper-right",
"manualpois": stations.overworld + railways.overworld + custom_pois.overworld,
"markers": overworldmarkers,
"imgquality": 10,
"defaultzoom": 4
#"rerenderprob": 0.1
# "forcerender": True ## add back after rendering caves
}

renders["survivalday_old"] = {
"world": "island",
"title": "Overworld_old",
"rendermode": normal,
"dimension": "overworld",
"northdirection" : "upper-right",
"manualpois": stations.overworld + railways.overworld + custom_pois.overworld,
"markers": overworldmarkers,
"imgquality": 10,
"defaultzoom": 4,
#"rerenderprob": 0.1
#"forcerender": True
"renderchecks": 3 # Do not rerender
}


renders["biomeoverlay"] = {
"world": "island",
"title": "Biomes",
"dimension": "overworld",
"rendermode": [ClearBase(), BiomeOverlay()],
"northdirection": "upper-right",
"overlay": ["survivalday_old"],
"renderchecks": 3 # Do not rerender
}

nether_custom = [Base(), EdgeLines(), Nether(), Hide(blocks=[7])] # Standard nether render, but hiding all bedrock.

renders["survivalnether"] = {
"world": "island",
"title": "Nether",
"rendermode": nether_custom,
"dimension": "nether",
"northdirection" : "upper-right",
"manualpois": stations.nether + custom_pois.nether,
"markers": [dict(name='Player', filterFunction=_PlayerIcons),
            dict(name='PlayerSpawn', filterFunction=_PlayerSpawns),
            custom_pois.baseDict,
            custom_pois.farmDict,
            #custom_pois.bannerDict,
            dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png", checked='True')],
"imgquality": 10,
"defaultzoom": 6,
#"forcerender": True
"renderchecks": 3 # Do not rerender, temp while rendering new survivalday
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
"manualpois": stations.end + custom_pois.end,
"markers": [dict(name='Player', filterFunction=_PlayerIcons),
            custom_pois.farmDict,
            custom_pois.baseDict,
            dict(name='Station', filterFunction=stations.filterfunction, icon="icons/marker_transport_yellow.png")],
"imgquality": 10,
"defaultzoom": 6,
"renderchecks": 3 # Do not rerender, temp while rendering new survivalday
}



renders["caves_cable"] = {
"world": "island",
"title": "Caves CableSquid",
"dimension": "overworld",
"northdirection" : "upper-right",
"crop": [(728, 0, 1024, 128)],
"manualpois": stations.overworld + railways.overworld + custom_pois.overworld,
"markers": overworldmarkers,
#"forcerender": True,
#"renderchecks": 1, # Check tiles
"rendermode": cave
}


renders["caves_castlecool"] = {
"world": "island",
"title": "Caves Castle Cool",
"dimension": "overworld",
"northdirection" : "upper-right",
"crop": [(3936, 4800, 4480, 5488)],
"manualpois": stations.overworld + railways.overworld + custom_pois.overworld,
"markers": overworldmarkers,
#"forcerender": True,
#"renderchecks": 1, # Check tiles
"rendermode": cave
}

'''
renders["caves_1"] = {
"world": "island",
"title": "Caves",
"dimension": "overworld",
"northdirection" : "upper-right",
"crop": [(-321, -1344, -192, -1473),(728, 0, 1024, 128),(3936, 4800, 4480, 5488)],
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
#"forcerender": True,
#"renderchecks": 1, # Check tiles
"rendermode": cave
}

renders["caves_2"] = {
"world": "island",
"title": "Caves flipped",
"dimension": "overworld",
"northdirection" : "lower-left",
"crop": [(-321, -1344, -192, -1473),(728, 0, 1024, 128),(3936, 4800, 4480, 5488)],
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
#"forcerender": True,
#"renderchecks": 1, # Check tiles
"rendermode": cave
}
'''
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

