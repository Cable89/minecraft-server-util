import copy
import sys

def filterfunction(poi):
    if poi['id'] == 'Railway':
        return poi

polylinetest = {'id': 'Railway',
                'x': sys.maxsize,
                'y': sys.maxsize,
                'z': sys.maxsize,
                'text': "Wololo",
                'color': "#CCCCCC",
                'polyline': [{'x':0, 'y':75, 'z':0},{'x':4069, 'y':75, 'z':0}]}
overworld = [polylinetest]

