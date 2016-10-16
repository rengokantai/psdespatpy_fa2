import abc
class AbsAuto(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def start(self):
		pass

	@abc.abstractmethod
	def stop(self):
		pass

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,name):
		self._name = name