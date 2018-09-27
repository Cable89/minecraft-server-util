import copy

def filterfunction(poi):
    if poi['id'] == 'Station':
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

overworld = [overworld1,
             overworld2,
             overworld3,
             overworld4,
             overworld5,
             overworld6,
             overworld7,
             overworld8]

netherhub = {'id': 'Station',
             'x':0,
             'y':120,
             'z':0,
             'name':'Nye Hell Sentralstasjon'}

nether = copy.deepcopy(overworld)
nether.append(netherhub)

for station in nether:
    station['x'] = station['x']/8
    station['y'] = 120
    station['z'] = station['z']/8
