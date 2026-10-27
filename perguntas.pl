:- consult('base.pl').

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
