from abc import ABC,abstractmethod
import csv

class Models(ABC):
   
   @classmethod
   @abstractmethod
   def create_from_dict(cls,diccionario):
      pass 

class Director(Models):
    @classmethod
    def create_from_dict(cls,diccionario):
       return cls(diccionario["nombre"],int(diccionario["id"]))
    
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
    
class Pelicula(Models):
    @classmethod
    def create_from_dict(cls,diccionario):
       return cls(diccionario["titulo"],diccionario["sinopsis"],director=int(diccionario["director_id"]),pelicula_id=int(diccionario["id"]))
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

    def __repr__(self):
       return f"Pelicula {self.pelicula_id},{self.title},{self.director}"
    
    def __eq__(self, other: object) -> bool:
       if isinstance(other,self.__class__):
          return self.pelicula_id==other.pelicula_id and self.title==other.title
             
       else:
         return False
    def __hash__(self) -> int:
       return hash(self.pelicula_id,self.title)

class Genero(Models):
   @classmethod
   def create_from_dict(cls,diccionario):
       return cls(int(diccionario["id"]),diccionario["genero"])
   
   def __init__(self,genero:str,id:int=-1):
      self.id=id
      self.genero=genero

   def __repr__(self):
      return f"Genero{self.genero} id {self.id}"
      
   def __eq__(self, other: object):
      if isinstance(other,self.__class__):
         return self.id==other.id and self.genero==self.genero
      else:
         return False
   def __hash__(self):
       return hash((self.id,self.genero))

class Copia(Models):
   @classmethod
   def create_from_dict(cls, diccionario):
      return cls(int(diccionario["id_copia"]),int(diccionario["id_pelicula"]))  
    
   def __init__(self,id_pelicula:int,id_copia:int=-1):
      self.id_copia=id_copia
      self.id_pelicula=id_pelicula

   def __repr__(self) -> str:
       return f"Copia {self.id_copia}, pelicula {self.id_pelicula}"
   
   def __eq__(self, other: object) -> bool:
      if isinstance(other,self.__class__):
         return self.id_copia==other.id_copia and self.id_pelicula==other.id_pelicula
      else:
         return False
   def __hash__(self) -> int:
       return hash((self.id_copia,self.id_pelicula))
      
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

class DAO_CSV(DAO):
    model=None
    def __init__(self,path,encoding="utf-8"):
        self.path=path
        self.encoding=encoding
        
    def all(self):
        lista=[]
        with open(self.path,"r",newline="",encoding=self.encoding) as fichero:
            reader=csv.DictReader(fichero,delimiter=";",quotechar="'")
            for registro in reader:
                lista.append(self.model.create_from_dict(registro))
        return lista
   
class DAO_CSV_Director(DAO_CSV):
    model=Director

class DAO_CSV_Pelicula(DAO_CSV):
    model=Pelicula

class DAO_CSV_Genero(DAO_CSV):
   model=Genero

class DAO_CSV_Copia(DAO_CSV):
   model=Copia
