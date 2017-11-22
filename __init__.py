class Materiel(dict):
	"""docstring for Materiel"""
	def __init__(self, id, active,use):
		super(Materiel, self).__init__()
		self['Id'] = id
		self['Active'] = active
		self['Use'] = use

class MotherBoard(Materiel):
	def __init__(self, id, active,use,ramSlot,cpu=None):
		Materiel.__init__(self, id, active,use)
		self['RamSlot'] = ramSlot
		self['Cpu']= cpu


class Chassis(Materiel):
	def __init__(self, id, active,use,nodeCount=4,powerSupply=0):
		Materiel.__init__(self, id, active,use)
		self['NodeCount'] = nodeCount
		self['PowerSupply'] = powerSupply

class Switch(Materiel):
	def __init__(self, id, active,use):
		Materiel.__init__(self, id, active,use)

class Action(dict):
	"""docstring for Action"""
	def __init__(self,_id,_source,_target ):
		super(Action, self).__init__()
		self['_id'] = _id
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
		