class Materiel(dict):
	"""docstring for Materiel"""
	def __init__(self, id_, active,use):
		super(Materiel, self).__init__()
		self['id_'] = id_
		self['Active'] = active
		self['Use'] = use

class MotherBoard(Materiel):
	def __init__(self, id_, active,use,ramSlot,cpu=None):
		Materiel.__init__(self, id_, active,use)
		self['RamSlot'] = ramSlot
		self['Cpu']= cpu


class Chassis(Materiel):
	def __init__(self, id_, active,use,nodeCount=4,powerSupply=0):
		Materiel.__init__(self, id_, active,use)
		self['NodeCount'] = nodeCount
		self['PowerSupply'] = powerSupply

class Switch(Materiel):
	def __init__(self, id_, active,use):
		Materiel.__init__(self, id_, active,use,port)
		self['port'] = port

class Customer(dict):
	def __init__(self,id_,name):
		self['id_'] = id_
		self['name'] = name

class Action(dict):
	"""docstring for Action"""
	def __init__(self,_id_,_source,_target ):
		super(Action, self).__init__()
		self['_id_'] = _id_
		self['Source'] = _source
		self['Target'] = _target

class Setup(Action):
	"""docstring for Setup"""
	def __init__(self, arg):
		self.arg = arg
		
class Leasing(Action):
	"""docstring for Leasing"""
	def __init__(self, arg):
		super(Leasing, self).__init__()
		self.arg = arg

class ArangoSession(object):
	"""docstring for ArangoSession"""
	def __init__(self, arg):
		super(ArangoSession, self).__init__()
		self.arg = arg
		