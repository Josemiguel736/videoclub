from app.models import Director,DAO_CSV_Director,Pelicula

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