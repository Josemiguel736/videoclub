from abc import ABC,abstractmethod
import csv

class Director:
    
    def __init__(self,nombre:str,id:int=-1):
        self.nombre=nombre
        self.id=id

    def __repr__(self) -> str:        
        return f"Director({self.id}){self.nombre})"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other,self.__class__):
         return self.nombre==other.nombre and self.id==other.id
        else:
            return False
    def __hash__(self) -> int:
        return hash((self.id,self.nombre))
    
class Pelicula:
    def __init__(self,title:str,synopsis:str,director:object=None,pelicula_id:int=-1):
        self.title=title
        self.synopsis=synopsis
        self.pelicula_id=pelicula_id
        self.director=director
    @property
    def director(self):
        return self._director
    
    @director.setter
    def director(self,value):
     if isinstance(value,Director):
       self._director=value
       self._director_id=value.id
     elif type(value)==int:
       self._director=None
       self._director_id=value
     else:
       raise TypeError("(Director) debe de ser un entero o una instancia de director")


class DAO(ABC):
    """
    @abstractmethod
    def save(self,instancia):
        pass
    @abstractmethod
    def update(self,instancia):
        pass
    @abstractmethod
    def delete(self, instancia):
        pass
    @abstractmethod
    def consult(self, instancia):
        pass
""" 
    @abstractmethod
    def all(self):
        pass


class DAO_CSV_Director(DAO):
    def __init__(self,path):
        self.path=path
    def all(self):
        list=[]
        with open(self.path,"r",newline="") as fichero:
            reader=csv.DictReader(fichero,delimiter=";",quotechar="'")
            for registro in reader:
                list.append(Director(registro["nombre"],int(registro["id"])))
        return list

class DAO_CSV_PELICULAS(DAO):
    pass