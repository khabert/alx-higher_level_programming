#!/usr/bin/python3
"""Define a class Rectangle."""                                                 
                        
 class Rectangle:                                                                
     """Represent a Rectangle."""                                                
                                                                                 
     def __init__(self, width=0, height=0):                                      
     """Initialize a new Rectangle.                                              
                                                                                 
         Args:                                                                   
         width (int): The width of the new Rectangle.                            
         height (int): The height of the new Rectangle.                          
     """                                                                         
                                                                                 
         self.width = width                                                      
         self.height = height                                                    
@property                                                                   
 def width(self):                                                            
  """Get/set the current width of the Rectangle."""                       
 return (self.__width)                                                   
                                                                             
     @width.setter                                                               
     def width(self, value):                                                     
         if not isinstance(value, int):                                          
            raise TypeError("width must be an integer")                         
        elif value < 0:                                                         
             raise ValueError("width must be >= 0")                              
         self.__width = value                                                    
                                                                                 
     @property                                                                   
     def height(self):                                                           
         """Get/set the current height of the Rectangle."""                      
         return (self.__height)

	 def area(self):
	""" Returns the area of the Rectangle """
	return (self._width * self._height)

	def perimeter(self):
	""" Return the perimeter of the Rectangle """
	return ((self._width * 2) + (self._height * 2))
