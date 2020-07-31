import copy
import sys

# File format based on: https://github.com/overviewer/Minecraft-Overviewer/pull/1649

def filterfunction(poi):
    if poi['id'] == 'Station':
        return (poi['name'], poi['description'])

def explorationfilterfunction(poi):
    if poi['id'] == 'Exploration Station':
        return (poi['name'], poi['description'])

stations = {}

stations["overworld"] = {
    "Noname1 Sentralstasjon":{
        'x':-4096,  'y':80, 'z':-4096,
        'description':'Planlagt Ikke Navngitt Sentralstasjon'
    },
    "Terese Jordhaug Stavkirke Sentralstasjon":{
        'x':0,      'y':80, 'z':-4096,
        'description':''
    },
    "Noname2 Sentralstasjon":{
        'x':4096,   'y':80, 'z':-4096,
        'description':'Planlagt Ikke Navngitt Sentralstasjon'
    },
    "Hellopolis Sentralstasjon":{
        'x':4096,   'y':80, 'z':0,
        'description':''
    },
    "Flyvende Øy Sentralstasjon":{
        'x':4096,   'y':80, 'z':4096,
        'description':''
    },
    "Endor Sentralstasjon":{
        'x':0,  'y':80, 'z':4096,
        'description':''
    },
    "Obsidian Spire Sentralstasjon":{
        'x':-4096,  'y':80, 'z':4096,
        'description':''
    },
    "Serengeti Sentralstasjon":{
        'x':-4096,  'y':80, 'z':0,
        'description':''
    },
}
stations["overworld-exploration"] = {
    "White Exploration Station":{
        'x':-8192,  'y':80, 'z':-8192,
        'color': "white"
    },
    "Grey Exploration Station":{
        'x':-4096,  'y':80, 'z':-8192,
        'color': "gray"
    },
    "Dark Grey Exploration Station":{
        'x':    0,  'y':80, 'z':-8192,
        'color': "dark_gray"
    },
    "Black Exploration Station":{
        'x': 4096,  'y':80, 'z':-8192,
        'color': "black"
    },
    "Brown Exploration Station":{
        'x': 8192,  'y':80, 'z':-8192,
        'color': "brown"
    },
    "Red Exploration Station"
        'x': 8192,  'y':80, 'z':-4096,
        'color': "red"
    },
    "Orange Exploration Station":{
        'x': 8192,  'y':80, 'z':    0,
        'color': "orange"
    },
    "Yellow Exploration Station":{
        'x': 8192,  'y':80, 'z': 4096,
        'color': "yellow"
    },
    "Lime Exploration Station":{
        'x': 8192,  'y':80, 'z': 8192,
        'color': "lime"
    },
    "Green Exploration Station":{
        'x': 4096,  'y':80, 'z': 8192,
        'color': "green"
    },
    "Cyan Exploration Station":{
        'x':    0,  'y':80, 'z': 8192,
        'color': "cyan"
    },
    "Light Blue Exploration Station":{
        'x':-4096,  'y':80, 'z': 8192,
        'color': "light_blue"
    },
    "Blue Exploration Station":{
        'x':-8192,  'y':80, 'z': 8192,
        'color': "blue"
    },
    "Purple Exploration Station":{
        'x':-8192,  'y':80, 'z': 4096,
        'color': "purple"
    },
    "Magenta Exploration Station":{
        'x':-8192,  'y':80, 'z':    0,
        'color': "magenta"
    },
    "Pink Exploration Station":{
        'x':-8192,  'y':80, 'z':-4096,
        'color': "pink"
    },
}

stations["end"] = {
    "Arrival":{
        'x':120,    'y':80, 'z':0,
    },
    "XP Farm":{
        'x':14,     'y':80, 'z':-14,
    },
    "Heim te mor":{
        'x':0,      'y':80, 'z':0,
    },
    "Further down the rabbit hole":{
        'x':0,      'y':80, 'z':-80,
    },
    "Teleport1-1":{
        'x':-84,    'y':80, 'z':35,
    },
    "Teleport1-2":{
        'x':-1092,  'y':80, 'z':324,
    },
    "Teleport1-3":{
        'x':-2506,  'y':80, 'z':225,
    },
}
exploration = [exploration01,
               exploration02,
               exploration03,
               exploration04,
               exploration05,
               exploration06,
               exploration07,
               exploration08,
               exploration09,
               exploration10,
               exploration11,
               exploration12,
               exploration13,
               exploration14,
               exploration15,
               exploration16]

overworld.extend(exploration)

netherhub = {'id': 'Station',
             'x':0,
             'y':120,
             'z':0,
             'name':'Nye Hell Sentralstasjon'}

nether = copy.deepcopy(overworld)
nether.append(netherhub)
nether.extend(copy.deepcopy(exploration))

for station in nether:
    station['id'] = 'Station'
    station['x'] = station['x']/8
    station['y'] = 120
    station['z'] = station['z']/8

end = [end1, end2, end3, end4, end5, end6, end7]

def stationPois(dimension):
    stp = stationToPoi(dimension):
    return [stp(name, info) for name, info in stations[dimension].items()]
