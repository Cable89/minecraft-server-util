import copy

def baseFilter(poi):
    if poi['id'] == 'Base':
        return (poi['name'], poi['description'])

def bannerFilter(poi):
    if poi['id'] == 'Banner' or poi['id'] == 'minecraft:black_banner':
        if 'name' in poi:
            return poi['name']

castlecool  = {'id': 'Base',
               'x':4031,
               'y':80,
               'z':5065,
               'name':'Castle Cool',
               'description':'<h1>Castle Cool</h1><img src="images/dealsteve.png" alt="Deal with it">'}
exploration16 = {'id': 'Exploration Station', 'x':-8192, 'y':80, 'z':-4096, 'name':'Pink Exploration Station'}

overworld = [castlecool]
overworldBaseDict = dict(name='Bases', filterFunction=baseFilter, icon="icons/marker_town.png")
overworldBannerDict = dict(name='Banners', filterFunction=bannerFilter, icon="icons/marker_base_plain.png")
nether = []
end = []
