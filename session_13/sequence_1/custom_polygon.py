# Implement a Custom Polygon sequence type:
# where initializer takes in:
# number of vertices for largest polygon in the sequence
# common circumradius for all polygons
# that can provide these properties:
# max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
# that has these functionalities:
# functions as a sequence type (__getitem__)
# supports the len() function (__len__)
# has a proper representation (__repr__)


from polygon import Polygon as Polygon

class Polygons:
    ''' Polygon class
    inputs : 
            m - number of vertices for largest polygon in the sequence
            R - common circumradius for all polygons
    properties :
           max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
          
    '''
    def __init__(self, m, R):
        if m < 3:
            raise ValueError(' only two side cannot make bounded object !!, m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(edges, R) for edges in range(3, m+1)]
        
    def __len__(self):
        return self._m - 2
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __getitem__(self, s):
        return self._polygons[s]
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda polygon: polygon.area/polygon.perimeter,
                                reverse=True)
        return sorted_polygons[0]