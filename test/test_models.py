from app.models import Director,DAO_CSV_Director,Pelicula,DAO_CSV_Pelicula,Genero,DAO_CSV_Genero,Copia,DAO_CSV_Copia

def test_create_dicrector():
    director=Director("Robert Redford")

    assert director.nombre=="Robert Redford"
    assert director.id==-1

def test_dao_directores_catch_all():

    dao=DAO_CSV_Director("test/data/directores.csv")
    directores=dao.all()
    assert len(directores)==8
    assert directores[7]==Director("Charlie Chaplin",8)


def test_create_pelicula():
    pelicula=Pelicula("El señor de los anillos","Sauron es muy malo",9)
    assert pelicula.pelicula_id==-1
    assert pelicula.title=="El señor de los anillos"
    assert pelicula.synopsis=="Sauron es muy malo"
    assert pelicula._director_id==9
    assert pelicula._director is None

def test_create_pelicula_and_informate_director():
    director=Director("Peter Jackson",9)
    pelicula=Pelicula("El señor de los anillos","Sauron es muy malo",director=director)

  
    assert pelicula.director==Director("Peter Jackson",9)
    assert pelicula.pelicula_id==-1
    assert pelicula._director_id==9
    assert pelicula.title=="El señor de los anillos"
    assert pelicula.synopsis=="Sauron es muy malo"

def test_asign_director_a_pelicula():
    pelicula=Pelicula("El señor de los anillos","Sauron es muy malo",-1)
    director=Director("Peter Jackson",9)
    pelicula.director=director
    assert pelicula.director==Director("Peter Jackson",9)
    assert pelicula.pelicula_id==-1
    assert pelicula._director_id==9
    assert pelicula.title=="El señor de los anillos"
    assert pelicula.synopsis=="Sauron es muy malo"

def test_dao_peliculas_catch_all():
    dao=DAO_CSV_Pelicula("test\data\peliculas.csv")
    peliculas=dao.all()
    assert len(peliculas)==5
    assert peliculas[0]==Pelicula("Un amor contra viento y marea","Los Singh son una familia india con grandes convicciones culturales de su nación de origen, que emigraron a Reino Unido antes de nacer sus primeros hijos. Uno de ellos querrá casarse con una mujer ajena a su cultura y para ello deberá hacer todos los esfuerzos por convencer a su familia.",1,6)

def test_assing_genero():
    genero=Genero("comedia")
    assert genero.genero=="comedia"
    assert genero.id==-1

def test_genero_catch_all():
    dao=DAO_CSV_Genero("data\generos.csv")
    generos=dao.all()
    assert len(generos)==13
    assert generos[0]==Genero(1,"Accion")

def test_assing_copias():
    copia=Copia(1)
    assert copia.id_copia==-1
    assert copia.id_pelicula==1

def test_copias_catch_all():
    dao=DAO_CSV_Copia("data\copias.csv")
    copia=dao.all()
    assert len(copia)==308
    assert copia[1]==Copia(2,1)