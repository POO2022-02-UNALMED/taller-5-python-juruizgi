from zooAnimales.animal import Animal

class Anfibio(Animal):
	_listado = []
	_ranas = 0
	_salamandras = 0
	def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorPiel=None,venenoso=None):
		super().__init__(nombre,edad,habitat,genero)
		self._colorPiel = colorPiel
		self._venenoso = venenoso
		Anfibio._listado.append(self)

	def movimiento():
		return "salatar"

	@classmethod
	def crearRana(cls,nombre,edad,genero):
		an = Anfibio(nombre, edad, "selva", genero, "rojo", True)
		cls._listado.append(an)
		cls._ranas+=1
		return an

	@classmethod
	def crearSalamandra(cls,nombre,edad,genero):
		an = Anfibio(nombre,edad,"selva",genero,"negro y amarillo", False)
		cls._listado.append(an)
		cls._ranas+=1
		return an

	@classmethod
	def cantidadAnfibios(cls):
		return len(cls._listado)

	@classmethod
	def setListado(cls,listado):
		cls._listado = listado

	@classmethod
	def getListado(cls):
		return cls._listado

	def setColorPiel(self, colorPiel):
		self._colorPiel = colorPiel

	def getColorPiel(self):
		return self._colorPiel

	def isVenenoso(self):
		return self._venenoso

	def setVenenoso(self, venenoso):
		self._venenoso = venenoso