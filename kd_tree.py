from typing import List
from collections import namedtuple
import time


class Point(namedtuple("Point", "x y")):
    def __repr__(self) -> str:
        return f'Point{tuple(self)!r}'


class Rectangle(namedtuple("Rectangle", "lower upper")):
    def __repr__(self) -> str:
        return f'Rectangle{tuple(self)!r}'

    def is_contains(self, p: Point) -> bool:
        return self.lower.x <= p.x <= self.upper.x and self.lower.y <= p.y <= self.upper.y


class Node(namedtuple("Node", "location left right")):
    """
    location: Point
    left: Node
    right: Node
    """

    def __repr__(self):
        return f'{tuple(self)!r}'


class KDTree:
    """k-d tree"""

    def __init__(self):
        self._root = None
        self._n = 0

    def insert(self, p: List[Point]):
        def insert_recursive(node,point,depth):
            #base case:node is None, create new node
            if node is None:
                return Node(point,None,None)
            #determine the next axis to split on
            axis=depth%2
            #compare point to node location along the current axis
            if point [axis]<node.location[axis]:
                #recurse on left child 
                node=node._replace (left=insert_recursive(node.left,point,depth+1))
            else:
                  #recurse on right child
                   node=node._replace(right=insert_recursive(node.right,point,depth+1))
                   return node
                   self._root=insert_recursive(self._root,p,0)
                   self._n+=1
        
                  
        

    def range(self, rectangle: Rectangle) -> List[Point]:
        def range_recursive(node,rectangle):
            #base case:node is Node,return empty list
            if node is Node:
                #if node location is contained within the rectangle, add to result list
                result=[]
            if rectangle.is_contains(node.location):
                result.append(node.location)
                #if the rectangle intersects the left child's rectangle, recurse on left child
                if rectangle.lower.x<=node.location.x:
                    result.extend(range_recursive(node.left,rectangle))
                    #if the rectangle intersects the right child's rectangle,recurse on right child
                if rectangle.upper.x>=node.location.x:
                    result.extend(range_recursive(node.right,rectangle))
                    return result
                    return range_recursive(self._root,rectangle)

        

def range_test():
    points = [Point(7, 2), Point(5, 4), Point(9, 6), Point(4, 7), Point(8, 1), Point(2, 3)]
    kd = KDTree()
    kd.insert(points)
    result = kd.range(Rectangle(Point(0, 0), Point(6, 6)))
    assert sorted(result) == sorted([Point(2, 3), Point(5, 4)])


def performance_test():
    points = [Point(x, y) for x in range(1000) for y in range(1000)]

    lower = Point(500, 500)
    upper = Point(504, 504)
    rectangle = Rectangle(lower, upper)
    #  naive method
    start = int(round(time.time() * 1000))
    result1 = [p for p in points if rectangle.is_contains(p)]
    end = int(round(time.time() * 1000))
    print(f'Naive method: {end - start}ms')

    kd = KDTree()
    kd.insert(points)
    # k-d tree
    start = int(round(time.time() * 1000))
    result2 = kd.range(rectangle)
    end = int(round(time.time() * 1000))
    print(f'K-D tree: {end - start}ms')

    assert sorted(result1) == sorted(result2)


if __name__ == '__main__':
    range_test()
    performance_test()


def performance_test() :
    # Store the running times of each method in separate lists
    naive_times = []
    kd_times = []
    
    #Test performance for different numbers of points
    for num_points in range(100,1000,100):
        points =[point(x,y) for x in range(num_points) for y in range(num_points)]
        
        lower = Point(500,500)
        upper = Point(504,504)
        rectangle=Rectangle (lower,upper)
        
        #naive method
        start =int(round(time.time()*1000))
        result=[p for p in points if rectangle.is_contains(p)]
        end=int(round(time.time()*1000))
        naive_times.append(end-start)
        
        #K-D tree
        kd=KDTree()
        kd.insert(points)
        start=int(round(time.time()*1000))
        result2=kd.range(rectangle)
        end=int(round(time.time()*1000))
        kd_times.append(end-start)
        
        assert sorted(result)==sorted(result2)




def nearest_neighbor(self,p:Point)->Point:
    def nearest_neighbor_recursive(node,point,depth,best):
        #base case:node is Node,return best
        if node is None:
            return best
        #update best if necessary
        if node .location.distance(point)<best.distance(point):
            best=node.location
            #determine the next axis to split on
            axis=depth%2
            #compare point to node location along the current axis
        if point[axis]<node.location[axis]:
            #recurse on left child
            best=nearest_neighbor_recursive(node.left,point,depth+1,best)
            #check if there may be a better point in the right child's rectangle
        if abs(point[axis]-best[axis])>abs(point[axis]-node.location[axis]):
            best=nearest_neighbor_recursive(node.right,point,depth+1,best)
        else:
                #recurse on right child 
                best=nearest_neighbor_recursive(node.right,point,depth+1,best)
                #check if there may be a better point in the left child's rectangle
        if abs(point[axis]-best[axis])>abs(point[axis]-node.location[axis]):
            best=nearest_neighbor_recursive(node.left,point,depth+1,best)
            return best
        return nearest_neighbor_recursive(self._root,p,0,self._root.location)
