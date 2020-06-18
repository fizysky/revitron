import revitron



class BoundingBox:
    
    
    def __init__(self, element):
        """
        Inits a new BoundingBox instance for an element. In case the element has a scope box applied, the scope box's bounding box is taken.
        In case the element has no scope box, but is a view plan, the crop box is used. The default Revit bounding box is used for all other elements. 

        Args:
            element (object): A Revit Element
        """        
        if revitron._(element).get('Scope Box'):
            self.bbox = revitron._(revitron._(element).get('Scope Box')).getBbox().bbox
        else:
            if revitron._(element).getClassName() == 'ViewPlan':
                self.bbox = element.CropBox
            else:
                self.bbox = element.get_BoundingBox(None)
        
        
    def containsXY(self, bbox2):
        """
        Checks whether the bounding box contains another bounding box. Only in X and Y dimensions.

        Args:
            bbox2 (object): A bounding box object

        Returns:
            boolean: True if the bounding box entirely contains bbox2
        """
        if isinstance(bbox2, revitron.BoundingBox):
            bbox2 = bbox2.bbox
        if self.hasPointXY(bbox2.Min) and self.hasPointXY(bbox2.Max):
            return True
        return False
    
    
    def hasPointXY(self, point): 
        """
        Checks whether a point is inside a bounding box. Only in X and Y dimensions.

        Args:
            point (object): A point object

        Returns:
            boolean: True if the bounding box has the point inside
        """        
        if self.bbox.Min.X < point.X < self.bbox.Max.X and self.bbox.Min.Y < point.Y < self.bbox.Max.Y:
            return True
        return False
    
    