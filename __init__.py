class Materiel(object):
	"""docstring for Materiel"""
	def __init__(self, id, active,use, brand="",used=[]):
		super(Materiel, self).__init__()
		if type(id) == "String":
			self.__id__ = id
		self.__brand__ = brand
		if type(active) == "Boolean":
			self.__active__ = active
		if type(use) == "Boolean":
			self.__use__ = use
		if type(used) == "List":
			self.__used__ = used

	def getId(self):
		return self.__id__
	def getBrand(self):
		return self.__brand__
	def getActive(self):
		return self.__active__
	def getUse(self):
		return self.__use__
	def getUsed(self):
		return self.__used__

class MotherBoard(Materiel):
	def __init__(self):
		Materiel.__init__(self)

class Chassis(Materiel):
	def __init__(self,nodeCount=4,PowerSupply=0):
		Materiel.__init__(self)
		self.__nodeCount__ = nodeCount
		nodes =[]
		for slot in range(0,nodeCount-1):
			nodes.append("")
		self.__nodes__ = nodes
		self.__powerSupply

class Switch(Materiel):
	def __init__(self):
		Materiel.__init__(self)

class Leasing(object):
	"""docstring for Leasing"""
	def __init__(self, arg):
		super(Leasing, self).__init__()
		self.arg = arg
		