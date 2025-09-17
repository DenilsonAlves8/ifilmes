from flask import *;

app = Flask(__name__)

usuarios = [['d@g', 'denilson', '1', '10-10-2000']]
adms = [['m@g', 'mariany', '2', '15-05-2015']]
filmes = []

@app.route('/')
def home_page():
    return render_template('paginaInicial.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cinema')
def cinema():
    return render_template('cinema.html', filmes = filmes)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/verFilme')
def verFilme():
    return render_template('filme.html')

@app.route('/cadastrar', methods=['post'])
def cadastrar():

    global usuarios
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

@app.route("/adicionarFilme")
def adicionarFilme():

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

    filmes.append([nome, descricao, link, duracao, genero, classificacao])
    mensagem = 'Adicionado com sucesso.'
    return render_template('paginaAdm.html', msg = mensagem)
       
@app.route('/logar', methods=['post'])
def logar():

    email = request.form.get('emailUsuario')
    senha = request.form.get('senhaUsuario')
    opcao = request.form.get('admtrue')
    mensagem = 'Usuario não encontrado'
    
    if opcao:
        for adm in adms:
            if email == adm[0] and senha == adm[2]:
                return render_template("paginaAdm.html")
    else:        
        for usuario in usuarios:
            if email == usuario[0] and senha == usuario[2]:
                return render_template("paginaInicial.html")

    return render_template('login.html', msg = mensagem)

if __name__ == "__main__":
    app.run(debug=True)