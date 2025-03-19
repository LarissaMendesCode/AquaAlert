from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "chave-secreta"  # Necessário para o uso de sessões e mensagens flash

# Função para criar o banco de dados (executar apenas uma vez)
def criar_banco():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

#Página inicial (home)
@app.route("/")
def home():
    return render_template("Home.html")



# Funções de Cálculo
def calcular_chuveiro(tempobanho, qtdebanho):
    consumo = qtdebanho * tempobanho * 0.2 * 60
    desperdicio = max(consumo - 48, 0)
    economia = max(48 - consumo, 0)
    return consumo, desperdicio, economia


def calcular_torneira(dados):
    fator_vazao = 0.15 if dados["arejador"] == "1" else 0.30
    consumo_maos = dados["tempo_maos"] * dados["vezes_maos"] * fator_vazao * 60
    consumo_dentes = dados["tempo_dentes"] * dados["vezes_dentes"] * fator_vazao * 60
    consumo_louca = dados["tempo_louca"] * dados["vezes_louca"] * fator_vazao * 60
    consumo_total = consumo_maos + consumo_dentes + consumo_louca
    desperdicio = max(consumo_total - 27, 0)
    economia = max(27 - consumo_total, 0)
    return consumo_total, desperdicio, economia


def calcular_descarga(qtd_descarga):
    consumo = qtd_descarga * 6
    desperdicio = max(consumo - 30, 0)
    economia = max(30 - consumo, 0)
    return consumo, desperdicio, economia


def calcular_fatura(desperdicio_total_m3, volumeatual, reais_atual, categoria):
    volume = volumeatual - desperdicio_total_m3
    esgoto = round(volume * 0.8)
    faixa_precos = {
        1: 2.12,
        2: [4.34, 7.38, 8.00],
        3: [6.17, 8.00, 8.65],
    }

    if categoria == 1:
        custo_agua = volume * faixa_precos[1]
    elif categoria in (2, 3):
        precos = faixa_precos[categoria]
        if volume <= 10:
            custo_agua = volume * precos[0]
        elif volume <= 20:
            custo_agua = 10 * precos[0] + (volume - 10) * precos[1]
        else:
            custo_agua = 10 * precos[0] + 10 * precos[1] + (volume - 20) * precos[2]
    else:
        custo_agua = 0

    custo_esgoto = esgoto * 2.12
    total = custo_agua + custo_esgoto
    economia = reais_atual - total
    return round(custo_agua, 2), round(custo_esgoto, 2), round(total, 2), round(economia, 2)


# Rotas
@app.route("/index", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    # Recebendo dados do formulário
    dados = {
        "tempobanho": float(request.form["tempobanho"]),
        "qtdebanho": int(request.form["qtdebanho"]),
        "tempo_maos": float(request.form["tempo_maos"]),
        "vezes_maos": int(request.form["vezes_maos"]),
        "tempo_dentes": float(request.form["tempo_dentes"]),
        "vezes_dentes": int(request.form["vezes_dentes"]),
        "tempo_louca": float(request.form["tempo_louca"]),
        "vezes_louca": int(request.form["vezes_louca"]),
        "arejador": request.form["arejador"],
        "qtd_descarga": int(request.form["qtd_descarga"]),
        "volumeatual": float(request.form["volumeatual"]),
        "reais_atual": float(request.form["reais_atual"]),
        "categoria": int(request.form["categoria"]),
    }

    # Cálculos
    consumo_chuveiro, desperdicio_chuveiro, economia_chuveiro = calcular_chuveiro(
        dados["tempobanho"], dados["qtdebanho"]
    )
    consumo_torneira, desperdicio_torneira, economia_torneira = calcular_torneira(dados)
    consumo_descarga, desperdicio_descarga, economia_descarga = calcular_descarga(
        dados["qtd_descarga"]
    )

    desperdicio_total_m3 = (desperdicio_chuveiro + desperdicio_torneira + desperdicio_descarga) / 1000 * 30

    custo_agua, custo_esgoto, total, economia = calcular_fatura(
        desperdicio_total_m3, dados["volumeatual"], dados["reais_atual"], dados["categoria"]
    )

    # Renderizar página com resultados
    return render_template(
        "resultado.html",
        consumo_chuveiro=consumo_chuveiro,
        desperdicio_chuveiro=desperdicio_chuveiro,
        economia_chuveiro=economia_chuveiro,
        consumo_torneira=consumo_torneira,
        desperdicio_torneira=desperdicio_torneira,
        economia_torneira=economia_torneira,
        consumo_descarga=consumo_descarga,
        desperdicio_descarga=desperdicio_descarga,
        economia_descarga=economia_descarga,
        custo_agua=custo_agua,
        custo_esgoto=custo_esgoto,
        total=total,
        economia=economia,
    )
# Rota para cadastro
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            flash("Cadastro realizado com sucesso!", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Usuário já existente!", "error")
    
    return render_template("Cadastro.html")


# Rota para login
@app.route("/Login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("index"))
        else:
            flash("Credenciais inválidas!", "error")
    return render_template("Login.html")

# Rota para logout
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for("Home"))


if __name__ == "__main__":
    criar_banco()  # Executa a criação do banco antes de rodar o servidor
    app.run(debug=True)

conn = sqlite3.connect("database.db", timeout=10)
