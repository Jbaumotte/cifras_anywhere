def user():
    return dict(form=auth())

def index():
    import cifra_club
    response.title = " "
    form = SQLFORM.factory(Field('url',
                                 label=T('Insira o link: '),
                                 requires=IS_MATCH('http://www.cifraclub.com.br/', error_message='Desculpa, por enquanto, so CifraClub')))

    if auth.user_id != 0:
        musica = db.music
        user = (db.music.user == auth.user_id)
        myset = db(user)
        rows = myset.select(musica.musica, orderby=~musica.id, limitby=(0, 5))


    if form.process().accepted:

        cifra = cifra_club.get_song(form.vars.url)
        session.url = form.vars.url
        ## cifra[0] = name; cifra[1] = nome_musica; cifra[2] = letra
        session.name = cifra[0].title().split("-")[0]
        session.banda = cifra[0].split("-")[1]
        session.nome_musica = cifra[1]
        session.letra = cifra[2].strip()
        redirect(URL('cifra'))

    return dict(form=form, rows=rows)

@auth.requires_login()
def cifra():
    response.title = session.name
    response.subtitles = session.banda
    db.music.insert(user=auth.user_id, musica=session.name, banda=session.banda, url = session.url)
    return dict()

def evernote():
    import evernote_song
    evernote_song.evernote_song(session.name, session.banda, session.letra)
    response.flash='Gravado no Evernote!'
    #redirect(URL('ever'))
    return ("")


def get_me_a_pdf():
    from reportlab.platypus import *
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.rl_config import defaultPageSize
    from reportlab.lib.units import inch, mm
    from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
    from reportlab.lib import colors
    from uuid import uuid4
    from cgi import escape
    import os

    title = session.name.replace("\r", "").replace("\t", "")
    heading = session.banda
    text = session.letra


    styles = getSampleStyleSheet()
    tmpfilename=os.path.join(request.folder,'private',str(uuid4()))
    doc = SimpleDocTemplate(tmpfilename)
    story = []
    story.append(Paragraph(escape(title),styles["Heading1"]))
    story.append(Paragraph(escape(heading),styles["Heading3"]))
    story.append(Preformatted(escape(text), styles["Normal"]))
    story.append(Spacer(1,2*inch))
    doc.build(story)
    data = open(tmpfilename,"rb").read()
    os.unlink(tmpfilename)
    response.headers['Content-Type']='application/pdf'
    return data

def update_song():
    nova_letra = list(request.post_vars.keys())
    session.letra = nova_letra[0]
    response.flash='Cifra Atualizada'
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())
