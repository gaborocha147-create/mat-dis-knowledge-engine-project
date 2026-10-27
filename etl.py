import re
import unicodedata
import pandas as pd

def atomo(texto):
    texto = str(texto)
    
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode("ascii")

    texto = texto.lower()

    texto = re.sub(r"[^a-z0-9]+", "_", texto)
    texto = texto.strip("_")
    
    if texto == "":
        texto = "desconhecido"
    return "'" + texto + "'"

def primeiro_da_lista(texto):
    """Pega o primeiro item de uma lista separada por virgula.
    Exemplo: "Action, Indie" -> "Action"
    """

    if pd.isna(texto):
        return "desconhecido"
    return str(texto).split(",")[0]

df = pd.read_csv("steam_games.csv")

linhas = []
for _, jogo in df.iterrows():
    nome = atomo(jogo["Nome"])
    desenvolvedora = atomo(primeiro_da_lista(jogo["Desenvolvedora"]))
    genero = atomo(primeiro_da_lista(jogo["Genero"]))
    ano = str(jogo["Ano"])[-4:]
    preco = jogo["Preco"]
    positivas = jogo["Positivas"]
    negativas = jogo["Negativas"]
    tempo = jogo["TempoMedio"]
 
    fato = f"jogo({nome}, {desenvolvedora}, {genero}, {ano}, {preco}, {positivas}, {negativas}, {tempo})."
    linhas.append(fato)
 
with open("base.pl", "w", encoding="utf-8") as arquivo:
    arquivo.write("% jogo(Nome, Desenvolvedora, Genero, Ano, Preco, Positivas, Negativas, TempoMedio)\n")
    for fato in linhas:
        arquivo.write(fato + "\n")
 
print(len(linhas), "fatos salvos em base.pl")

perguntas = """:- consult('base.pl').

aprovacao(Positivas, Negativas, Taxa) :-
    Total is Positivas + Negativas,
    Taxa is Positivas / Total * 100.

media(Lista, Media) :-
    sum_list(Lista, Soma),
    length(Lista, Quantidade),
    Media is Soma / Quantidade.

desenvolvedoras(Lista) :-
    findall(Dev, jogo(_, Dev, _, _, _, _, _, _), Repetidas),
    sort(Repetidas, Lista).

aprovacao_desenvolvedora(Dev, Media) :-
    findall(Taxa, (jogo(_, Dev, _, _, _, Positivas, Negativas, _), aprovacao(Positivas, Negativas, Taxa)), Taxas),
    media(Taxas, Media).

top_10_desenvolvedoras_de_jogos(Top10) :-
    desenvolvedoras(Lista),
    findall(Media-Dev, (member(Dev, Lista), aprovacao_desenvolvedora(Dev, Media)), Pares),
    sort(0, @>=, Pares, Ranking),
    length(Top10, 10),
    append(Top10, _, Ranking).

media_gratuitos(Media) :-
    findall(Taxa, (jogo(_, _, _, _, Preco, Positivas, Negativas, _), Preco =:= 0, aprovacao(Positivas, Negativas, Taxa)), Taxas),
    media(Taxas, Media).

media_pagos(Media) :-
    findall(Taxa, (jogo(_, _, _, _, Preco, Positivas, Negativas, _), Preco > 0, aprovacao(Positivas, Negativas, Taxa)), Taxas),
    media(Taxas, Media).

gratuitos_vs_pagos_ratings(Gratuitos, Pagos, Melhor) :-
    media_gratuitos(Gratuitos),
    media_pagos(Pagos),
    (Gratuitos > Pagos -> Melhor = gratuitos ; Melhor = pagos).

anos(Lista) :-
    findall(Ano, jogo(_, _, _, Ano, _, _, _, _), Repetidos),
    sort(Repetidos, Lista).

melhor_do_ano(Ano, Jogo, Taxa) :-
    findall(T-J, (jogo(J, _, _, Ano, _, Positivas, Negativas, _), aprovacao(Positivas, Negativas, T)), Pares),
    max_member(Taxa-Jogo, Pares).

melhor_jogo_por_ano(Ano, Jogo, Taxa) :-
    anos(Lista),
    member(Ano, Lista),
    melhor_do_ano(Ano, Jogo, Taxa).
"""

with open("perguntas.pl", "w", encoding="utf-8") as arquivo:
    arquivo.write(perguntas)
    
print("Perguntas salvas em perguntas.pl")