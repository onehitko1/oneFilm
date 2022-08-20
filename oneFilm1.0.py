import random
import requests
import json
from easygui import *
from bs4 import BeautifulSoup
import urllib.request

lista_generos = ['https://www.imdb.com/list/ls068082370/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls000551766/?sort=list_order,asc&st_dt=&mode=detail&page=','https://www.imdb.com/list/ls055874673/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls045017156/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls062101934/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls076655138/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls076166467/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls069376839/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls064252275/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls064287418/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls027738538/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls032616214/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls066247137/?sort=list_order,asc&st_dt=&mode=detail&page=', 'https://www.imdb.com/list/ls008594849/?sort=list_order,asc&st_dt=&mode=detail&page=', 'Sair']



sair = False
while not sair:
    message = "Selecione um gênero de filme"
    title = "oneFilm1.0"
    choices = ['Todos', 'Comédia', 'Sci-fi', 'Horror', 'Romance', 'Ação', 'Suspense', 'Drama', 'Mistério', 'Crime',
               'Animação', 'Aventura', 'Fantasia', 'Comédia Romântica', '-------------------------------------------------Sair---------------------------------------------------------']
    output = choicebox(message, title, choices)
    if output == 'Sair':
        exit()
    x = 0
    for i in choices:
        if i == output:
            link_lista = lista_generos[x]
        else:
            x = x + 1


    def detalhes_filme(detalhe):
        titulo = 'Título:', detalhe['Title']
        genero = 'Gênero:', detalhe['Genre']
        ano = 'Ano:', detalhe['Year']
        diretor = 'Diretor:', detalhe['Director']
        atores = 'Atores:', detalhe['Actors']
        nota = 'Nota:', detalhe['imdbRating']
        premios = 'Prêmios:', detalhe['Awards']
        poster = detalhe['Poster']
        urllib.request.urlretrieve(str(poster), "poster.jpg")
        msgbox(msg=str(titulo)+ '\n' +str(genero)+ '\n' +str(ano)+ '\n' +str(diretor)+ '\n' +str(atores)+ '\n' +str(nota)+ '\n' +str(premios)+ '\n' ,title= 'Resultado da Busca', image= 'poster.jpg')


    def requisicao(filme):
        req = requests.get('http://www.omdbapi.com/?i=' + filme + '&apikey=369a3949')
        dicionario = dict(json.loads(req.text))
        return dicionario


    def imdb_top_1000_rating():
        lista_completa = []
        for i in range(1, 3):
            try:
                lista_filmes_link = requests.get(link_lista + str(i))
                soup = BeautifulSoup(lista_filmes_link.text, 'html.parser')
                lista_filmes = soup.find_all('h3')
                for i in lista_filmes:
                    try:
                        teste = str(i.find('a'))
                        lista_completa.append(teste[16:25])
                    except:
                        pass
            except:
                "print('Quantidade de filmes da lista:', len(lista_completa))"
                break
        return lista_completa


    def roleta_russa(imdb_top_1000_rating):
        filme_escolhido = random.choice(imdb_top_1000_rating())
        return filme_escolhido


    detalhes_filme(requisicao(roleta_russa(imdb_top_1000_rating)))
