from factories import loader


for factory_name in 'jeep_factory', 'NotExist':
	factory = loader.load_factory(factory_name)
	car = factory.create_auto()
	car.start()
	car.stop()