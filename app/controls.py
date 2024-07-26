from app.views import VistaCatalogo,VistaTituloPagina
from app.models import DAO_CSV_Pelicula
from simple_screen import cls, locate,DIMENSIONS,Input,Screen_manager


class VideoClub():
    def __init__(self):
        self.title_pag=VistaTituloPagina("CATALOGO VIDEOCLUB")
        self.title_pag_2=VistaTituloPagina("***************",2)

        self.catalogo=VistaCatalogo([],0,3,0,3)
        self.dao_peliculas=DAO_CSV_Pelicula("test/data/peliculas.csv")

    def run(self):
        continuar="S"
        with Screen_manager:
         while continuar.upper()=="S":
          cls()
          peliculas=self.dao_peliculas.all()
          self.catalogo.films=peliculas
          self.title_pag.paint()
          self.title_pag_2.paint()
          self.catalogo.paint()

          locate(0,DIMENSIONS.h-1,"Repetir (S/n)")
          continuar=Input()



