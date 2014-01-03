# -*- coding: utf-8 -*-
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    #from gluon.contrib.heroku import *
    #try: db = DAL(os.environ.get('DATABASE_URL'))
    #except: db = get_db(name=None, pool_size=10)
    #db = DAL('sqlite://storage.db')
    db = DAL('mysql://jbtte:mysql1234@mysql.server/jbtte$questoes')
else:
    db = DAL('google:datastore')
    session.connect(request, response, db=db)


from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)


db.define_table('administrativo',
   Field('enunciado', "text"),
   Field('explicacao', "text"),
   Field('resposta', "integer"),
   Field('banca', 'integer'),
   Field('assunto', 'integer'),
   Field('respondida', 'integer'))
   

db.define_table('civil_1',
   Field('enunciado', "text"),
   Field('explicacao', "text"),
   Field('resposta', "integer"),
   Field('banca', 'integer'),
   Field('assunto', 'integer'))
   
db.define_table('penal',
   Field('enunciado', "text"),
   Field('explicacao', "text"),
   Field('resposta', "integer"),
   Field('banca', 'integer'),
   Field('assunto', 'integer'))
   
db.define_table('proc_penal',
   Field('enunciado', "text"),
   Field('explicacao', "text"),
   Field('resposta', "integer"),
   Field('banca', 'integer'),
   Field('assunto', 'integer'))
   
db.define_table('const',
   Field('enunciado', "text"),
   Field('explicacao', "text"),
   Field('resposta', "integer"),
   Field('banca', 'integer'),
   Field('assunto', 'integer'))

db.define_table('banca',
    Field('numero', 'integer'),
    Field('nome'))
    

db.define_table('materia_civil_1',
    Field('mateira'),
    Field('num_questoes', 'integer'))

db.define_table('materia_administrativo',
    Field('mateira'),
    Field('num_questoes', 'integer'))

db.define_table('materia_const',
    Field('mateira'),
    Field('num_questoes', 'integer'))

db.define_table('materia_penal',
    Field('mateira'),
    Field('num_questoes', 'integer'))

db.define_table('materia_proc_penal',
    Field('mateira'),
    Field('num_questoes', 'integer'))
