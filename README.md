# Knowledge Engine: Steam Games

Projeto que transforma um dataset de jogos da Steam em uma base de conhecimento em Prolog e responde perguntas sobre ela.

## Dataset

- [Steam Games Dataset (Kaggle)](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset)
- **Limitação:** só jogos com pelo menos 5.000 avaliações (2.731 jogos no total)

Campos usados:

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | qualitativo | nome do jogo |
| Desenvolvedora | qualitativo | primeira desenvolvedora listada |
| Genero | qualitativo | primeiro gênero listado |
| Ano | quantitativo | ano de lançamento |
| Preco | quantitativo | preço em dólares |
| Positivas | quantitativo | avaliações positivas |
| Negativas | quantitativo | avaliações negativas |
| TempoMedio | quantitativo | tempo médio de jogo (minutos) |

## ETL (etl.py)

1. **Extração:** lê o `games.csv` para que mantém só as 8 colunas acima.
2. **Transformação:** filtra os jogos com 5.000+ avaliações, transforma os textos em átomos de Prolog e extrai o ano da data.
3. **Carga:** escreve um fato por jogo no `base.pl` e as regras no `perguntas.pl`.

Exemplo de fato:

```prolog
jogo('team_fortress_2', 'valve', 'action', 2007, 0.0, 1044264, 117208, 23093).
```
## Perguntas

A taxa de aprovação de um jogo é `positivas / (positivas + negativas) * 100`.

1. **Quais desenvolvedoras têm a maior aprovação média?**
   `top_10_desenvolvedoras_de_jogos(Top10).`
2. **Jogos gratuitos ou jogos pagos são mais bem avaliados?**
   `gratuitos_vs_pagos_ratings(Gratuitos, Pagos, Melhor).`
3. **Qual foi o jogo mais bem avaliado de cada ano?**
   `melhor_jogo_por_ano(Ano, Jogo, Taxa).`

## Como rodar

1. Instale o pandas e rode o ETL:
   ```
   pip install pandas
   python etl.py
   ```
2. Abra o Prolog com as perguntas:
   ```
   swipl perguntas.pl
   ```
3. Digite as consultas da seção "Perguntas".

## Resultados esperados

`top_10_desenvolvedoras_de_jogos(Top10).`

```
Top10 = [99.43670323154463-howlin_hugs, 99.25755700901539-flipline_studios, 99.2128801431127-something_we_made, 99.16072177926982-adamgryu, 99.09249243743697-igara_studio, 99.04438477333754-kayanimate, 98.82749759074846-gb_patch_games, 98.66143137604854-matt_roszak, …- …|…].
```

`gratuitos_vs_pagos_ratings(Gratuitos, Pagos, Melhor).`

```
Gratuitos = 80.62467776821616,
Pagos = 86.22901039131773,
Melhor = pagos.
```

`melhor_jogo_por_ano(Ano, Jogo, Taxa).`

```
Ano = 1997,
Jogo = postal,
Taxa = 90.9280595119296 ;
Ano = 1998,
Jogo = half_life,
Taxa = 96.53557862920908 ;
Ano = 1999,
Jogo = half_life_opposing_force,
Taxa = 95.31317241109502 ;
Ano = 2000,
Jogo = counter_strike,
Taxa = 97.43171691742093 ;
Ano = 2001,
Jogo = half_life_blue_shift,
Taxa = 92.49760561881452 ;
Ano = 2002,
Jogo = mafia,
Taxa = 87.47460182211444 ;
Ano = 2003,
Jogo = day_of_defeat,
Taxa = 90.31258800337933 ;
Ano = 2004,
Jogo = half_life_2,
Taxa = 97.59554120678916 ;
Ano = 2005,
Jogo = sid_meier_s_pirates,
Taxa = 94.57499274731651 ;
Ano = 2006,
Jogo = garry_s_mod,
Taxa = 96.79565614418124 ;
Ano = 2007,
Jogo = portal,
Taxa = 98.47137126493043 ;
Ano = 2008,
Jogo = left_4_dead,
Taxa = 96.32920800077552 ;
Ano = 2009,
Jogo = plants_vs_zombies_goty_edition,
Taxa = 97.60514561372163 ;
Ano = 2010,
Jogo = mount_blade_warband,
Taxa = 97.73264024518494 ;
Ano = 2011,
Jogo = portal_2,
Taxa = 98.69091831791654 ;
Ano = 2012,
Jogo = dishonored,
Taxa = 97.64113147990773 ;
Ano = 2013,
Jogo = the_wolf_among_us,
Taxa = 97.85862436235216 ;
Ano = 2014,
Jogo = one_finger_death_punch,
Taxa = 97.93751150942238 ;
Ano = 2015,
Jogo = clannad,
Taxa = 98.46534143578123 ;
Ano = 2016,
Jogo = aseprite,
Taxa = 99.09249243743697 ;
Ano = 2017,
Jogo = vtol_vr,
Taxa = 98.09479553903346 ;
Ano = 2018,
Jogo = epic_battle_fantasy_5,
Taxa = 98.66143137604854 ;
Ano = 2019,
Jogo = a_short_hike,
Taxa = 99.16072177926982 ;
Ano = 2020,
Jogo = senren_banka,
Taxa = 98.85351950297829 ;
Ano = 2021,
Jogo = toem_a_photo_adventure,
Taxa = 99.2128801431127 ;
Ano = 2022,
Jogo = vampire_survivors,
Taxa = 98.46005736336255 ;
Ano = 2023,
Jogo = papa_s_freezeria_deluxe,
Taxa = 99.25755700901539 ;
Ano = 2024,
Jogo = the_werecleaner,
Taxa = 99.43670323154463 ;
Ano = 2025,
Jogo = rhythm_doctor,
Taxa = 98.43492198180361.
```