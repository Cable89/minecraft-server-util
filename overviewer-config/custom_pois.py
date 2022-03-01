import copy

def baseFilter(poi):
    if poi['id'] == 'Base':
        return (poi['name'], poi['description'])

def farmFilter(poi):
    if poi['id'] == 'Farm':
        return (poi['name'], poi['description'])

def bannerFilter(poi):
    if poi['id'] == 'Banner' or poi['id'] == 'minecraft:black_banner':
        if 'name' in poi:
            return poi['name']

cablesquid =  {'id': 'Base',
               'x':780,
               'y':64,
               'z':64,
               'name':'CableSquid',
               'description':'Cable89s undervannsbase'}

castlecool  = {'id': 'Base',
               'x':4031,
               'y':80,
               'z':5065,
               'name':'Castle Cool',
               'description':'<h1>Castle Cool</h1><img src="images/dealsteve.png" alt="deal with it">'}

livestream  = {'id': 'Base',
               'x':-256,
               'y':80,
               'z':-1408,
               'name':'Livestream',
               'description':'Rokreders livestream canvas'}
 
sig2        = {'id': 'Base',
               'x':-1076,
               'y':128,
               'z':-6365,
               'name':'Sig2 the dirtening',
               'description':'Sigs flyvende øy'}

stronkhold1  = {'id': 'Base',
                'x':-780,
                'y':80,
                'z':1460,
                'name':'Stronkhold',
                'description':'Stronkhold, End Portal'}

stronkhold2  = {'id': 'Base',
                'x':1842,
                'y':34,
                'z':17,
                'name':'Stronkhold',
                'description':'Stronkhold, End Portal'}

stronkhold3  = {'id': 'Base',
                'x':5592,
                'y':80,
                'z':6568,
                'name':'Stronkhold',
                'description':'Stronkhold, End Portal'}

fishfarm =     {'id': 'Farm',
                'x':1320,
                'y':64,
                'z':1111,
                'name':'Guardian FishFarm',
                'description':'<h1>Guardian FishFarm</h1><p>Produserer fisk og prismarine.</p><p>Laget av PilosiusCrinitus</p>'}

slimefarm =    {'id': 'Farm',
                'x':940,
                'y':64,
                'z':120,
                'name':'SlimeFarm',
                'description':'<h1>SlimeFarm</h1><p>Produserer slime.</p><p style="background-color:Tomato;">Private property. Tax required.</p><p>Laget av Cable89</p>'}

bambusfarm =    {'id': 'Farm',
                'x':4105,
                'y':64,
                'z':5320,
                'name':'BambusFarm',
                'description':'<h1>BambusFarm</h1><p>Produserer bambus.</p><p style="background-color:Tomato;">Private property. Tax required.</p><p>Laget av Einhen og Rosaskjorte</p>'}

sugarcanefarm = {'id': 'Farm',
                'x':4070,
                'y':64,
                'z':4977,
                'name':'SugarCaneFarm',
                'description':'<h1>SugarCaneFarm</h1><p>Produserer sugarcane.</p><p>Output i biblioteket.</p><p>Laget av The Empire</p>'}

heksefarm =    {'id': 'Farm',
                'x':1685,
                'y':64,
                'z':-700,
                'name':'HekseFarm',
                'description':'<h1>HekseFarm</h1><p>Produserer redstone, gunpowder, glowstone, flasker, og pinner.</p><p>Laget av Cable89</p>'}

honningfarm =  {'id': 'Farm',
                'x':0,
                'y':64,
                'z':-14,
                'name':'HonningFarm',
                'description':'<h1>HonningFarm</h1><p>Produserer honning i flasker og honeycomb. (Husk pant)</p><p>Laget av Cable89</p>'}

endermanfarm = {'id': 'Farm',
                'x':14,
                'y':64,
                'z':-14,
                'name':'EndermanFarm',
                'description':'<h1>EndermanFarm</h1><p>Produserer xp og uhorvelige mengder med enderpearls.</p><p>Laget av Cable89</p>'}

witherfarm =   {'id': 'Farm',
                'x':1168,
                'y':64,
                'z':190,
                'name':'WitherSkeletonFarm',
                'description':'<h1>WitherSkeletonFarm</h1><p>Produserer wither skeleton skulls, kull, bein, og steinsverd (gode mengder xp også).</p><p>Laget av Cable89</p>'}

trefarm =      {'id': 'Farm',
                'x':4402,
                'y':64,
                'z':5405,
                'name':'TreFarm',
                'description':'<h1>TreFarm</h1><p>Produserer 4 typer logs, saplings og pinner. Forbruker bonemeal. Krever player til å plante saplings.</p><p><img src="images/Oak_Log.png" alt="Oak" width="50" height="50"><b>Oak:</b> Krever egen modus se spaken på veggen, hvis eik planes uten at farmen er i eikemodus ødelegges den og må repareres.</p><p><img src="images/Spruce_Log.png" alt="Spruce" width="50" height="50"><img src="images/Birch_Log.png" alt="Birch" width="50" height="50"><b>Spruce og Birch:</b> Fungerer bra og gir gode rates</p><p><img src="images/Jungle_Log.png" alt="Jungle" width="50" height="50"><b>Jungle:</b> Gir lite saplings tilbake, ikke bærekraftig.</p><p>Se også brukermanual som bok på lectern i farmen.</p><p>Laget av Cable89</p>'}


isfarm =       {'id': 'Farm',
                'x':4190,
                'y':64,
                'z':5274,
                'name':'IsFarm',
                'description':'<h1>IsFarm</h1><p>Produserer blå is.</p><p>Isen mines manuellt med silk touch.</p><p>Laget av Epletord_</p>'}

baseDict = dict(name='Bases', filterFunction=baseFilter, icon="icons/marker_town.png", checked='True')
farmDict = dict(name='Farms', filterFunction=farmFilter, icon="icons/marker_factory.png", checked='True')
bannerDict = dict(name='Banners', filterFunction=bannerFilter, icon="icons/marker_base_plain.png")
overworld = [cablesquid, castlecool, livestream, sig2, stronkhold1, stronkhold2, stronkhold3, fishfarm, slimefarm, bambusfarm, sugarcanefarm, heksefarm, trefarm, isfarm]
nether = [witherfarm]
end = [honningfarm, endermanfarm]
