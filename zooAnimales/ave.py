from zooAnimales.animal import Animal

class Ave(Animal):
	_listado = []
	_halcones = 0
	_aguilas = 0

	def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorPlumas=None):
		super().__init__(nombre,edad,habitat,genero)
		self._colorPlumas = colorPlumas
		Ave._listado.append(self)

	def movimiento():
		return "volar"

	@classmethod
	def crearHalcon(cls,nombre,edad,genero):
		a = Ave(nombre,edad,"montanas",genero,"cafe glorioso")
		cls._listado.append(a)
		cls._halcones+=1
		return a

	@classmethod
	def crearAguila(cls,nombre,edad,genero):
		a = Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
		cls._listado.append(a)
		cls._aguilas+=1
		return a

	@classmethod
	def cantidadAves(cls):
		return len(cls._listado)

	def getColorPlumas(self):
		return self._colorPlumas

	def setColorPlumas(self,colorPlumas):
		self._colorPlumas = colorPlumas

	@classmethod
	def getListado(cls):
		return cls._listado

	@classmethod
	def setListado(cls,listado):
		cls._listado = listado



