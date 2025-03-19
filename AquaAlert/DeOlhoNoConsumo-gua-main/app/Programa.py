from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "chave_secreta"  # chave para usar flash messages

# Configuração do banco de dados
def init_sqlite_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_sqlite_db()  # Inicializa o banco de dados

# Página inicial
@app.route('/')
def index():
    return redirect(url_for('login'))

# Rota para cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect('usuarios.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            flash("Cadastro realizado com sucesso!", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Nome de usuário já existe!", "error")

    return render_template('cadastro.html')

# Rota para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[0], password):
            session['username'] = username
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for('calculo'))
        else:
            flash("Usuário ou senha inválidos.", "error")

    return render_template('login.html')

# Rota para cálculo
@app.route('/calculo', methods=['GET', 'POST'])
def calculo():
    if 'username' not in session:
        flash("Por favor, faça login para acessar esta página.", "error")
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            # Coleta os dados do formulário
            dados = {
                "tempobanho": float(request.form["tempobanho"]),
                "qtdebanho": int(request.form["qtdebanho"]),
                "tempo_torneira_maos": float(request.form["tempo_torneira_maos"]),
                "qtdeusotorneiramaos": int(request.form["qtdeusotorneiramaos"]),
                "tempo_torneira_escovardentes": float(request.form["tempo_torneira_escovardentes"]),
                "qtdeusotorneiradentes": int(request.form["qtdeusotorneiradentes"]),
                "tempo_torneira_lavarlouça": float(request.form["tempo_torneira_lavarlouça"]),
                "qtdeusotorneiralouça": int(request.form["qtdeusotorneiralouça"]),
                "arejador": int(request.form["arejador"]),
                "qtdedescarga": int(request.form["qtdedescarga"]),
                "volumeatual": float(request.form["volumeatual"]),
                "reais_atual": float(request.form["reais_atual"]),
                "categoria": int(request.form["categoria"])
            }

            # Adaptação da lógica de cálculo para Flask
            desperdicio_total_m3 = calcular_desperdicio(dados)

            # Resultado simplificado para exemplo
            return render_template(
                "resultado.html",
                desperdicio_total_m3=desperdicio_total_m3
            )
        except Exception as e:
            flash(f"Erro no cálculo: {e}", "error")

    return render_template('calculo.html')


# Função para o cálculo (adaptar o seu cálculo aqui)
def calcular_desperdicio(dados):
    # Substitua esta função pela lógica completa do cálculo que você forneceu
    return 10  # Exemplo: Retorna um valor fixo de desperdício

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("Você saiu com sucesso.", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)