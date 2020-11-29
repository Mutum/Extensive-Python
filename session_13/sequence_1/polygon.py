# Create a Polygon Class:
# where initializer takes in:
# number of edges/vertices
# circumradius
# that can provide these properties:
# # edges
# # vertices
# interior angle
# edge length
# apothem
# area
# perimeter
# that has these functionalities:
# a proper __repr__ function
# implements equality (==) based on # vertices and circumradius (__eq__)
# implements > based on number of vertices only (__gt__)


import math

class Polygon:
    ''' Polygon class
    inputs : 
            n - number of edges/vertices
            R - circumradius
    properties :
            edges
            vertices
            interior angle
            edge length
            apothem
            area
            perimeter
    '''
    
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
 
    @property
    def count_edges(self):
        return self._n
    
    @property
    def count_vertices(self):
        return self._n
      
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def edge_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.edge_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.edge_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented