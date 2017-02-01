# Object attribute Access - 
# Self is the instance of the descriptor
# obj is the instance of the object the descriptor is attached to.
# type is the class the descriptor is attached to.
# __get__ can be called on the class or object, __set__ can only be called on the object

# self, and type are both provided on object attribute access, only type is provided on class attribute access.











class Widget(object):
	copyright = "asf"

class Circle(Widget):
	pi = 3.14
	# Constructor
	def __init__(self, rad):
		self.radius = rad

	@property
	def circumference(self):
		return 2 * self.pi * self.radius
 


class MyDescriptor(object):
	def __get__(self, obj, type):
		print self, obj, type
	def __set__(self, obj, val):
		print "got %s" %val


class MyDescriptor(object):
	def __get__(self, obj, type):
		return self.data
	def __set__(self, obj, val):
		self.data = val
		
class MyClass(object):
	x = MyDescriptor()