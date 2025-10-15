from flask import *;
import os

app = Flask(__name__)
app.secret_key = 'J!dGo4Zs#67$hde'

usuarios = [['d@g', 'denilson', '1', '10-10-2000']]
adms = [['m@g', 'mariany', '2', '15-05-2015']]
filmes =  [[
    'agrandeviagemdasuavida.png',
    'A Grande Viagem da Sua Vida',
    'A Grande Viagem da Sua Vida conta a história de David e Sarah, dois desconhecidos que se conhecem em um casamento e acabam embarcando juntos em uma viagem inesperada. Guiados pelo GPS de um carro antigo, eles chegam a um campo misterioso com uma porta vermelha que os transporta para uma jornada fantástica no tempo. Revivendo momentos marcantes de suas vidas, os dois criam uma conexão especial e refletem sobre o passado, enquanto vislumbram novas possibilidades para o futuro.',
    'https://www.youtube.com/watch?v=bQNA_KrpUkI',
    '01:49',
    'Romance',
    '16', [    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'], [    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', 
    '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', 
    '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', 
    '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'], [    '00:00', '01:00', '02:00', '03:00', '04:00', '05:00', 
    '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', 
    '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', 
    '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'], [], [], []
  ],
  [
    'guardioesdagalaxia.png',
    'Guardiões da Galáxia',
    'Peter Quill, um aventureiro intergaláctico, rouba uma esfera cobiçada por um vilão poderoso chamado Ronan. Para escapar, ele une forças com um grupo de desajustados: Rocket, Groot, Gamora e Drax. Juntos, eles formam os Guardiões da Galáxia e precisam salvar o universo de uma ameaça devastadora.',
    'https://www.youtube.com/watch?v=d96cjJhvlMA',
    '02:01',
    'Ficção Científica',
    '12', [], [], [], [], [], []
  ],
  [
    'corra.png',
    'Corra!',
    'Chris, um jovem negro, vai visitar a família de sua namorada branca pela primeira vez. O que parecia ser um encontro normal se transforma em um pesadelo quando ele descobre segredos perturbadores sobre a comunidade local, revelando um esquema macabro que ameaça sua vida.',
    'https://www.youtube.com/watch?v=sRfnevzM9kQ',
    '01:44',
    'Suspense',
    '16', [], [], [], [], [], []
  ]
]


@app.route('/listarimagens')
def listar_imagens():
    imgs = os.listdir('static/imagens')
    return render_template('listarimagens.html', imgs = imgs)

@app.route('/')
def home_page():
    return render_template('paginaInicial.html', filmes = filmes)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/lanchonete')
def lanchonete():
    return render_template('lanchonete.html')

@app.route('/cinema')
def cinema():
    return render_template('cinema.html', filmes = filmes)

@app.route('/versessoes')
def versessoes():
    nomeFilme = request.values.get('nomeFilme')
    dia = request.values.get('dia')
    for filme in filmes:
        if filme[1] == nomeFilme:
            return render_template('sessoes.html', filme = filme, dia = dia )   

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/paginaadiconarfilme')
def pag_adicionar():

    if 'tipo' not in session or session['tipo'] != 'adm':
       return render_template('paginaInicial.html')
    
    return render_template('pagadicionar.html')

@app.route('/paginaAdm')
def paginaAdm():

    if 'tipo' not in session or session['tipo'] != 'adm':
       return render_template('paginaInicial.html')
    
    return render_template('paginaAdm.html', filmes = filmes)

@app.route('/verFilme')
def verFilme():

    global filmes
    nomeFilme = request.values.get('nomeFilme')
    diasessao = request.form.get('diasessao')
    infFilme = None
    for filme in filmes:
        if nomeFilme == filme[1]:
            infFilme = filme
            break
    return render_template('filme.html', filme = infFilme, diasessao = diasessao)

@app.route('/adicionarsessao', methods=['post'])
def adicionarSessao():

    if 'tipo' not in session or session['tipo'] != 'adm':
       return render_template('paginaInicial.html')

    global filmes
    opdia = request.form.get('diaSessao')
    horario = request.form.get('horario')
    idfilme = int(request.form.get('idfilme'))

    if opdia == 'segunda':
        indicedia = 7
    elif opdia == 'terca':
        indicedia = 8
    elif opdia == 'quarta':
        indicedia = 9
    elif opdia == 'quinta':
        indicedia = 10
    elif opdia == 'sexta':
        indicedia = 11
    elif opdia == 'sabado':
        indicedia = 12

    filmes[idfilme][indicedia].append(horario)
   
    return render_template('paginaAdm.html')

@app.route('/cadastrar', methods=['post'])
def cadastrar():

    global filmes
    mensagem = 'senhas incorretas'
    email = request.form.get('emailUsuario')
    nome = request.form.get('nomeUsuario')
    senha = request.form.get('senhaUsuario')
    conf_senha = request.form.get('confirmacaoSenhaUsuario')
    dt = request.form.get('nascimentoUsuario')

    if senha == conf_senha:
        usuarios.append([email, nome, senha, dt])
        return render_template('login.html')
    else:
        return render_template('cadastro.html', msg = mensagem)

@app.route("/adicionarFilme", methods=['post'])
def adicionarFilme():

    if 'tipo' not in session or session['tipo'] != 'adm':
       return render_template('paginaInicial.html')

    global filmes
    filmenaoexiste = True
    imagem = request.form.get('imagemFilme')
    nome = request.form.get('nomeFilme')
    descricao = request.form.get('descriçãoFilme')
    link = request.form.get('linkFilme')
    duracao = request.form.get('duracaoFilme')
    opCla = request.form.get('classificacaoFilme')
    opGen = request.form.get('generoFilme')
    genero = ''
    classificacao = ''
    
    if opGen == 'terror':
        genero = 'Terror'
    elif opGen == 'comedia':
        genero = 'Comédia'
    elif opGen == 'romance':
        genero = 'Romance'
    elif opGen == 'suspense':
        genero = 'Suspense'
    elif opGen == 'ficcaoCien':
        genero = 'Ficção Cientifica'
    elif opGen == 'animacao':
        genero = 'Animação'

    if opCla == 'livre':
        classificacao = 'Livre'
    elif opCla == '12':
        classificacao = '12'
    elif opCla == '14':
        classificacao = '14'
    elif opCla == '16':
        classificacao = '16'
    elif opCla == '18':
        classificacao = '18'
    
    for filme in filmes:
        if filme == [imagem, nome, descricao, link, duracao, genero, classificacao]:
           filmenaoexiste = False
           mensagem = 'Algo deu errado'
    if filmenaoexiste:
        filmes.append([imagem, nome, descricao, link, duracao, genero, classificacao, [], [], [], [], [], []])
        mensagem = 'Adicionado com sucesso'
    return render_template('paginaAdm.html', msg = mensagem, filmes = filmes)

@app.route('/logar', methods=['post'])
def logar():

    email = request.form.get('emailUsuario')
    senha = request.form.get('senhaUsuario')
    opcao = request.form.get('admtrue')
    mensagem = 'Usuario não encontrado'
            
    if opcao:
        for adm in adms:
            if email == adm[0] and senha == adm[2]:
                session['login'] = email
                session['tipo'] = 'adm'
                return render_template("paginaAdm.html", filmes = filmes)
                
    else:        
        for usuario in usuarios:
            if email == usuario[0] and senha == usuario[2]:
                session['login'] = email
                session['tipo'] = 'cliente'
                return render_template("paginaInicial.html")

    return render_template('login.html', msg = mensagem)

if __name__ == "__main__":
    app.run(debug=True)