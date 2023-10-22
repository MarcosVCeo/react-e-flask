from __init__ import app
from flask import render_template, jsonify


class Colaborador:
    def __init__(self, nome, cargo, link_imagem):
        self.nome = nome
        self.cargo = cargo
        self.link_imagem = link_imagem

    def toJson(self):
        return {
            "nome": self.nome,
            "cargo": self.cargo,
            "link_imagem": self.link_imagem
        }

_times = [
    "Programação",
    "Front-End",
    "Data Science",
    "Devops",
    "UX e Desing",
    "Mobile",
    "Inovação e Gestão"
]

_itens = [
    Colaborador("Colaborador um", "Desenvolvedor full-stack", ""),
    Colaborador("Colaborador dois", "Desenvolvedor front-end", ""),
    Colaborador("Colaborador tres", "desempregado", "")
]




@app.route("/")
def index():
    return render_template(
        "index.html",
        times=jsonify(_times).json,
        lista=jsonify(list(map(lambda x: x.toJson(), _itens))).json
    )
    
app.run(port=8080, debug=True)
