
from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import *


shp2019_mapping = {
    'id': 'id',
    'geom': 'MULTIPOLYGON',
}

shp_2019 = Path(__file__).resolve().parent / "maps" / "2019" / "2019_cc_driscoll_grid_10m_cotton.shp"

# def run(verbose=True):
#     lm = LayerMapping(Shp2019, shp_2019, shp2019_mapping, transform=False)
#     lm.save(strict=True, verbose=verbose)

cc2022_shp_mapping = {
    'fid': 'FID',
    'd220408': 'd220408',
    'd220427': 'd220427',
    'd220506': 'd220506',
    'd220511': 'd220511',
    'd220521': 'd220521',
    'd220526': 'd220526',
    'd220603': 'd220603',
    'd220608': 'd220608',
    'd220617': 'd220617',
    'd220623': 'd220623',
    'd220630': 'd220630',
    'd220708': 'd220708',
    'd220713': 'd220713',
    'geom': 'MULTIPOLYGON',
}

Cc2022_shp_file = Path(__file__).resolve().parent / "shp_data" / "geodata2022_CC.shp"

# def run(verbose=True):
#     lm = LayerMapping(Cc2022_shp, Cc2022_shp_file, cc2022_shp_mapping, transform=False)
#     lm.save(strict=True, verbose=verbose)


shp2019_mapping = {
    'id': 'id',
    'geom': 'MULTIPOLYGON',
}



shp2022_mapping = {
    'fid': 'FID',
    'geom': 'MULTIPOLYGON',
}

shp_2022 = Path(__file__).resolve().parent / "maps" / "2022" / "2022_cc_driscoll_grid_10m_cotton.shp"

def run(verbose=True):
    lm = LayerMapping(Shp2022, shp_2022, shp2022_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)