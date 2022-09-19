from zooAnimales.animal import Animal

class Pez(Animal):
	_listado = []
	_salmones = 0
	_bacalaos = 0

	def __init__(self,nombre=None,edad=None,habitat=None,genero=None,colorEscamas=None,cantidadAletas=None):
		super().__init__(nombre,edad,habitat,genero)
		self._cantidadAletas = cantidadAletas
		self._colorEscamas = colorEscamas
		Pez._listado.append(self)

	def movimiento():
		return "nadar"

	@classmethod
	def crearSalmon(cls,nombre,edad,genero):
		p = Pez(nombre,edad,"oceano",genero,"rojo",6)
		cls._listado.append(p)
		cls._salmones+=1
		return p

	@classmethod
	def crearBacalao(cls,nombre,edad,genero):
		p = Pez(nombre,edad,"oceano",genero,"gris",6)
		cls._listado.append(p)
		cls._bacalaos+=1
		return p

	@classmethod
	def cantidadPeces(cls):
		return len(cls._listado)

	def getCantidadAletas(self):
		return self._cantidadAletas

	def setCantidadAletas(self,cantidadAletas):
		self._cantidadAletas = cantidadAletas

	def getColorEscamas(self):
		return self._cantidadAletas

	def setColorEscamas(self,colorEscamas):
		self._colorEscamas = colorEscamas

	@classmethod
	def getListado(cls):
		return cls._listado

	@classmethod
	def setListado(cls,listado):
		cls._listado = listado
