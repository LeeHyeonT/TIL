# 0127_workshop

```python
# Point class 만들기

class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
# Rextangle class 만들기

class Rectangle:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_area(self):
        length = self.p2.x - self.p1.x
        height = self.p1.y - self.p2.y
        return length * height
    def get_parimeter(self):
        length = self.p2.x - self.p1.x
        height = self.p1.y - self.p2.y
        return 2 * (length + height)
    def is_square(self)
    	length = self.p2.x - self.p1.x
        height = self.p1.y - self.p2.y
        if length == height:
            return True
        else:
            return False
```

