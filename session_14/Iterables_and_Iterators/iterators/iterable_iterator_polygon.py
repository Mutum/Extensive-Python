# Refactor the Polygons (sequence) type, into an iterable. 
# Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

# You'll need to implement both an iterable, and an iterator.


from polygon import Polygon as Polygon

class PolygonsIterator:
    '''
    Integrating iterator in previous sequence polygon class
    '''
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._i = 3
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._i > self._m:
            raise StopIteration
        else:
            result = Polygon(self._i, self._R)
            self._i += 1
            return result
        

class Polygons:
    ''' 
    updating max_efficiency_polygon property as lazy calculation
    '''
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._max_efficiency_polygon = None
        
    def __len__(self):
        return self._m - 2
    
    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __iter__(self):
        return PolygonsIterator(self._m, self._R)
    
    @property
    def max_efficiency_polygon(self):
        if self._max_efficiency_polygon is None:
            sorted_polygons = sorted(PolygonsIterator(self._m, self._R), 
                                     key=lambda p: p.area/p.perimeter,
                                    reverse=True)
            self._max_efficiency_polygon = sorted_polygons[0]
        return self._max_efficiency_polygon