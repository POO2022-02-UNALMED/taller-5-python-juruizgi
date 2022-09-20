class Zona:
	def __init__(self,nombre=None,zoo=None):
		self._nombre = nombre
		if zoo is None:self._zoo = [None]
		else:
			self._zoo = [zoo]
			self._zoo[0].agregarZonas(self)
		self._animales = []

	def agregarAnimales(self,animal):
		self._animales.append(animal)
		animal.setZona(self)

	def cantidadAnimales(self):
		return len(self._animales)

	def getNombre(self):
		return self._nombre

	def setNombre(self,nombre):
		self._nombre = nombre

	def getZoo(self):
		return self._zoo[0]

	def setZoo(self,zoo):
		self._zoo = [zoo]

	def getAnimales(self):
		return self._animales

	def setAnimales(self,animales):
		self._animales = animales