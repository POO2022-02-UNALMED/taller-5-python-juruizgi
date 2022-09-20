from zooAnimales.animal import Animal

class Mamifero(Animal):
	_listado = []
	caballos = 0
	leones = 0

	def __init__(self,nombre=None,edad=None,habitat=None,genero=None,pelaje=None,patas=None):
		super().__init__(nombre,edad,habitat,genero)
		self._pelaje = pelaje
		self._patas = patas
		Mamifero._listado.append(self)

	@classmethod
	def crearCaballo(cls,nombre,edad,genero):
		m = Mamifero(nombre,edad,"pradera",genero,True,4)
		cls.caballos+=1
		return m

	@classmethod
	def crearLeon(cls,nombre,edad,genero):
		m = Mamifero(nombre,edad,"selva",genero,True,4)
		cls.leones+=1
		return m

	@classmethod
	def cantidadMamiferos(cls):
		return len(cls._listado)

	def isPelaje(self):
		return self._pelaje

	def setPelaje(self,pelaje):
		self._pelaje = pelaje

	def getPatas(self):
		return self._patas

	def setPatas(self,patas):
		self._patas = patas

	@classmethod
	def getListado(cls):
		return cls._listado

	@classmethod
	def setListado(cls,listado):
		cls._listado = listado