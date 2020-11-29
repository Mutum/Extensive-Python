

from polygon import Polygon as Polygon
from custom_polygon import Polygons as Polygons


polygons = Polygons(10, 25)
polygons.max_efficiency_polygon

[(p, p.area/p.perimeter) for p in polygons]
