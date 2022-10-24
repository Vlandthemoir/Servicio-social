from flask import render_template
from flask_mysqldb import MySQL
from . import blog
from app import db 


def query(table):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM "+table)
    result = cur.fetchall()
    return result

def queryLimit(table,position,amount):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM "+table+" LIMIT "+position+","+amount)
    result = cur.fetchall()
    return result

def queryCount(table,data='*'):
    cur = db.connection.cursor()
    if (data == '*'):
        cur.execute("SELECT COUNT(*) FROM "+table)
        tup = cur.fetchall()
    elif (data != '*' ):
        cur.execute("SELECT COUNT("+data+") FROM "+table)
        tup = cur.fetchall()

    string = str(tup)
    characters ="(,)' "
    for x in range(len(characters)):
            string = string.replace(characters[x],"")

    nstring = "".join(string)
    result = int(nstring)
    return result

def eventsbar():
    data = query('eventos')
    return data


@blog.route('/')
def home():
    #data = queryCount('taller_verano')
    return render_template('home.html',eventos = eventsbar())

@blog.route('/talleres-verano')
def verano():
    return render_template('verano.html',verano = query('taller_verano'),eventos = eventsbar())

@blog.route('/talleres-permanentes')
def permanente():
    return render_template('permanentes.html',permanentes = query('taller_permanente'),eventos = eventsbar())

@blog.route('/galeria')
def galeria():
    medio = round(queryCount('galeria')/3)
    data1 = queryLimit("galeria",str(0),str(medio))
    data2 = queryLimit("galeria",str(medio),str(medio))
    data3 = queryLimit("galeria",str(medio*2),str(queryCount('galeria')-(medio*2)))
    return render_template('galeria.html',eventos = eventsbar(),col1 = data1,col2 = data2,col3 = data3)

@blog.route('/galeria/<title>')
def imagen(title):
    return render_template('imagen.html',eventos = eventsbar(),galeria = query('galeria'),filtro = title)

@blog.route('/calendario')
def calendario():
    return render_template('calendario.html', eventos = eventsbar())

@blog.route('/articulos')
def articulos():
    return render_template('articulos.html',articulos = query('articulos'), eventos = eventsbar())

@blog.route('/articulo/<title>')
def articulo(title):
    return render_template('articulo.html',eventos = eventsbar(), articulo = query('articulos'),filtro = title)

@blog.route('/articulos/categoria/<tag>')
def categoria(tag):
    return render_template('categoria.html',articulos = query('articulos'),eventos = eventsbar(),filtro = tag)


