from .abs_factory import AbsFactory
from autos.jeep import Jeep
class JeepFactory(AbsFactory):
	def create_auto(self):
		self.jeep = jeep = Jeep()
		jeep.name = 'Jeep'
		return jeep