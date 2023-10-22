import React from "react";
import CampoTexto from "../CampoTexto";
import './Formulario.css';
import ListaSuspensa from "../ListaSuspensa";

const Formulario = () => {
    return (
        <section className="formulario">
            <form>
                <h2>Preencha os dados para criar o card do colaborador</h2>
                <CampoTexto label="Nome" placeholder="Digite seu nome" />
                <CampoTexto label="Cargo" placeholder="Digite seu cargo" />
                <CampoTexto label="Imagem" placeholder="Digite o endereço da imagem" />
                <ListaSuspensa label="Times" itens={window.times} />
            </form>
        </section>
    )
}

export default Formulario