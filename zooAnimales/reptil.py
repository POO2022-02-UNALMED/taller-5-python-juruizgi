from zooAnimales.animal import Animal

class Reptil(Animal):
	_listado = []
	iguanas = 0
	serpientes = 0

	def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorEscamas=None,largoCola=None):
		super().__init__(nombre,edad,habitat,genero)
		self._colorEscamas = colorEscamas
		self._largoCola = largoCola
		Reptil._listado.append(self)

	def movimiento():
		return "reptar"

	@classmethod
	def cantidadReptiles(cls):
		return len(cls._listado)

	@classmethod
	def crearIguana(cls,nombre,edad,genero):
		r = Reptil(nombre,edad,"humedal",genero,"verde",3)
		cls._listado.append(r)
		cls.iguanas+=1
		return r

	@classmethod
	def crearSerpiente(cls,nombre,edad,genero):
		r = Reptil(nombre,edad,"jungla",genero,"blanco",1)
		cls._listado.append(r)
		cls.serpientes+=1
		return r

	def getColorEscamas(self):
		return self._colorEscamas

	def setColorEscamas(self,colorEscamas):
		self._colorEscamas = colorEscamas

	@classmethod
	def getListado(cls):
		return cls._listado

	@classmethod
	def setListado(cls,listado):
		cls._listado = listado

	def getLargoCola(self):
		return self._largoCola

	def setLargoCola(self,largoCola):
		self._largoCola = largoCola