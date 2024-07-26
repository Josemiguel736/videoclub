from simple_screen import locate, DIMENSIONS,Print,Input
from app.models import Director

class VistaTituloPagina():
    def __init__(self,text:str,y:int=0):
        self.text=text
        self.y=y
    
    def paint(self):
        x=(DIMENSIONS.w-len(self.text))//2
       
        
        locate(x,self.y,self.text)
        
class VistaCatalogo():
    def __init__(self,films:list,x:int,y:int,w:int,num_colums:int):
        self.x=x
        self.y=y
        self.w=w
        self.films=films
        self.num_colums=num_colums
    
    def __cls(self):
     for i in range(self.num_colums+4):   
            
        locate(self.x,self.y+2+i,f'{" "*14} {" "*14} {" "*54}')
    def director_or_none(self,director):
        if isinstance(director, Director.__class__):
            return director.director.nombre
        else:
            return director

    
    def paint(self):
        locate(self.x,self.y,"Titulo")
        locate(self.x+15,self.y,"DIrector")
        locate(self.x+30,self.y,"Sinopsis")
        locate(self.x,self.y+1,f"+{'-'*14}+{'-'*14}+{'-'*24}")

        contador=0
        for elt,film in enumerate(self.films):
            if contador==self.num_colums:
                 locate(self.x,self.y+3+elt)
                 Input("Pulsa enter para imprimir el resto")
                 contador=0
                 self.__cls()
            
            locate(self.x,self.y+2+contador,film.title[:14])
            locate(self.x+15,self.y+2+contador,f"| {film._director_id}")
            locate(self.x+30,self.y+2+contador,f"| {film.synopsis[:30]}")
            contador+=1

 


            
            


