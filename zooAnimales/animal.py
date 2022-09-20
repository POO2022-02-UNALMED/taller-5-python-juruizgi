from gestion.zona import Zona
from gestion.zoologico import Zoologico
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil

class Animal:
	_totalAnimales = 0
	def __init__(self,nombre=None,edad=None,habitat=None,genero=None):
		self._nombre = nombre
		self._edad = edad
		self._habitat = habitat
		self._genero = genero
		self._zona = [Zona()]
		Animal._totalAnimales+=1

	def movimiento():
		return "desplazarse"

	@classmethod
	def totalPorTipo(cls):
		return "Mamiferos:",len(Mamifero.getListado()),"\nAves:",len(Ave.getListado()),"\nReptiles:",len(Reptil.getListado()),"\nPeces:",len(Pez.getListado()),"\nAnfibios:",len(Anfibio.getListado())

	def toString(self):
		if (self._zona[0].getZoo()!=None and self._zona[0].getZoo()!=None and self._zona[0].getNombre()!=None):
			return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona[0].getNombre()} en el {self._zona[0].getZoo().getNombre()}"
		else:
			return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

	def __str__(self):
		if (self._zona[0].getZoo()!=None and self._zona[0].getZoo()!=None and self._zona[0].getNombre()!=None):
			return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona[0].getNombre()} en el {self._zona[0].getZoo().getNombre()}"
		else:
			return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"


	def getHabitat(self):
		return self._habitat

	def setHabitat(self, habitat):
		self._habitat = habitat

	def getGenero(self):
		return self._genero

	def setGenero(self, genero):
		self._genero = genero

	@classmethod
	def getTotalAnimales(cls):
		return cls._totalAnimales

	def getZona(self):
		return self._zona[0]

	def setZona(self, zona):
		self._zona[0] = zona

	def getNombre(self):
		return self._nombre

	def setNombre(self,nombre):
		self._nombre = nombre

	def getEdad(self):
		return self._edad

	def setEdad(self, edad):
		self._edad = edad
