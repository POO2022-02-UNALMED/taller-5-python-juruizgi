from gestion.zona import Zona

class Zoologico:
	def __init__(self,nombre=None,ubicacion=None):
		self._nombre = nombre
		self._ubicacion = ubicacion
		self._zonas = []

	def agregarZonas(self,zona):
		self._zonas.append(zona)

	def cantidadTotalAnimales(self):
		contador = 0
		for i in self._zonas:
			contador+=i.cantidadAnimales()
		return contador

	def getNombre(self):
		return self._nombre

	def setNombre(self,nombre):
		self._nombre = nombre

	def getUbicacion(self):
		return self._ubicacion

	def setUbicacion(self,ubicacion):
		self._ubicacion = ubicacion

	def getZona(self):
		return self._zonas

