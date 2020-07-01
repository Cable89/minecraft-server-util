import copy

def filterfunction(poi):
    if poi['id'] == 'Station':
        return poi['name']

def explorationfilterfunction(poi):
    if poi['id'] == 'Exploration Station':
        return poi['name']

overworld1  = {'id': 'Station',
               'x':-4096,
               'y':80,
               'z':-4096,
               'name':'Planlagt Ikke Navngitt Sentralstasjon'}
overworld2 = {'id': 'Station',
              'x':0,
              'y':80,
              'z':-4096,
              'name':'Terese Jordhaug Stavkirke Sentralstasjon'}
overworld3 = {'id': 'Station',
              'x':4096,
              'y':80,
              'z':-4096,
              'name':'Planlagt Ikke Navngitt Sentralstasjon'}
overworld4  = {'id': 'Station',
               'x':4096,
               'y':80,
               'z':0,
               'name':'Hellopolis Sentralstasjon'}
overworld5 = {'id': 'Station',
              'x':4096,
              'y':80,
              'z':4096,
              'name':'Flyvende Ey Sentralstasjon'}
overworld6  = {'id': 'Station',
               'x':0,
               'y':80,
               'z':4096,
               'name':'Endor Sentralstasjon'}
overworld7 = {'id': 'Station',
              'x':-4096,
              'y':80,
              'z':4096,
              'name':'Obsidian Spire Sentralstasjon'}
overworld8 = {'id': 'Station',
              'x':-4096,
              'y':80,
              'z':0,
              'name':'Serengeti Sentralstasjon'}


exploration01 = {'id': 'Exploration Station', 'x':-8192, 'y':80, 'z':-8192, 'name':'White Exploration Station'}
exploration02 = {'id': 'Exploration Station', 'x':-4096, 'y':80, 'z':-8192, 'name':'Grey Exploration Station'}
exploration03 = {'id': 'Exploration Station', 'x':    0, 'y':80, 'z':-8192, 'name':'Dark Grey Exploration Station'}
exploration04 = {'id': 'Exploration Station', 'x': 4096, 'y':80, 'z':-8192, 'name':'Black Exploration Station'}
exploration05 = {'id': 'Exploration Station', 'x': 8192, 'y':80, 'z':-8192, 'name':'Brown Exploration Station'}
exploration06 = {'id': 'Exploration Station', 'x': 8192, 'y':80, 'z':-4096, 'name':'Red Exploration Station'}
exploration07 = {'id': 'Exploration Station', 'x': 8192, 'y':80, 'z':    0, 'name':'Orange Exploration Station'}
exploration08 = {'id': 'Exploration Station', 'x': 8192, 'y':80, 'z': 4096, 'name':'Yellow Exploration Station'}
exploration09 = {'id': 'Exploration Station', 'x': 8192, 'y':80, 'z': 8192, 'name':'Green Exploration Station'}
exploration10 = {'id': 'Exploration Station', 'x': 4096, 'y':80, 'z': 8192, 'name':'Dark Green Exploration Station'}
exploration11 = {'id': 'Exploration Station', 'x':    0, 'y':80, 'z': 8192, 'name':'Cyan Exploration Station'}
exploration12 = {'id': 'Exploration Station', 'x':-4096, 'y':80, 'z': 8192, 'name':'Light Blue Exploration Station'}
exploration13 = {'id': 'Exploration Station', 'x':-8192, 'y':80, 'z': 8192, 'name':'Blue Exploration Station'}
exploration14 = {'id': 'Exploration Station', 'x':-8192, 'y':80, 'z': 4096, 'name':'Purple Exploration Station'}
exploration15 = {'id': 'Exploration Station', 'x':-8192, 'y':80, 'z':    0, 'name':'Magenta Exploration Station'}
exploration16 = {'id': 'Exploration Station', 'x':-8192, 'y':80, 'z':-4096, 'name':'Pink Exploration Station'}

overworld = [overworld1,
             overworld2,
             overworld3,
             overworld4,
             overworld5,
             overworld6,
             overworld7,
             overworld8]

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
